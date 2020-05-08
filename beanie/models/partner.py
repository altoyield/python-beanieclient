# coding: utf-8

"""
    Beanie ERP API

    An API specification for interacting with the Beanie ERP system  # noqa: E501

    OpenAPI spec version: 0.8
    Contact: dev@bean.ie
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from beanie.models.partner_input import PartnerInput  # noqa: F401,E501
from beanie.models.partner_note import PartnerNote  # noqa: F401,E501
from beanie.models.payables_ledger import PayablesLedger  # noqa: F401,E501
from beanie.models.receivables_ledger import ReceivablesLedger  # noqa: F401,E501


class Partner(object):
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
        'name': 'str',
        'currency_code': 'str',
        'net_terms': 'int',
        'credit_limit': 'float',
        'partner_vat': 'str',
        'id': 'int',
        'code': 'str',
        'state': 'str',
        'credit_hold': 'bool',
        'balance': 'float',
        'address_ids': 'list[int]',
        'notes': 'list[PartnerNote]',
        'receivables_ledgers': 'list[ReceivablesLedger]',
        'payables_ledgers': 'list[PayablesLedger]'
    }

    attribute_map = {
        'name': 'name',
        'currency_code': 'currency_code',
        'net_terms': 'net_terms',
        'credit_limit': 'credit_limit',
        'partner_vat': 'partner_vat',
        'id': 'id',
        'code': 'code',
        'state': 'state',
        'credit_hold': 'credit_hold',
        'balance': 'balance',
        'address_ids': 'address_ids',
        'notes': 'notes',
        'receivables_ledgers': 'receivables_ledgers',
        'payables_ledgers': 'payables_ledgers'
    }

    def __init__(self, name=None, currency_code=None, net_terms=None, credit_limit=None, partner_vat=None, id=None, code=None, state=None, credit_hold=None, balance=None, address_ids=None, notes=None, receivables_ledgers=None, payables_ledgers=None):  # noqa: E501
        """Partner - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._currency_code = None
        self._net_terms = None
        self._credit_limit = None
        self._partner_vat = None
        self._id = None
        self._code = None
        self._state = None
        self._credit_hold = None
        self._balance = None
        self._address_ids = None
        self._notes = None
        self._receivables_ledgers = None
        self._payables_ledgers = None
        self.discriminator = None

        self.name = name
        self.currency_code = currency_code
        if net_terms is not None:
            self.net_terms = net_terms
        if credit_limit is not None:
            self.credit_limit = credit_limit
        if partner_vat is not None:
            self.partner_vat = partner_vat
        if id is not None:
            self.id = id
        if code is not None:
            self.code = code
        if state is not None:
            self.state = state
        if credit_hold is not None:
            self.credit_hold = credit_hold
        if balance is not None:
            self.balance = balance
        if address_ids is not None:
            self.address_ids = address_ids
        if notes is not None:
            self.notes = notes
        if receivables_ledgers is not None:
            self.receivables_ledgers = receivables_ledgers
        if payables_ledgers is not None:
            self.payables_ledgers = payables_ledgers

    @property
    def name(self):
        """Gets the name of this Partner.  # noqa: E501


        :return: The name of this Partner.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Partner.


        :param name: The name of this Partner.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def currency_code(self):
        """Gets the currency_code of this Partner.  # noqa: E501


        :return: The currency_code of this Partner.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this Partner.


        :param currency_code: The currency_code of this Partner.  # noqa: E501
        :type: str
        """
        if currency_code is None:
            raise ValueError("Invalid value for `currency_code`, must not be `None`")  # noqa: E501

        self._currency_code = currency_code

    @property
    def net_terms(self):
        """Gets the net_terms of this Partner.  # noqa: E501


        :return: The net_terms of this Partner.  # noqa: E501
        :rtype: int
        """
        return self._net_terms

    @net_terms.setter
    def net_terms(self, net_terms):
        """Sets the net_terms of this Partner.


        :param net_terms: The net_terms of this Partner.  # noqa: E501
        :type: int
        """

        self._net_terms = net_terms

    @property
    def credit_limit(self):
        """Gets the credit_limit of this Partner.  # noqa: E501


        :return: The credit_limit of this Partner.  # noqa: E501
        :rtype: float
        """
        return self._credit_limit

    @credit_limit.setter
    def credit_limit(self, credit_limit):
        """Sets the credit_limit of this Partner.


        :param credit_limit: The credit_limit of this Partner.  # noqa: E501
        :type: float
        """

        self._credit_limit = credit_limit

    @property
    def partner_vat(self):
        """Gets the partner_vat of this Partner.  # noqa: E501


        :return: The partner_vat of this Partner.  # noqa: E501
        :rtype: str
        """
        return self._partner_vat

    @partner_vat.setter
    def partner_vat(self, partner_vat):
        """Sets the partner_vat of this Partner.


        :param partner_vat: The partner_vat of this Partner.  # noqa: E501
        :type: str
        """

        self._partner_vat = partner_vat

    @property
    def id(self):
        """Gets the id of this Partner.  # noqa: E501


        :return: The id of this Partner.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Partner.


        :param id: The id of this Partner.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def code(self):
        """Gets the code of this Partner.  # noqa: E501


        :return: The code of this Partner.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Partner.


        :param code: The code of this Partner.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def state(self):
        """Gets the state of this Partner.  # noqa: E501


        :return: The state of this Partner.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Partner.


        :param state: The state of this Partner.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def credit_hold(self):
        """Gets the credit_hold of this Partner.  # noqa: E501


        :return: The credit_hold of this Partner.  # noqa: E501
        :rtype: bool
        """
        return self._credit_hold

    @credit_hold.setter
    def credit_hold(self, credit_hold):
        """Sets the credit_hold of this Partner.


        :param credit_hold: The credit_hold of this Partner.  # noqa: E501
        :type: bool
        """

        self._credit_hold = credit_hold

    @property
    def balance(self):
        """Gets the balance of this Partner.  # noqa: E501


        :return: The balance of this Partner.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this Partner.


        :param balance: The balance of this Partner.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def address_ids(self):
        """Gets the address_ids of this Partner.  # noqa: E501


        :return: The address_ids of this Partner.  # noqa: E501
        :rtype: list[int]
        """
        return self._address_ids

    @address_ids.setter
    def address_ids(self, address_ids):
        """Sets the address_ids of this Partner.


        :param address_ids: The address_ids of this Partner.  # noqa: E501
        :type: list[int]
        """

        self._address_ids = address_ids

    @property
    def notes(self):
        """Gets the notes of this Partner.  # noqa: E501


        :return: The notes of this Partner.  # noqa: E501
        :rtype: list[PartnerNote]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Partner.


        :param notes: The notes of this Partner.  # noqa: E501
        :type: list[PartnerNote]
        """

        self._notes = notes

    @property
    def receivables_ledgers(self):
        """Gets the receivables_ledgers of this Partner.  # noqa: E501


        :return: The receivables_ledgers of this Partner.  # noqa: E501
        :rtype: list[ReceivablesLedger]
        """
        return self._receivables_ledgers

    @receivables_ledgers.setter
    def receivables_ledgers(self, receivables_ledgers):
        """Sets the receivables_ledgers of this Partner.


        :param receivables_ledgers: The receivables_ledgers of this Partner.  # noqa: E501
        :type: list[ReceivablesLedger]
        """

        self._receivables_ledgers = receivables_ledgers

    @property
    def payables_ledgers(self):
        """Gets the payables_ledgers of this Partner.  # noqa: E501


        :return: The payables_ledgers of this Partner.  # noqa: E501
        :rtype: list[PayablesLedger]
        """
        return self._payables_ledgers

    @payables_ledgers.setter
    def payables_ledgers(self, payables_ledgers):
        """Sets the payables_ledgers of this Partner.


        :param payables_ledgers: The payables_ledgers of this Partner.  # noqa: E501
        :type: list[PayablesLedger]
        """

        self._payables_ledgers = payables_ledgers

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
        if not isinstance(other, Partner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
