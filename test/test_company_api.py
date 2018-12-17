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
from beanie.api.company_api import CompanyApi  # noqa: E501
from beanie.rest import ApiException


class TestCompanyApi(unittest.TestCase):
    """CompanyApi unit test stubs"""

    def setUp(self):
        self.api = beanie.api.company_api.CompanyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_find_company_by_id(self):
        """Test case for find_company_by_id

        Find Company details by ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
