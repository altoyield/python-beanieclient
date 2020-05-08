# coding: utf-8

"""
    Beanie ERP API

    An API specification for interacting with the Beanie ERP system  # noqa: E501

    OpenAPI spec version: 0.2
    Contact: dev@bean.ie
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PayablesLedger(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        '_date': 'date',
        'ledger_type': 'str',
        'narrative': 'str',
        'amount': 'float',
        'reconciled': 'bool',
        'journal_id': 'int',
        'sales_invoice_id': 'int'
    }

    attribute_map = {
        '_date': 'date',
        'ledger_type': 'ledger_type',
        'narrative': 'narrative',
        'amount': 'amount',
        'reconciled': 'reconciled',
        'journal_id': 'journal_id',
        'sales_invoice_id': 'sales_invoice_id'
    }

    def __init__(self, _date=None, ledger_type=None, narrative=None, amount=None, reconciled=None, journal_id=None, sales_invoice_id=None):  # noqa: E501
        """PayablesLedger - a model defined in Swagger"""  # noqa: E501

        self.__date = None
        self._ledger_type = None
        self._narrative = None
        self._amount = None
        self._reconciled = None
        self._journal_id = None
        self._sales_invoice_id = None
        self.discriminator = None

        self._date = _date
        self.ledger_type = ledger_type
        self.narrative = narrative
        self.amount = amount
        self.reconciled = reconciled
        if journal_id is not None:
            self.journal_id = journal_id
        if sales_invoice_id is not None:
            self.sales_invoice_id = sales_invoice_id

    @property
    def _date(self):
        """Gets the _date of this PayablesLedger.  # noqa: E501


        :return: The _date of this PayablesLedger.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this PayablesLedger.


        :param _date: The _date of this PayablesLedger.  # noqa: E501
        :type: date
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def ledger_type(self):
        """Gets the ledger_type of this PayablesLedger.  # noqa: E501


        :return: The ledger_type of this PayablesLedger.  # noqa: E501
        :rtype: str
        """
        return self._ledger_type

    @ledger_type.setter
    def ledger_type(self, ledger_type):
        """Sets the ledger_type of this PayablesLedger.


        :param ledger_type: The ledger_type of this PayablesLedger.  # noqa: E501
        :type: str
        """
        if ledger_type is None:
            raise ValueError("Invalid value for `ledger_type`, must not be `None`")  # noqa: E501

        self._ledger_type = ledger_type

    @property
    def narrative(self):
        """Gets the narrative of this PayablesLedger.  # noqa: E501


        :return: The narrative of this PayablesLedger.  # noqa: E501
        :rtype: str
        """
        return self._narrative

    @narrative.setter
    def narrative(self, narrative):
        """Sets the narrative of this PayablesLedger.


        :param narrative: The narrative of this PayablesLedger.  # noqa: E501
        :type: str
        """
        if narrative is None:
            raise ValueError("Invalid value for `narrative`, must not be `None`")  # noqa: E501

        self._narrative = narrative

    @property
    def amount(self):
        """Gets the amount of this PayablesLedger.  # noqa: E501


        :return: The amount of this PayablesLedger.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PayablesLedger.


        :param amount: The amount of this PayablesLedger.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def reconciled(self):
        """Gets the reconciled of this PayablesLedger.  # noqa: E501


        :return: The reconciled of this PayablesLedger.  # noqa: E501
        :rtype: bool
        """
        return self._reconciled

    @reconciled.setter
    def reconciled(self, reconciled):
        """Sets the reconciled of this PayablesLedger.


        :param reconciled: The reconciled of this PayablesLedger.  # noqa: E501
        :type: bool
        """
        if reconciled is None:
            raise ValueError("Invalid value for `reconciled`, must not be `None`")  # noqa: E501

        self._reconciled = reconciled

    @property
    def journal_id(self):
        """Gets the journal_id of this PayablesLedger.  # noqa: E501


        :return: The journal_id of this PayablesLedger.  # noqa: E501
        :rtype: int
        """
        return self._journal_id

    @journal_id.setter
    def journal_id(self, journal_id):
        """Sets the journal_id of this PayablesLedger.


        :param journal_id: The journal_id of this PayablesLedger.  # noqa: E501
        :type: int
        """

        self._journal_id = journal_id

    @property
    def sales_invoice_id(self):
        """Gets the sales_invoice_id of this PayablesLedger.  # noqa: E501


        :return: The sales_invoice_id of this PayablesLedger.  # noqa: E501
        :rtype: int
        """
        return self._sales_invoice_id

    @sales_invoice_id.setter
    def sales_invoice_id(self, sales_invoice_id):
        """Sets the sales_invoice_id of this PayablesLedger.


        :param sales_invoice_id: The sales_invoice_id of this PayablesLedger.  # noqa: E501
        :type: int
        """

        self._sales_invoice_id = sales_invoice_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PayablesLedger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
