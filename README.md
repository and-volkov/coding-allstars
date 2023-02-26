# coding allstars entry task

### Tech used
* Python 3.11
* Nginx
* beautifulsoup4
* selenium
* googletrans
* GNU Wget

### Web page is available on
[Web-page](http://167.99.129.13/index.html)

### About project
I used wget to get all html pages with depth 1 except main page. 
For main page I used selenium to "work-around" lazy loading. 
After that I used beautifulsoup to parse all html pages and
translate text on them with googletrans to hindi.
To host project I used DigitalOcean Ubuntu server.
I set up nginx to serve static files.

Not done - drop-down menu from the main page. Couldn't get it to work with selenium.