from lxml import html
import requests
import UserString

class WebScrape(object):



    def __init__(self, **kwargs):
        """
        Constructor
        :param kwargs: html_elem,attr,attr_name,city,cl_id
        """
        self.url = kwargs['url']
        self.city = kwargs['city']


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



if __name__ == "__main__":
    WebScrape(url="http://www.babynames.com/Names/A/",city="none").get_Page_Content("x",html_elem="a", attr="class", attr_name="M")
        #.clist()
        #.get_Page_Content("x",html_elem="a", attr="class", attr_name="M")







