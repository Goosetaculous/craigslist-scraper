from BeautifulSoup import BeautifulSoup
import re
import urllib2




url = 'https://losangeles.craigslist.org/sgv/fbh/6006913779.html';
soup = BeautifulSoup(urllib2.urlopen(url).read());
reply = soup.findAll('a', attrs = {"id": "replylink"});
print (reply)
if reply:
   url = 'http://losangeles.craigslist.org' + reply[0].get('href');
   soup = BeautifulSoup(urllib2.urlopen(url).read());
   reply = soup.findAll(['div', 'a','p'], attrs = {"class": re.compile(r'anonemail|mailapp')});
   print( reply)
   if reply:
      reply[0].getText()