import unittest
from connect import SalesForceQuery

class TestSalesForceQuery(unittest.TestCase):
    def __init__(self, grant_type):
        self.sf = SalesForceOAuth('password')

    def test_salesforce_query(self):
        pass




if __name__ == '__main__':
    unittest.main()
