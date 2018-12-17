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
from beanie.api.product_api import ProductApi  # noqa: E501
from beanie.rest import ApiException


class TestProductApi(unittest.TestCase):
    """ProductApi unit test stubs"""

    def setUp(self):
        self.api = beanie.api.product_api.ProductApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_product(self):
        """Test case for add_product

        """
        pass

    def test_find_product_by_id(self):
        """Test case for find_product_by_id

        Find Product by ID  # noqa: E501
        """
        pass

    def test_find_products(self):
        """Test case for find_products

        All product  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
