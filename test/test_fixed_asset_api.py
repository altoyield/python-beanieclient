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
from beanie.api.fixed_asset_api import FixedAssetApi  # noqa: E501
from beanie.rest import ApiException


class TestFixedAssetApi(unittest.TestCase):
    """FixedAssetApi unit test stubs"""

    def setUp(self):
        self.api = beanie.api.fixed_asset_api.FixedAssetApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_fixed_asset(self):
        """Test case for add_fixed_asset

        """
        pass

    def test_find_fixed_asset_by_id(self):
        """Test case for find_fixed_asset_by_id

        Find Fixed asset by ID  # noqa: E501
        """
        pass

    def test_find_fixed_assets(self):
        """Test case for find_fixed_assets

        All fixed asset  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
