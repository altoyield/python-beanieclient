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
from beanie.api.nominal_account_categories_api import NominalAccountCategoriesApi  # noqa: E501
from beanie.rest import ApiException


class TestNominalAccountCategoriesApi(unittest.TestCase):
    """NominalAccountCategoriesApi unit test stubs"""

    def setUp(self):
        self.api = beanie.api.nominal_account_categories_api.NominalAccountCategoriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_nominal_account_category(self):
        """Test case for add_nominal_account_category

        """
        pass

    def test_find_nominal_account_category_by_id(self):
        """Test case for find_nominal_account_category_by_id

        Find Nominal account category by ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
