from googletrans import Translator

from utils import get_html_files
from translate import Translation


BLACK_LIST = [
    "[document]",
    "noscript",
    "header",
    "html",
    "meta",
    "head",
    "input",
    "script",
    "style",
    "title",
]


def main():
    files = get_html_files()
    translator = Translator()
    translation = Translation(files, translator, BLACK_LIST)
    translation.translate(target_language="hi")  # hindi


if __name__ == "__main__":
    main()
