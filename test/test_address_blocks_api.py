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
from beanie.api.address_blocks_api import AddressBlocksApi  # noqa: E501
from beanie.rest import ApiException


class TestAddressBlocksApi(unittest.TestCase):
    """AddressBlocksApi unit test stubs"""

    def setUp(self):
        self.api = beanie.api.address_blocks_api.AddressBlocksApi()  # noqa: E501

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


if __name__ == '__main__':
    unittest.main()
