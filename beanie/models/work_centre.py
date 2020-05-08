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


class WorkCentre(object):
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
        'id': 'int',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'name': 'str',
        'description': 'str',
        'work_centre_group_id': 'int',
        'location': 'str',
        'state': 'int',
        'production_order_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'name': 'name',
        'description': 'description',
        'work_centre_group_id': 'work_centre_group_id',
        'location': 'location',
        'state': 'state',
        'production_order_id': 'production_order_id'
    }

    def __init__(self, id=None, created_at=None, updated_at=None, name=None, description=None, work_centre_group_id=None, location=None, state=None, production_order_id=None):  # noqa: E501
        """WorkCentre - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._created_at = None
        self._updated_at = None
        self._name = None
        self._description = None
        self._work_centre_group_id = None
        self._location = None
        self._state = None
        self._production_order_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if work_centre_group_id is not None:
            self.work_centre_group_id = work_centre_group_id
        if location is not None:
            self.location = location
        if state is not None:
            self.state = state
        if production_order_id is not None:
            self.production_order_id = production_order_id

    @property
    def id(self):
        """Gets the id of this WorkCentre.  # noqa: E501


        :return: The id of this WorkCentre.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkCentre.


        :param id: The id of this WorkCentre.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this WorkCentre.  # noqa: E501


        :return: The created_at of this WorkCentre.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this WorkCentre.


        :param created_at: The created_at of this WorkCentre.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this WorkCentre.  # noqa: E501


        :return: The updated_at of this WorkCentre.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this WorkCentre.


        :param updated_at: The updated_at of this WorkCentre.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def name(self):
        """Gets the name of this WorkCentre.  # noqa: E501


        :return: The name of this WorkCentre.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkCentre.


        :param name: The name of this WorkCentre.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this WorkCentre.  # noqa: E501


        :return: The description of this WorkCentre.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WorkCentre.


        :param description: The description of this WorkCentre.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def work_centre_group_id(self):
        """Gets the work_centre_group_id of this WorkCentre.  # noqa: E501


        :return: The work_centre_group_id of this WorkCentre.  # noqa: E501
        :rtype: int
        """
        return self._work_centre_group_id

    @work_centre_group_id.setter
    def work_centre_group_id(self, work_centre_group_id):
        """Sets the work_centre_group_id of this WorkCentre.


        :param work_centre_group_id: The work_centre_group_id of this WorkCentre.  # noqa: E501
        :type: int
        """

        self._work_centre_group_id = work_centre_group_id

    @property
    def location(self):
        """Gets the location of this WorkCentre.  # noqa: E501


        :return: The location of this WorkCentre.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this WorkCentre.


        :param location: The location of this WorkCentre.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def state(self):
        """Gets the state of this WorkCentre.  # noqa: E501


        :return: The state of this WorkCentre.  # noqa: E501
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this WorkCentre.


        :param state: The state of this WorkCentre.  # noqa: E501
        :type: int
        """

        self._state = state

    @property
    def production_order_id(self):
        """Gets the production_order_id of this WorkCentre.  # noqa: E501


        :return: The production_order_id of this WorkCentre.  # noqa: E501
        :rtype: int
        """
        return self._production_order_id

    @production_order_id.setter
    def production_order_id(self, production_order_id):
        """Sets the production_order_id of this WorkCentre.


        :param production_order_id: The production_order_id of this WorkCentre.  # noqa: E501
        :type: int
        """

        self._production_order_id = production_order_id

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
        if not isinstance(other, WorkCentre):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
