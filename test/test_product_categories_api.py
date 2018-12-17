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
from beanie.api.product_categories_api import ProductCategoriesApi  # noqa: E501
from beanie.rest import ApiException


class TestProductCategoriesApi(unittest.TestCase):
    """ProductCategoriesApi unit test stubs"""

    def setUp(self):
        self.api = beanie.api.product_categories_api.ProductCategoriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_product_category(self):
        """Test case for add_product_category

        """
        pass

    def test_find_product_category_by_id(self):
        """Test case for find_product_category_by_id

        Find Product category by ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()