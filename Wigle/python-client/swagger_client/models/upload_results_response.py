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


class UploadResultsResponse(object):
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
        'time_taken': 'str',
        'filesize': 'int',
        'filename': 'str',
        'transids': 'list[TransidResponse]'
    }

    attribute_map = {
        'time_taken': 'timeTaken',
        'filesize': 'filesize',
        'filename': 'filename',
        'transids': 'transids'
    }

    def __init__(self, time_taken=None, filesize=None, filename=None, transids=None, _configuration=None):  # noqa: E501
        """UploadResultsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._time_taken = None
        self._filesize = None
        self._filename = None
        self._transids = None
        self.discriminator = None

        if time_taken is not None:
            self.time_taken = time_taken
        if filesize is not None:
            self.filesize = filesize
        if filename is not None:
            self.filename = filename
        if transids is not None:
            self.transids = transids

    @property
    def time_taken(self):
        """Gets the time_taken of this UploadResultsResponse.  # noqa: E501


        :return: The time_taken of this UploadResultsResponse.  # noqa: E501
        :rtype: str
        """
        return self._time_taken

    @time_taken.setter
    def time_taken(self, time_taken):
        """Sets the time_taken of this UploadResultsResponse.


        :param time_taken: The time_taken of this UploadResultsResponse.  # noqa: E501
        :type: str
        """

        self._time_taken = time_taken

    @property
    def filesize(self):
        """Gets the filesize of this UploadResultsResponse.  # noqa: E501


        :return: The filesize of this UploadResultsResponse.  # noqa: E501
        :rtype: int
        """
        return self._filesize

    @filesize.setter
    def filesize(self, filesize):
        """Sets the filesize of this UploadResultsResponse.


        :param filesize: The filesize of this UploadResultsResponse.  # noqa: E501
        :type: int
        """

        self._filesize = filesize

    @property
    def filename(self):
        """Gets the filename of this UploadResultsResponse.  # noqa: E501


        :return: The filename of this UploadResultsResponse.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this UploadResultsResponse.


        :param filename: The filename of this UploadResultsResponse.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def transids(self):
        """Gets the transids of this UploadResultsResponse.  # noqa: E501


        :return: The transids of this UploadResultsResponse.  # noqa: E501
        :rtype: list[TransidResponse]
        """
        return self._transids

    @transids.setter
    def transids(self, transids):
        """Sets the transids of this UploadResultsResponse.


        :param transids: The transids of this UploadResultsResponse.  # noqa: E501
        :type: list[TransidResponse]
        """

        self._transids = transids

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
        if issubclass(UploadResultsResponse, dict):
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
        if not isinstance(other, UploadResultsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UploadResultsResponse):
            return True

        return self.to_dict() != other.to_dict()
