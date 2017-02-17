from scrape_result import Results
import threading

CITIES = ['sandiego','lasvegas','losangeles']


work = Results(city='sandiego',
               category='fbh')
work.traverseDictionary()

