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


class BankAccountInput(object):
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
        'bank_name': 'str',
        'currency_code': 'str',
        'swift': 'str',
        'iban': 'str',
        'address1': 'str',
        'address2': 'str',
        'address3': 'str',
        'city': 'str',
        'state_county': 'str',
        'zip_postcode': 'str',
        'country_name': 'str',
        'contact_name': 'str',
        'phone': 'str',
        'email': 'str',
        'website': 'str'
    }

    attribute_map = {
        'name': 'name',
        'bank_name': 'bank_name',
        'currency_code': 'currency_code',
        'swift': 'swift',
        'iban': 'iban',
        'address1': 'address1',
        'address2': 'address2',
        'address3': 'address3',
        'city': 'city',
        'state_county': 'state_county',
        'zip_postcode': 'zip_postcode',
        'country_name': 'country_name',
        'contact_name': 'contact_name',
        'phone': 'phone',
        'email': 'email',
        'website': 'website'
    }

    def __init__(self, name=None, bank_name=None, currency_code=None, swift=None, iban=None, address1=None, address2=None, address3=None, city=None, state_county=None, zip_postcode=None, country_name=None, contact_name=None, phone=None, email=None, website=None):  # noqa: E501
        """BankAccountInput - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._bank_name = None
        self._currency_code = None
        self._swift = None
        self._iban = None
        self._address1 = None
        self._address2 = None
        self._address3 = None
        self._city = None
        self._state_county = None
        self._zip_postcode = None
        self._country_name = None
        self._contact_name = None
        self._phone = None
        self._email = None
        self._website = None
        self.discriminator = None

        self.name = name
        self.bank_name = bank_name
        self.currency_code = currency_code
        self.swift = swift
        self.iban = iban
        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if address3 is not None:
            self.address3 = address3
        if city is not None:
            self.city = city
        if state_county is not None:
            self.state_county = state_county
        if zip_postcode is not None:
            self.zip_postcode = zip_postcode
        self.country_name = country_name
        if contact_name is not None:
            self.contact_name = contact_name
        if phone is not None:
            self.phone = phone
        if email is not None:
            self.email = email
        if website is not None:
            self.website = website

    @property
    def name(self):
        """Gets the name of this BankAccountInput.  # noqa: E501


        :return: The name of this BankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BankAccountInput.


        :param name: The name of this BankAccountInput.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def bank_name(self):
        """Gets the bank_name of this BankAccountInput.  # noqa: E501


        :return: The bank_name of this BankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._bank_name

    @bank_name.setter
    def bank_name(self, bank_name):
        """Sets the bank_name of this BankAccountInput.


        :param bank_name: The bank_name of this BankAccountInput.  # noqa: E501
        :type: str
        """
        if bank_name is None:
            raise ValueError("Invalid value for `bank_name`, must not be `None`")  # noqa: E501

        self._bank_name = bank_name

    @property
    def currency_code(self):
        """Gets the currency_code of this BankAccountInput.  # noqa: E501


        :return: The currency_code of this BankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this BankAccountInput.


        :param currency_code: The currency_code of this BankAccountInput.  # noqa: E501
        :type: str
        """
        if currency_code is None:
            raise ValueError("Invalid value for `currency_code`, must not be `None`")  # noqa: E501

        self._currency_code = currency_code

    @property
    def swift(self):
        """Gets the swift of this BankAccountInput.  # noqa: E501


        :return: The swift of this BankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._swift

    @swift.setter
    def swift(self, swift):
        """Sets the swift of this BankAccountInput.


        :param swift: The swift of this BankAccountInput.  # noqa: E501
        :type: str
        """
        if swift is None:
            raise ValueError("Invalid value for `swift`, must not be `None`")  # noqa: E501

        self._swift = swift

    @property
    def iban(self):
        """Gets the iban of this BankAccountInput.  # noqa: E501


        :return: The iban of this BankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this BankAccountInput.


        :param iban: The iban of this BankAccountInput.  # noqa: E501
        :type: str
        """
        if iban is None:
            raise ValueError("Invalid value for `iban`, must not be `None`")  # noqa: E501

        self._iban = iban

    @property
    def address1(self):
        """Gets the address1 of this BankAccountInput.  # noqa: E501


        :return: The address1 of this BankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this BankAccountInput.


        :param address1: The address1 of this BankAccountInput.  # noqa: E501
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this BankAccountInput.  # noqa: E501


        :return: The address2 of this BankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this BankAccountInput.


        :param address2: The address2 of this BankAccountInput.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def address3(self):
        """Gets the address3 of this BankAccountInput.  # noqa: E501


        :return: The address3 of this BankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._address3

    @address3.setter
    def address3(self, address3):
        """Sets the address3 of this BankAccountInput.


        :param address3: The address3 of this BankAccountInput.  # noqa: E501
        :type: str
        """

        self._address3 = address3

    @property
    def city(self):
        """Gets the city of this BankAccountInput.  # noqa: E501


        :return: The city of this BankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this BankAccountInput.


        :param city: The city of this BankAccountInput.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state_county(self):
        """Gets the state_county of this BankAccountInput.  # noqa: E501


        :return: The state_county of this BankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._state_county

    @state_county.setter
    def state_county(self, state_county):
        """Sets the state_county of this BankAccountInput.


        :param state_county: The state_county of this BankAccountInput.  # noqa: E501
        :type: str
        """

        self._state_county = state_county

    @property
    def zip_postcode(self):
        """Gets the zip_postcode of this BankAccountInput.  # noqa: E501


        :return: The zip_postcode of this BankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._zip_postcode

    @zip_postcode.setter
    def zip_postcode(self, zip_postcode):
        """Sets the zip_postcode of this BankAccountInput.


        :param zip_postcode: The zip_postcode of this BankAccountInput.  # noqa: E501
        :type: str
        """

        self._zip_postcode = zip_postcode

    @property
    def country_name(self):
        """Gets the country_name of this BankAccountInput.  # noqa: E501


        :return: The country_name of this BankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        """Sets the country_name of this BankAccountInput.


        :param country_name: The country_name of this BankAccountInput.  # noqa: E501
        :type: str
        """
        if country_name is None:
            raise ValueError("Invalid value for `country_name`, must not be `None`")  # noqa: E501

        self._country_name = country_name

    @property
    def contact_name(self):
        """Gets the contact_name of this BankAccountInput.  # noqa: E501


        :return: The contact_name of this BankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this BankAccountInput.


        :param contact_name: The contact_name of this BankAccountInput.  # noqa: E501
        :type: str
        """

        self._contact_name = contact_name

    @property
    def phone(self):
        """Gets the phone of this BankAccountInput.  # noqa: E501


        :return: The phone of this BankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this BankAccountInput.


        :param phone: The phone of this BankAccountInput.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def email(self):
        """Gets the email of this BankAccountInput.  # noqa: E501


        :return: The email of this BankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this BankAccountInput.


        :param email: The email of this BankAccountInput.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def website(self):
        """Gets the website of this BankAccountInput.  # noqa: E501


        :return: The website of this BankAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this BankAccountInput.


        :param website: The website of this BankAccountInput.  # noqa: E501
        :type: str
        """

        self._website = website

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
        if not isinstance(other, BankAccountInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
