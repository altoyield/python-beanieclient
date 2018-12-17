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
from beanie.api.customer_addresses_api import CustomerAddressesApi  # noqa: E501
from beanie.rest import ApiException


class TestCustomerAddressesApi(unittest.TestCase):
    """CustomerAddressesApi unit test stubs"""

    def setUp(self):
        self.api = beanie.api.customer_addresses_api.CustomerAddressesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_customer_address(self):
        """Test case for add_customer_address

        """
        pass

    def test_find_customer_address_by_id(self):
        """Test case for find_customer_address_by_id

        Find Customer address by ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()