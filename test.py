from craigslist_class import craigslistAPI

cl = craigslistAPI(city="lasvegas",category="fbh")

print(cl.call_craigslist_JOBS())