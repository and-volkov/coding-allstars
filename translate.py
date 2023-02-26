import logging
from logging.handlers import RotatingFileHandler

from googletrans import Translator
from bs4 import BeautifulSoup

log_level = logging.INFO
log_file_handler = RotatingFileHandler(
    filename="translation.log",
    mode="a",
    maxBytes=5 * 1024 * 1024,
    backupCount=2,
    encoding=None,
    delay=0,
)
logging.basicConfig(
    encoding="utf-8",
    level=log_level,
    format="%(asctime)s %(levelname)s: %(name)s:\n%(message)s",
    handlers=[log_file_handler],
)


class Translation:
    """Translate the text in the html files."""

    def __init__(
            self,
            files: list[str],
            translator: Translator,
            blacklist: list = None,
            logger: logging.Logger = logging.getLogger(__name__)
    ):
        if blacklist is None:
            blacklist = []
        self.files = files
        self.blacklist = blacklist
        self.translator = translator
        self.logger = logger

    def translate(
            self, target_language: str, source_language: str = "auto"
    ) -> None:
        counter = 0
        files_count = len(self.files)
        for file in self.files:
            print(f"Translating {file}...")
            counter += 1
            with open(file, "r") as f:
                soup = BeautifulSoup(f, "html.parser")
                text = soup.find_all(string=True)

                soup_before = str(soup.prettify("utf-8"))

                for t in text:
                    if t.parent.name not in self.blacklist and t.split():
                        try:
                            translated = self.translator.translate(
                                t.string,
                                dest=target_language,
                                src=source_language,
                            ).text
                            print(translated)
                            t.replace_with(translated)
                        except Exception as e:
                            self.logger.error(e)
                            pass

            with open(file, "wb") as f:
                f.write(soup.prettify("utf-8"))

            soup_after = str(soup.prettify("utf-8"))
            try:
                assert soup_before != soup_after, "Translation failed."
            except AssertionError as e:
                counter -= 1
                self.logger.error(e)
                self.logger.error(f"File: {file} was not translated.")

        self.logger.info(f"Translated {counter} files out of {files_count}.")
