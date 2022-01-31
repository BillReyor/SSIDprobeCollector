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


class WiFiLocationCluster(object):
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
        'centroid_latitude': 'float',
        'centroid_longitude': 'float',
        'min_last_update': 'datetime',
        'max_last_update': 'datetime',
        'cluster_ssid': 'str',
        'locations': 'list[WiFiLocation]',
        'score': 'int',
        'days_observed_count': 'int'
    }

    attribute_map = {
        'centroid_latitude': 'centroidLatitude',
        'centroid_longitude': 'centroidLongitude',
        'min_last_update': 'minLastUpdate',
        'max_last_update': 'maxLastUpdate',
        'cluster_ssid': 'clusterSsid',
        'locations': 'locations',
        'score': 'score',
        'days_observed_count': 'daysObservedCount'
    }

    def __init__(self, centroid_latitude=None, centroid_longitude=None, min_last_update=None, max_last_update=None, cluster_ssid=None, locations=None, score=None, days_observed_count=None, _configuration=None):  # noqa: E501
        """WiFiLocationCluster - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._centroid_latitude = None
        self._centroid_longitude = None
        self._min_last_update = None
        self._max_last_update = None
        self._cluster_ssid = None
        self._locations = None
        self._score = None
        self._days_observed_count = None
        self.discriminator = None

        if centroid_latitude is not None:
            self.centroid_latitude = centroid_latitude
        if centroid_longitude is not None:
            self.centroid_longitude = centroid_longitude
        if min_last_update is not None:
            self.min_last_update = min_last_update
        if max_last_update is not None:
            self.max_last_update = max_last_update
        if cluster_ssid is not None:
            self.cluster_ssid = cluster_ssid
        if locations is not None:
            self.locations = locations
        if score is not None:
            self.score = score
        if days_observed_count is not None:
            self.days_observed_count = days_observed_count

    @property
    def centroid_latitude(self):
        """Gets the centroid_latitude of this WiFiLocationCluster.  # noqa: E501


        :return: The centroid_latitude of this WiFiLocationCluster.  # noqa: E501
        :rtype: float
        """
        return self._centroid_latitude

    @centroid_latitude.setter
    def centroid_latitude(self, centroid_latitude):
        """Sets the centroid_latitude of this WiFiLocationCluster.


        :param centroid_latitude: The centroid_latitude of this WiFiLocationCluster.  # noqa: E501
        :type: float
        """

        self._centroid_latitude = centroid_latitude

    @property
    def centroid_longitude(self):
        """Gets the centroid_longitude of this WiFiLocationCluster.  # noqa: E501


        :return: The centroid_longitude of this WiFiLocationCluster.  # noqa: E501
        :rtype: float
        """
        return self._centroid_longitude

    @centroid_longitude.setter
    def centroid_longitude(self, centroid_longitude):
        """Sets the centroid_longitude of this WiFiLocationCluster.


        :param centroid_longitude: The centroid_longitude of this WiFiLocationCluster.  # noqa: E501
        :type: float
        """

        self._centroid_longitude = centroid_longitude

    @property
    def min_last_update(self):
        """Gets the min_last_update of this WiFiLocationCluster.  # noqa: E501


        :return: The min_last_update of this WiFiLocationCluster.  # noqa: E501
        :rtype: datetime
        """
        return self._min_last_update

    @min_last_update.setter
    def min_last_update(self, min_last_update):
        """Sets the min_last_update of this WiFiLocationCluster.


        :param min_last_update: The min_last_update of this WiFiLocationCluster.  # noqa: E501
        :type: datetime
        """

        self._min_last_update = min_last_update

    @property
    def max_last_update(self):
        """Gets the max_last_update of this WiFiLocationCluster.  # noqa: E501


        :return: The max_last_update of this WiFiLocationCluster.  # noqa: E501
        :rtype: datetime
        """
        return self._max_last_update

    @max_last_update.setter
    def max_last_update(self, max_last_update):
        """Sets the max_last_update of this WiFiLocationCluster.


        :param max_last_update: The max_last_update of this WiFiLocationCluster.  # noqa: E501
        :type: datetime
        """

        self._max_last_update = max_last_update

    @property
    def cluster_ssid(self):
        """Gets the cluster_ssid of this WiFiLocationCluster.  # noqa: E501


        :return: The cluster_ssid of this WiFiLocationCluster.  # noqa: E501
        :rtype: str
        """
        return self._cluster_ssid

    @cluster_ssid.setter
    def cluster_ssid(self, cluster_ssid):
        """Sets the cluster_ssid of this WiFiLocationCluster.


        :param cluster_ssid: The cluster_ssid of this WiFiLocationCluster.  # noqa: E501
        :type: str
        """

        self._cluster_ssid = cluster_ssid

    @property
    def locations(self):
        """Gets the locations of this WiFiLocationCluster.  # noqa: E501


        :return: The locations of this WiFiLocationCluster.  # noqa: E501
        :rtype: list[WiFiLocation]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this WiFiLocationCluster.


        :param locations: The locations of this WiFiLocationCluster.  # noqa: E501
        :type: list[WiFiLocation]
        """

        self._locations = locations

    @property
    def score(self):
        """Gets the score of this WiFiLocationCluster.  # noqa: E501


        :return: The score of this WiFiLocationCluster.  # noqa: E501
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this WiFiLocationCluster.


        :param score: The score of this WiFiLocationCluster.  # noqa: E501
        :type: int
        """

        self._score = score

    @property
    def days_observed_count(self):
        """Gets the days_observed_count of this WiFiLocationCluster.  # noqa: E501


        :return: The days_observed_count of this WiFiLocationCluster.  # noqa: E501
        :rtype: int
        """
        return self._days_observed_count

    @days_observed_count.setter
    def days_observed_count(self, days_observed_count):
        """Sets the days_observed_count of this WiFiLocationCluster.


        :param days_observed_count: The days_observed_count of this WiFiLocationCluster.  # noqa: E501
        :type: int
        """

        self._days_observed_count = days_observed_count

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
        if issubclass(WiFiLocationCluster, dict):
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
        if not isinstance(other, WiFiLocationCluster):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WiFiLocationCluster):
            return True

        return self.to_dict() != other.to_dict()
