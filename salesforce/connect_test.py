import unittest
from connect import SalesForceOAuth

class TestSalesForceOAuth(unittest.TestCase):
    def __init__(self, grant_type):
        self.sf = SalesForceOAuth('password')

    def test_salesforce_values(self):
        pass




if __name__ == '__main__':
    unittest.main()
