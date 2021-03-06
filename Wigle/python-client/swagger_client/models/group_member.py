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


class GroupMember(object):
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
        'group_id': 'str',
        'username': 'str',
        'status': 'str',
        'discovered': 'int',
        'total': 'int',
        'gen_disc': 'int',
        'first_transid': 'str',
        'last_transid': 'str',
        'month_count': 'int',
        'prev_month_count': 'int'
    }

    attribute_map = {
        'group_id': 'groupId',
        'username': 'username',
        'status': 'status',
        'discovered': 'discovered',
        'total': 'total',
        'gen_disc': 'genDisc',
        'first_transid': 'firstTransid',
        'last_transid': 'lastTransid',
        'month_count': 'monthCount',
        'prev_month_count': 'prevMonthCount'
    }

    def __init__(self, group_id=None, username=None, status=None, discovered=None, total=None, gen_disc=None, first_transid=None, last_transid=None, month_count=None, prev_month_count=None, _configuration=None):  # noqa: E501
        """GroupMember - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._group_id = None
        self._username = None
        self._status = None
        self._discovered = None
        self._total = None
        self._gen_disc = None
        self._first_transid = None
        self._last_transid = None
        self._month_count = None
        self._prev_month_count = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if username is not None:
            self.username = username
        if status is not None:
            self.status = status
        if discovered is not None:
            self.discovered = discovered
        if total is not None:
            self.total = total
        if gen_disc is not None:
            self.gen_disc = gen_disc
        if first_transid is not None:
            self.first_transid = first_transid
        if last_transid is not None:
            self.last_transid = last_transid
        if month_count is not None:
            self.month_count = month_count
        if prev_month_count is not None:
            self.prev_month_count = prev_month_count

    @property
    def group_id(self):
        """Gets the group_id of this GroupMember.  # noqa: E501


        :return: The group_id of this GroupMember.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this GroupMember.


        :param group_id: The group_id of this GroupMember.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def username(self):
        """Gets the username of this GroupMember.  # noqa: E501


        :return: The username of this GroupMember.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this GroupMember.


        :param username: The username of this GroupMember.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def status(self):
        """Gets the status of this GroupMember.  # noqa: E501


        :return: The status of this GroupMember.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GroupMember.


        :param status: The status of this GroupMember.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def discovered(self):
        """Gets the discovered of this GroupMember.  # noqa: E501


        :return: The discovered of this GroupMember.  # noqa: E501
        :rtype: int
        """
        return self._discovered

    @discovered.setter
    def discovered(self, discovered):
        """Sets the discovered of this GroupMember.


        :param discovered: The discovered of this GroupMember.  # noqa: E501
        :type: int
        """

        self._discovered = discovered

    @property
    def total(self):
        """Gets the total of this GroupMember.  # noqa: E501


        :return: The total of this GroupMember.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this GroupMember.


        :param total: The total of this GroupMember.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def gen_disc(self):
        """Gets the gen_disc of this GroupMember.  # noqa: E501


        :return: The gen_disc of this GroupMember.  # noqa: E501
        :rtype: int
        """
        return self._gen_disc

    @gen_disc.setter
    def gen_disc(self, gen_disc):
        """Sets the gen_disc of this GroupMember.


        :param gen_disc: The gen_disc of this GroupMember.  # noqa: E501
        :type: int
        """

        self._gen_disc = gen_disc

    @property
    def first_transid(self):
        """Gets the first_transid of this GroupMember.  # noqa: E501


        :return: The first_transid of this GroupMember.  # noqa: E501
        :rtype: str
        """
        return self._first_transid

    @first_transid.setter
    def first_transid(self, first_transid):
        """Sets the first_transid of this GroupMember.


        :param first_transid: The first_transid of this GroupMember.  # noqa: E501
        :type: str
        """

        self._first_transid = first_transid

    @property
    def last_transid(self):
        """Gets the last_transid of this GroupMember.  # noqa: E501


        :return: The last_transid of this GroupMember.  # noqa: E501
        :rtype: str
        """
        return self._last_transid

    @last_transid.setter
    def last_transid(self, last_transid):
        """Sets the last_transid of this GroupMember.


        :param last_transid: The last_transid of this GroupMember.  # noqa: E501
        :type: str
        """

        self._last_transid = last_transid

    @property
    def month_count(self):
        """Gets the month_count of this GroupMember.  # noqa: E501


        :return: The month_count of this GroupMember.  # noqa: E501
        :rtype: int
        """
        return self._month_count

    @month_count.setter
    def month_count(self, month_count):
        """Sets the month_count of this GroupMember.


        :param month_count: The month_count of this GroupMember.  # noqa: E501
        :type: int
        """

        self._month_count = month_count

    @property
    def prev_month_count(self):
        """Gets the prev_month_count of this GroupMember.  # noqa: E501


        :return: The prev_month_count of this GroupMember.  # noqa: E501
        :rtype: int
        """
        return self._prev_month_count

    @prev_month_count.setter
    def prev_month_count(self, prev_month_count):
        """Sets the prev_month_count of this GroupMember.


        :param prev_month_count: The prev_month_count of this GroupMember.  # noqa: E501
        :type: int
        """

        self._prev_month_count = prev_month_count

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
        if issubclass(GroupMember, dict):
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
        if not isinstance(other, GroupMember):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupMember):
            return True

        return self.to_dict() != other.to_dict()
