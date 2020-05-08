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


class PartnerNote(object):
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
        '_date': 'datetime',
        'author': 'str',
        'note': 'str'
    }

    attribute_map = {
        '_date': 'date',
        'author': 'author',
        'note': 'note'
    }

    def __init__(self, _date=None, author=None, note=None):  # noqa: E501
        """PartnerNote - a model defined in Swagger"""  # noqa: E501

        self.__date = None
        self._author = None
        self._note = None
        self.discriminator = None

        self._date = _date
        self.author = author
        self.note = note

    @property
    def _date(self):
        """Gets the _date of this PartnerNote.  # noqa: E501


        :return: The _date of this PartnerNote.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this PartnerNote.


        :param _date: The _date of this PartnerNote.  # noqa: E501
        :type: datetime
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def author(self):
        """Gets the author of this PartnerNote.  # noqa: E501


        :return: The author of this PartnerNote.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this PartnerNote.


        :param author: The author of this PartnerNote.  # noqa: E501
        :type: str
        """
        if author is None:
            raise ValueError("Invalid value for `author`, must not be `None`")  # noqa: E501

        self._author = author

    @property
    def note(self):
        """Gets the note of this PartnerNote.  # noqa: E501


        :return: The note of this PartnerNote.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this PartnerNote.


        :param note: The note of this PartnerNote.  # noqa: E501
        :type: str
        """
        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")  # noqa: E501

        self._note = note

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
        if not isinstance(other, PartnerNote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
