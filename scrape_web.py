from lxml import html
import requests
from selenium import webdriver
import time
import UserString


#Actual web scraping
class WebScrape(object):


    def __init__(self, **kwargs):
        """
        Constructor
        :param kwargs: html_elem,attr,attr_name,city,cl_id
        """
        self.url = kwargs['url']
        self.city = kwargs['city']


    # Get the page content
    # Params: html element, attribute, and value through kwars
    # Return: Atomic values
    def get_Page_Content(self,type,**kwargs):
        """
        :param kwargs,
        :return: Return the posting body
        """
        url=self.url
        if type == "reply":
            url=self.get_reply_url()

        page = requests.get(url)
        tree = html.fromstring(page.content)
        val = self.stringyfy( tree.xpath(self.get_xpath(**kwargs) ) )
        return val


    def get_reply_url(self):
        """
        :return: Return the reply url of the ad
        """
        replyURL= UserString.MutableString(self.url)
        del replyURL[replyURL.find('/fbh')-1]
        del replyURL[replyURL.find('/fbh') - 1]
        del replyURL[replyURL.find('/fbh') - 1]
        replyURL = str(replyURL)
        replacewith = self.get_city_cl_code(self.city)
        replyURL =  str(replyURL.replace(".org/",".org/reply/"+replacewith ).replace(".html",""))
        return (replyURL)


    def stringyfy(self,list):
        """
        Get the posting body
        :param list:
        :return: Actual posting text
        """
        str = ''.join(list)
        #str = str.replace("\n", " ")
        return str

    def get_city_cl_code(self,city):
        """
        Get Craigslist city code
        :param city:
        :return: craigslist city code
        """
        CITIES = {'sandiego':'sdo', 'lasvegas':'lvg', 'losangeles':'lax'} #nice trick for switch statement =)
        return CITIES.get(city)


    def get_xpath(self, **kwargs):
        """
        Get the text between html tags
        :param kwargs:
        :return: text between <p>test</p>  -> test
        """
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
        time.sleep(2)  # Let the user actually see something!
        search_box =  driver.find_element_by_class_name('_1frb')
        search_box.send_keys('Cody Barbo')
        search_box.submit()

        time.sleep(5)
        driver.get('https://www.facebook.com/search/str/Chef Groups/keywords_top')
        time.sleep(10)

       # driver.quit()
       # https: // www.facebook.com / search / str / Cody + Barbo / keywords_top

if __name__ == "__main__":
    WebScrape(url="http://www.babynames.com/Names/A/",city="none").get_Page_Content("x",html_elem="a", attr="class", attr_name="M")
        #.clist()
        #.get_Page_Content("x",html_elem="a", attr="class", attr_name="M")







