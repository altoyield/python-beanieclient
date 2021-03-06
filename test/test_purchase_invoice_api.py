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
from beanie.api.purchase_invoice_api import PurchaseInvoiceApi  # noqa: E501
from beanie.rest import ApiException


class TestPurchaseInvoiceApi(unittest.TestCase):
    """PurchaseInvoiceApi unit test stubs"""

    def setUp(self):
        self.api = beanie.api.purchase_invoice_api.PurchaseInvoiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_purchase_invoice(self):
        """Test case for add_purchase_invoice

        """
        pass

    def test_find_purchase_invoice_by_id(self):
        """Test case for find_purchase_invoice_by_id

        Find Purchase invoice by ID  # noqa: E501
        """
        pass

    def test_find_purchase_invoices(self):
        """Test case for find_purchase_invoices

        All purchase invoice  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
