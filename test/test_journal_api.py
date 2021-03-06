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
from beanie.api.journal_api import JournalApi  # noqa: E501
from beanie.rest import ApiException


class TestJournalApi(unittest.TestCase):
    """JournalApi unit test stubs"""

    def setUp(self):
        self.api = beanie.api.journal_api.JournalApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_journal(self):
        """Test case for add_journal

        """
        pass

    def test_find_journal_by_id(self):
        """Test case for find_journal_by_id

        Find Journal by ID  # noqa: E501
        """
        pass

    def test_find_journals(self):
        """Test case for find_journals

        All journal  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
