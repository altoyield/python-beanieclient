# coding: utf-8

"""
    Beanie ERP API

    An API specification for interacting with the Beanie ERP system  # noqa: E501

    OpenAPI spec version: 0.2
    Contact: dev@bean.ie
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import beanie
from beanie.api.customer_api import CustomerApi  # noqa: E501
from beanie.rest import ApiException


class TestCustomerApi(unittest.TestCase):
    """CustomerApi unit test stubs"""

    def setUp(self):
        self.api = beanie.api.customer_api.CustomerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_find_customers(self):
        """Test case for find_customers

        All customer  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
