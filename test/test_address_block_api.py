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
from beanie.api.address_block_api import AddressBlockApi  # noqa: E501
from beanie.rest import ApiException


class TestAddressBlockApi(unittest.TestCase):
    """AddressBlockApi unit test stubs"""

    def setUp(self):
        self.api = beanie.api.address_block_api.AddressBlockApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_address_block(self):
        """Test case for add_address_block

        """
        pass

    def test_find_address_block_by_id(self):
        """Test case for find_address_block_by_id

        Find Address block by ID  # noqa: E501
        """
        pass

    def test_find_address_blocks(self):
        """Test case for find_address_blocks

        All address block  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
