import googletrans
from googletrans import Translator
from bs4 import BeautifulSoup


soup = BeautifulSoup(
    open('wget/www.classcentral.com/index.html'), 'html.parser'
)
text = soup.findAll(string=True)

translator = Translator()

output = ''
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head',
    'input',
    'script',
    'style',
    'title',
]

for t in text:
    if t.parent.name not in blacklist:
        t = t.split()
        if t:
            source_str = ' '.join(t) + '\n'
            try:
                translated = translator.translate(
                    source_str, dest='hi', src='en'
                ).text
                print(translated)
                output += translated
            except AttributeError:
                pass
        # print(soup.find(str(t)))

print(output)
