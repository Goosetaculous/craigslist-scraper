# Class - Craigslist API
# Goose 2017
from craigslist import CraigslistJobs

class craigslistAPI(object):


    def __init__(self,**kwargs):
        """
        Constructor
        :param kwargs:
        """
        self.city = kwargs['city']
        self.category = kwargs['category']


    def call_craigslist_JOBS(self):
        """
        Call the craigslist API with the city and category given
        by the constructor
        :return:
        """
        cl = CraigslistJobs(site=self.city, category=self.category)
        results =cl.get_results(sort_by='newest', geotagged=False, limit=500)
        return results



    def get_results(self,results):
        """
        Test Method to see the result of the craigslist API
        :param results:
        :return: Print the result
        """
        for result in results:
            print result


if __name__ == "__main__":
    """
    This is a test run for this class.
    Args:
        param1: City.
        param2: Job site parameter from the URL.
    Returns:
        Run the methods from the class.
    Raises:
        KeyError: Raises an exception.
    """
    test =craigslistAPI(city='sandiego' , category='fbh')
    test.get_results( test.call_craigslist_JOBS() )
