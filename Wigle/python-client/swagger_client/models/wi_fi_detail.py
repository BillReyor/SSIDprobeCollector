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


class WiFiDetail(object):
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
        'trilaterated_latitude': 'float',
        'trilaterated_longitude': 'float',
        'best_cluster_wi_gle_qo_s': 'int',
        'first_seen': 'datetime',
        'last_seen': 'datetime',
        'last_update': 'datetime',
        'street_address': 'StreetAddress',
        'network_id': 'str',
        'name': 'str',
        'type': 'str',
        'comment': 'str',
        'bcninterval': 'int',
        'freenet': 'str',
        'dhcp': 'str',
        'paynet': 'str',
        'encryption': 'str',
        'channel': 'int',
        'location_clusters': 'list[WiFiLocationCluster]'
    }

    attribute_map = {
        'trilaterated_latitude': 'trilateratedLatitude',
        'trilaterated_longitude': 'trilateratedLongitude',
        'best_cluster_wi_gle_qo_s': 'bestClusterWiGLEQoS',
        'first_seen': 'firstSeen',
        'last_seen': 'lastSeen',
        'last_update': 'lastUpdate',
        'street_address': 'streetAddress',
        'network_id': 'networkId',
        'name': 'name',
        'type': 'type',
        'comment': 'comment',
        'bcninterval': 'bcninterval',
        'freenet': 'freenet',
        'dhcp': 'dhcp',
        'paynet': 'paynet',
        'encryption': 'encryption',
        'channel': 'channel',
        'location_clusters': 'locationClusters'
    }

    def __init__(self, trilaterated_latitude=None, trilaterated_longitude=None, best_cluster_wi_gle_qo_s=None, first_seen=None, last_seen=None, last_update=None, street_address=None, network_id=None, name=None, type=None, comment=None, bcninterval=None, freenet=None, dhcp=None, paynet=None, encryption=None, channel=None, location_clusters=None, _configuration=None):  # noqa: E501
        """WiFiDetail - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._trilaterated_latitude = None
        self._trilaterated_longitude = None
        self._best_cluster_wi_gle_qo_s = None
        self._first_seen = None
        self._last_seen = None
        self._last_update = None
        self._street_address = None
        self._network_id = None
        self._name = None
        self._type = None
        self._comment = None
        self._bcninterval = None
        self._freenet = None
        self._dhcp = None
        self._paynet = None
        self._encryption = None
        self._channel = None
        self._location_clusters = None
        self.discriminator = None

        if trilaterated_latitude is not None:
            self.trilaterated_latitude = trilaterated_latitude
        if trilaterated_longitude is not None:
            self.trilaterated_longitude = trilaterated_longitude
        if best_cluster_wi_gle_qo_s is not None:
            self.best_cluster_wi_gle_qo_s = best_cluster_wi_gle_qo_s
        if first_seen is not None:
            self.first_seen = first_seen
        if last_seen is not None:
            self.last_seen = last_seen
        if last_update is not None:
            self.last_update = last_update
        if street_address is not None:
            self.street_address = street_address
        self.network_id = network_id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if comment is not None:
            self.comment = comment
        if bcninterval is not None:
            self.bcninterval = bcninterval
        if freenet is not None:
            self.freenet = freenet
        if dhcp is not None:
            self.dhcp = dhcp
        if paynet is not None:
            self.paynet = paynet
        if encryption is not None:
            self.encryption = encryption
        if channel is not None:
            self.channel = channel
        if location_clusters is not None:
            self.location_clusters = location_clusters

    @property
    def trilaterated_latitude(self):
        """Gets the trilaterated_latitude of this WiFiDetail.  # noqa: E501


        :return: The trilaterated_latitude of this WiFiDetail.  # noqa: E501
        :rtype: float
        """
        return self._trilaterated_latitude

    @trilaterated_latitude.setter
    def trilaterated_latitude(self, trilaterated_latitude):
        """Sets the trilaterated_latitude of this WiFiDetail.


        :param trilaterated_latitude: The trilaterated_latitude of this WiFiDetail.  # noqa: E501
        :type: float
        """

        self._trilaterated_latitude = trilaterated_latitude

    @property
    def trilaterated_longitude(self):
        """Gets the trilaterated_longitude of this WiFiDetail.  # noqa: E501


        :return: The trilaterated_longitude of this WiFiDetail.  # noqa: E501
        :rtype: float
        """
        return self._trilaterated_longitude

    @trilaterated_longitude.setter
    def trilaterated_longitude(self, trilaterated_longitude):
        """Sets the trilaterated_longitude of this WiFiDetail.


        :param trilaterated_longitude: The trilaterated_longitude of this WiFiDetail.  # noqa: E501
        :type: float
        """

        self._trilaterated_longitude = trilaterated_longitude

    @property
    def best_cluster_wi_gle_qo_s(self):
        """Gets the best_cluster_wi_gle_qo_s of this WiFiDetail.  # noqa: E501


        :return: The best_cluster_wi_gle_qo_s of this WiFiDetail.  # noqa: E501
        :rtype: int
        """
        return self._best_cluster_wi_gle_qo_s

    @best_cluster_wi_gle_qo_s.setter
    def best_cluster_wi_gle_qo_s(self, best_cluster_wi_gle_qo_s):
        """Sets the best_cluster_wi_gle_qo_s of this WiFiDetail.


        :param best_cluster_wi_gle_qo_s: The best_cluster_wi_gle_qo_s of this WiFiDetail.  # noqa: E501
        :type: int
        """

        self._best_cluster_wi_gle_qo_s = best_cluster_wi_gle_qo_s

    @property
    def first_seen(self):
        """Gets the first_seen of this WiFiDetail.  # noqa: E501


        :return: The first_seen of this WiFiDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._first_seen

    @first_seen.setter
    def first_seen(self, first_seen):
        """Sets the first_seen of this WiFiDetail.


        :param first_seen: The first_seen of this WiFiDetail.  # noqa: E501
        :type: datetime
        """

        self._first_seen = first_seen

    @property
    def last_seen(self):
        """Gets the last_seen of this WiFiDetail.  # noqa: E501


        :return: The last_seen of this WiFiDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen):
        """Sets the last_seen of this WiFiDetail.


        :param last_seen: The last_seen of this WiFiDetail.  # noqa: E501
        :type: datetime
        """

        self._last_seen = last_seen

    @property
    def last_update(self):
        """Gets the last_update of this WiFiDetail.  # noqa: E501


        :return: The last_update of this WiFiDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this WiFiDetail.


        :param last_update: The last_update of this WiFiDetail.  # noqa: E501
        :type: datetime
        """

        self._last_update = last_update

    @property
    def street_address(self):
        """Gets the street_address of this WiFiDetail.  # noqa: E501


        :return: The street_address of this WiFiDetail.  # noqa: E501
        :rtype: StreetAddress
        """
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        """Sets the street_address of this WiFiDetail.


        :param street_address: The street_address of this WiFiDetail.  # noqa: E501
        :type: StreetAddress
        """

        self._street_address = street_address

    @property
    def network_id(self):
        """Gets the network_id of this WiFiDetail.  # noqa: E501


        :return: The network_id of this WiFiDetail.  # noqa: E501
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this WiFiDetail.


        :param network_id: The network_id of this WiFiDetail.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and network_id is None:
            raise ValueError("Invalid value for `network_id`, must not be `None`")  # noqa: E501

        self._network_id = network_id

    @property
    def name(self):
        """Gets the name of this WiFiDetail.  # noqa: E501


        :return: The name of this WiFiDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WiFiDetail.


        :param name: The name of this WiFiDetail.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this WiFiDetail.  # noqa: E501


        :return: The type of this WiFiDetail.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WiFiDetail.


        :param type: The type of this WiFiDetail.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def comment(self):
        """Gets the comment of this WiFiDetail.  # noqa: E501


        :return: The comment of this WiFiDetail.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this WiFiDetail.


        :param comment: The comment of this WiFiDetail.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def bcninterval(self):
        """Gets the bcninterval of this WiFiDetail.  # noqa: E501


        :return: The bcninterval of this WiFiDetail.  # noqa: E501
        :rtype: int
        """
        return self._bcninterval

    @bcninterval.setter
    def bcninterval(self, bcninterval):
        """Sets the bcninterval of this WiFiDetail.


        :param bcninterval: The bcninterval of this WiFiDetail.  # noqa: E501
        :type: int
        """

        self._bcninterval = bcninterval

    @property
    def freenet(self):
        """Gets the freenet of this WiFiDetail.  # noqa: E501


        :return: The freenet of this WiFiDetail.  # noqa: E501
        :rtype: str
        """
        return self._freenet

    @freenet.setter
    def freenet(self, freenet):
        """Sets the freenet of this WiFiDetail.


        :param freenet: The freenet of this WiFiDetail.  # noqa: E501
        :type: str
        """

        self._freenet = freenet

    @property
    def dhcp(self):
        """Gets the dhcp of this WiFiDetail.  # noqa: E501


        :return: The dhcp of this WiFiDetail.  # noqa: E501
        :rtype: str
        """
        return self._dhcp

    @dhcp.setter
    def dhcp(self, dhcp):
        """Sets the dhcp of this WiFiDetail.


        :param dhcp: The dhcp of this WiFiDetail.  # noqa: E501
        :type: str
        """

        self._dhcp = dhcp

    @property
    def paynet(self):
        """Gets the paynet of this WiFiDetail.  # noqa: E501


        :return: The paynet of this WiFiDetail.  # noqa: E501
        :rtype: str
        """
        return self._paynet

    @paynet.setter
    def paynet(self, paynet):
        """Sets the paynet of this WiFiDetail.


        :param paynet: The paynet of this WiFiDetail.  # noqa: E501
        :type: str
        """

        self._paynet = paynet

    @property
    def encryption(self):
        """Gets the encryption of this WiFiDetail.  # noqa: E501


        :return: The encryption of this WiFiDetail.  # noqa: E501
        :rtype: str
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        """Sets the encryption of this WiFiDetail.


        :param encryption: The encryption of this WiFiDetail.  # noqa: E501
        :type: str
        """

        self._encryption = encryption

    @property
    def channel(self):
        """Gets the channel of this WiFiDetail.  # noqa: E501


        :return: The channel of this WiFiDetail.  # noqa: E501
        :rtype: int
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this WiFiDetail.


        :param channel: The channel of this WiFiDetail.  # noqa: E501
        :type: int
        """

        self._channel = channel

    @property
    def location_clusters(self):
        """Gets the location_clusters of this WiFiDetail.  # noqa: E501


        :return: The location_clusters of this WiFiDetail.  # noqa: E501
        :rtype: list[WiFiLocationCluster]
        """
        return self._location_clusters

    @location_clusters.setter
    def location_clusters(self, location_clusters):
        """Sets the location_clusters of this WiFiDetail.


        :param location_clusters: The location_clusters of this WiFiDetail.  # noqa: E501
        :type: list[WiFiLocationCluster]
        """

        self._location_clusters = location_clusters

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
        if issubclass(WiFiDetail, dict):
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
        if not isinstance(other, WiFiDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WiFiDetail):
            return True

        return self.to_dict() != other.to_dict()
