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
from beanie.api.stock_supplier_api import StockSupplierApi  # noqa: E501
from beanie.rest import ApiException


class TestStockSupplierApi(unittest.TestCase):
    """StockSupplierApi unit test stubs"""

    def setUp(self):
        self.api = beanie.api.stock_supplier_api.StockSupplierApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_stock_supplier(self):
        """Test case for add_stock_supplier

        """
        pass

    def test_find_stock_supplier_by_id(self):
        """Test case for find_stock_supplier_by_id

        Find Stock supplier by ID  # noqa: E501
        """
        pass

    def test_find_stock_suppliers(self):
        """Test case for find_stock_suppliers

        All stock supplier  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
