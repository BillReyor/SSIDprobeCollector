# coding: utf-8

"""
    WiGLE API

    Search, upload, and integrate statistics from WiGLE. Use API Name+Token from https://wigle.net/account  # noqa: E501

    OpenAPI spec version: 3.1
    Contact: WiGLE-admin@wigle.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class GroupResponse(object):
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
        'success': 'bool',
        'groupid': 'str',
        'group': 'Group',
        'users': 'list[GroupMember]'
    }

    attribute_map = {
        'success': 'success',
        'groupid': 'groupid',
        'group': 'group',
        'users': 'users'
    }

    def __init__(self, success=None, groupid=None, group=None, users=None, _configuration=None):  # noqa: E501
        """GroupResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._success = None
        self._groupid = None
        self._group = None
        self._users = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if groupid is not None:
            self.groupid = groupid
        if group is not None:
            self.group = group
        if users is not None:
            self.users = users

    @property
    def success(self):
        """Gets the success of this GroupResponse.  # noqa: E501


        :return: The success of this GroupResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this GroupResponse.


        :param success: The success of this GroupResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def groupid(self):
        """Gets the groupid of this GroupResponse.  # noqa: E501


        :return: The groupid of this GroupResponse.  # noqa: E501
        :rtype: str
        """
        return self._groupid

    @groupid.setter
    def groupid(self, groupid):
        """Sets the groupid of this GroupResponse.


        :param groupid: The groupid of this GroupResponse.  # noqa: E501
        :type: str
        """

        self._groupid = groupid

    @property
    def group(self):
        """Gets the group of this GroupResponse.  # noqa: E501


        :return: The group of this GroupResponse.  # noqa: E501
        :rtype: Group
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this GroupResponse.


        :param group: The group of this GroupResponse.  # noqa: E501
        :type: Group
        """

        self._group = group

    @property
    def users(self):
        """Gets the users of this GroupResponse.  # noqa: E501


        :return: The users of this GroupResponse.  # noqa: E501
        :rtype: list[GroupMember]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this GroupResponse.


        :param users: The users of this GroupResponse.  # noqa: E501
        :type: list[GroupMember]
        """

        self._users = users

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
        if issubclass(GroupResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GroupResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupResponse):
            return True

        return self.to_dict() != other.to_dict()
