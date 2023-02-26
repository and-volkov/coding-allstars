# coding allstars entry task

### Tech used
* Python 3.11
* beautifulsoup4
* selenium
* googletrans
* GNU Wget

### About project
I used wget to get all html pages with depth 1 except main page. 
For main page I used selenium to "work-around" lazy loading. 
After that I used beautifulsoup to parse all html pages and
translate text on them with googletrans to hindi.

Not done - drop-down menu from the main page. Couldn't get it to work with selenium.