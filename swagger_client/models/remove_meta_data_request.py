# coding: utf-8

"""
    GSI Floating-Point 32 API

    **Introduction**<br> GSI Technology’s floating-point similarity search API provides an accessible gateway to running searches on GSI’s Gemini® Associative Processing Unit (APU).<br> It works in conjunction with the GSI system management solution which enables users to work with multiple APU boards simultaneously for improved performance.<br><br> **Dataset and Query Format**<br> Dataset embeddings can be in 32- or 64-bit floating point format, and any number of features, e.g. 256 or 512 (there is no upper limit).<br> Query embeddings must have the same floating-point format and number of features as used in the dataset.<br> GSI performs the search and delivers the top-k most similar results.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RemoveMetaDataRequest(object):
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
        'allocation_id': 'str',
        'dataset_id': 'str',
        'metadata_values': 'list[Object]'
    }

    attribute_map = {
        'allocation_id': 'allocationId',
        'dataset_id': 'datasetId',
        'metadata_values': 'metadataValues'
    }

    def __init__(self, allocation_id=None, dataset_id=None, metadata_values=None):  # noqa: E501
        """RemoveMetaDataRequest - a model defined in Swagger"""  # noqa: E501
        self._allocation_id = None
        self._dataset_id = None
        self._metadata_values = None
        self.discriminator = None
        self.allocation_id = allocation_id
        self.dataset_id = dataset_id
        self.metadata_values = metadata_values

    @property
    def allocation_id(self):
        """Gets the allocation_id of this RemoveMetaDataRequest.  # noqa: E501

        The UID representing an allocation of a specific number of APU boards. It is generated using the /allocate endpoint.  # noqa: E501

        :return: The allocation_id of this RemoveMetaDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._allocation_id

    @allocation_id.setter
    def allocation_id(self, allocation_id):
        """Sets the allocation_id of this RemoveMetaDataRequest.

        The UID representing an allocation of a specific number of APU boards. It is generated using the /allocate endpoint.  # noqa: E501

        :param allocation_id: The allocation_id of this RemoveMetaDataRequest.  # noqa: E501
        :type: str
        """
        if allocation_id is None:
            raise ValueError("Invalid value for `allocation_id`, must not be `None`")  # noqa: E501

        self._allocation_id = allocation_id

    @property
    def dataset_id(self):
        """Gets the dataset_id of this RemoveMetaDataRequest.  # noqa: E501

        Dataset UID identifies specific dataset to remove data from. It is generated using the /import/dataset ednpoint.  # noqa: E501

        :return: The dataset_id of this RemoveMetaDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this RemoveMetaDataRequest.

        Dataset UID identifies specific dataset to remove data from. It is generated using the /import/dataset ednpoint.  # noqa: E501

        :param dataset_id: The dataset_id of this RemoveMetaDataRequest.  # noqa: E501
        :type: str
        """
        if dataset_id is None:
            raise ValueError("Invalid value for `dataset_id`, must not be `None`")  # noqa: E501

        self._dataset_id = dataset_id

    @property
    def metadata_values(self):
        """Gets the metadata_values of this RemoveMetaDataRequest.  # noqa: E501

        One-dimensional array containing the metadata values to find and based its indices to remove  # noqa: E501

        :return: The metadata_values of this RemoveMetaDataRequest.  # noqa: E501
        :rtype: list[Object]
        """
        return self._metadata_values

    @metadata_values.setter
    def metadata_values(self, metadata_values):
        """Sets the metadata_values of this RemoveMetaDataRequest.

        One-dimensional array containing the metadata values to find and based its indices to remove  # noqa: E501

        :param metadata_values: The metadata_values of this RemoveMetaDataRequest.  # noqa: E501
        :type: list[Object]
        """
        if metadata_values is None:
            raise ValueError("Invalid value for `metadata_values`, must not be `None`")  # noqa: E501

        self._metadata_values = metadata_values

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
        if issubclass(RemoveMetaDataRequest, dict):
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
        if not isinstance(other, RemoveMetaDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
