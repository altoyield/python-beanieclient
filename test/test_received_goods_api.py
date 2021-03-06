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
from beanie.api.received_goods_api import ReceivedGoodsApi  # noqa: E501
from beanie.rest import ApiException


class TestReceivedGoodsApi(unittest.TestCase):
    """ReceivedGoodsApi unit test stubs"""

    def setUp(self):
        self.api = beanie.api.received_goods_api.ReceivedGoodsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_received_goods(self):
        """Test case for add_received_goods

        """
        pass

    def test_find_received_goods(self):
        """Test case for find_received_goods

        All received goods  # noqa: E501
        """
        pass

    def test_find_received_goods_by_id(self):
        """Test case for find_received_goods_by_id

        Find Received goods by ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
