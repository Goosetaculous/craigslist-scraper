from scrape_result import Results
import threading

CITIES = ['sandiego','lasvegas','losangeles']

HTML_ELEM = 'section'
HTML_ATTR = 'id'
HTML_ATTR_NAME = 'postingbody'

work = Results(city='losangeles',
               category='fbh',
               html=HTML_ELEM,
               attr =HTML_ATTR,
               attr_name=HTML_ATTR_NAME)
work.traverseDictionary()

