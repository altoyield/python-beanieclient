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
from beanie.api.beanie_task_api import BeanieTaskApi  # noqa: E501
from beanie.rest import ApiException


class TestBeanieTaskApi(unittest.TestCase):
    """BeanieTaskApi unit test stubs"""

    def setUp(self):
        self.api = beanie.api.beanie_task_api.BeanieTaskApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_find_beanie_tasks(self):
        """Test case for find_beanie_tasks

        All beanie task  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()