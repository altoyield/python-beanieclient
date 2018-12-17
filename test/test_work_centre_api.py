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
from beanie.api.work_centre_api import WorkCentreApi  # noqa: E501
from beanie.rest import ApiException


class TestWorkCentreApi(unittest.TestCase):
    """WorkCentreApi unit test stubs"""

    def setUp(self):
        self.api = beanie.api.work_centre_api.WorkCentreApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_work_centre(self):
        """Test case for add_work_centre

        """
        pass

    def test_find_work_centre_by_id(self):
        """Test case for find_work_centre_by_id

        Find Work centre by ID  # noqa: E501
        """
        pass

    def test_find_work_centres(self):
        """Test case for find_work_centres

        All work centre  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
