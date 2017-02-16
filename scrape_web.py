from lxml import html
import requests
from selenium import webdriver
import time


#Actual web scraping
class WebScrape(object):

    # Constructor
    # Initialize the URL
    # Return:  None
    def __init__(self, **kwargs):
        self.url = kwargs['url']


    # Get the page content
    # Params: html element, attribute, and value through kwars
    # Return: Atomic values
    def get_Page_Content(self,**kwargs):
        page = requests.get(self.url)
        tree = html.fromstring(page.content)
        val = self.stringyfy( tree.xpath(self.get_xpath(**kwargs) ) )
        return val

    # Clean Xpath result
    # Params: list of results
    # Return: Stringify
    def stringyfy (self,list):
        str = ''.join(list)
        #str = str.replace("\n", " ")
        return str

    # Build the xpath
    # Return: Xpath
    def get_xpath(self, **kwargs):
        htmlElem = kwargs['html_elem']
        htmlAttr = kwargs['attr']
        attrName = kwargs['attr_name']
        xpath = '//'+ htmlElem+'[@'+htmlAttr+'="'+attrName+'"]/text()';
        return xpath

    def clist(self):
        driver = webdriver.Chrome('./driver/chromedriver')
        driver.get('https://www.facebook.com')
        time.sleep(3)
        search_box = driver.find_element_by_name('email')
        search_box.send_keys('josephtrop@yahoo.com')
        search_box = driver.find_element_by_name('pass')
        search_box.send_keys('q1w2e3r4')
        search_box.submit()
        time.sleep(20)  # Let the user actually see something!
       # driver.quit()





if __name__ == "__main__":
    WebScrape(url="https://sandiego.craigslist.org/nsd/fbh/5995669616.html").clist()
        #.get_Page_Content(html_elem="section", attr="id", attr_name="postingbody")







