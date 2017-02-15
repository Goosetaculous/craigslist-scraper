# Class - Craigslist API
# Goose 2017
from craigslist import CraigslistJobs

class craigslistAPI(object):

    # Constructor
    # Initialize the city and the category
    def __init__(self,**kwargs):
        self.city = kwargs['city']
        self.category = kwargs['category']

    # Call the API and
    # Return: results
    def call_craigslist_JOBS(self):
        cl = CraigslistJobs(site=self.city, category=self.category)
        results =cl.get_results(sort_by='newest', geotagged=False, limit=30)
        return results

    # Traverse the results
    # TEST FUNCTION
    # Return : Dictionary of each Ad
    def get_results(self,results):
        for result in results:
            print result


if __name__ == "__main__":
    test =craigslistAPI(city='lasvegas',category='fbh')
    test.get_results( test.call_craigslist_JOBS() )


