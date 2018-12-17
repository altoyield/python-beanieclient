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
from beanie.api.product_price_api import ProductPriceApi  # noqa: E501
from beanie.rest import ApiException


class TestProductPriceApi(unittest.TestCase):
    """ProductPriceApi unit test stubs"""

    def setUp(self):
        self.api = beanie.api.product_price_api.ProductPriceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_product_price(self):
        """Test case for add_product_price

        """
        pass

    def test_find_product_price_by_id(self):
        """Test case for find_product_price_by_id

        Find Product price by ID  # noqa: E501
        """
        pass

    def test_find_product_prices(self):
        """Test case for find_product_prices

        All product price  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
