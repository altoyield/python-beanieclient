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
from beanie.api.delivery_note_api import DeliveryNoteApi  # noqa: E501
from beanie.rest import ApiException


class TestDeliveryNoteApi(unittest.TestCase):
    """DeliveryNoteApi unit test stubs"""

    def setUp(self):
        self.api = beanie.api.delivery_note_api.DeliveryNoteApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_delivery_note(self):
        """Test case for add_delivery_note

        """
        pass

    def test_find_delivery_note_by_id(self):
        """Test case for find_delivery_note_by_id

        Find Delivery note by ID  # noqa: E501
        """
        pass

    def test_find_delivery_notes(self):
        """Test case for find_delivery_notes

        All delivery note  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
