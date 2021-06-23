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

class AddDataRequest(object):
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
        'data_to_add': 'OneOfAddDataRequestDataToAdd',
        'metadata_to_add': 'list[Object]',
        'records_to_add_file_type': 'str'
    }

    attribute_map = {
        'allocation_id': 'allocationId',
        'dataset_id': 'datasetId',
        'data_to_add': 'dataToAdd',
        'metadata_to_add': 'metadataToAdd',
        'records_to_add_file_type': 'records_to_add_file_type'
    }

    def __init__(self, allocation_id=None, dataset_id=None, data_to_add=None, metadata_to_add=None, records_to_add_file_type=None):  # noqa: E501
        """AddDataRequest - a model defined in Swagger"""  # noqa: E501
        self._allocation_id = None
        self._dataset_id = None
        self._data_to_add = None
        self._metadata_to_add = None
        self._records_to_add_file_type = None
        self.discriminator = None
        self.allocation_id = allocation_id
        self.dataset_id = dataset_id
        self.data_to_add = data_to_add
        if metadata_to_add is not None:
            self.metadata_to_add = metadata_to_add
        if records_to_add_file_type is not None:
            self.records_to_add_file_type = records_to_add_file_type

    @property
    def allocation_id(self):
        """Gets the allocation_id of this AddDataRequest.  # noqa: E501

        The UID representing an allocation of a specific number of APU boards. It is generated using the /allocate endpoint.  # noqa: E501

        :return: The allocation_id of this AddDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._allocation_id

    @allocation_id.setter
    def allocation_id(self, allocation_id):
        """Sets the allocation_id of this AddDataRequest.

        The UID representing an allocation of a specific number of APU boards. It is generated using the /allocate endpoint.  # noqa: E501

        :param allocation_id: The allocation_id of this AddDataRequest.  # noqa: E501
        :type: str
        """
        if allocation_id is None:
            raise ValueError("Invalid value for `allocation_id`, must not be `None`")  # noqa: E501

        self._allocation_id = allocation_id

    @property
    def dataset_id(self):
        """Gets the dataset_id of this AddDataRequest.  # noqa: E501

        The datasetId identifies the specific dataset to search. It is generated using the /import/dataset endpoint.  # noqa: E501

        :return: The dataset_id of this AddDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this AddDataRequest.

        The datasetId identifies the specific dataset to search. It is generated using the /import/dataset endpoint.  # noqa: E501

        :param dataset_id: The dataset_id of this AddDataRequest.  # noqa: E501
        :type: str
        """
        if dataset_id is None:
            raise ValueError("Invalid value for `dataset_id`, must not be `None`")  # noqa: E501

        self._dataset_id = dataset_id

    @property
    def data_to_add(self):
        """Gets the data_to_add of this AddDataRequest.  # noqa: E501


        :return: The data_to_add of this AddDataRequest.  # noqa: E501
        :rtype: OneOfAddDataRequestDataToAdd
        """
        return self._data_to_add

    @data_to_add.setter
    def data_to_add(self, data_to_add):
        """Sets the data_to_add of this AddDataRequest.


        :param data_to_add: The data_to_add of this AddDataRequest.  # noqa: E501
        :type: OneOfAddDataRequestDataToAdd
        """
        if data_to_add is None:
            raise ValueError("Invalid value for `data_to_add`, must not be `None`")  # noqa: E501

        self._data_to_add = data_to_add

    @property
    def metadata_to_add(self):
        """Gets the metadata_to_add of this AddDataRequest.  # noqa: E501

        One-dimensional array containing the metadata values to add  # noqa: E501

        :return: The metadata_to_add of this AddDataRequest.  # noqa: E501
        :rtype: list[Object]
        """
        return self._metadata_to_add

    @metadata_to_add.setter
    def metadata_to_add(self, metadata_to_add):
        """Sets the metadata_to_add of this AddDataRequest.

        One-dimensional array containing the metadata values to add  # noqa: E501

        :param metadata_to_add: The metadata_to_add of this AddDataRequest.  # noqa: E501
        :type: list[Object]
        """

        self._metadata_to_add = metadata_to_add

    @property
    def records_to_add_file_type(self):
        """Gets the records_to_add_file_type of this AddDataRequest.  # noqa: E501

        indicates the file type. if no value will be set, read file will based file extension  # noqa: E501

        :return: The records_to_add_file_type of this AddDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._records_to_add_file_type

    @records_to_add_file_type.setter
    def records_to_add_file_type(self, records_to_add_file_type):
        """Sets the records_to_add_file_type of this AddDataRequest.

        indicates the file type. if no value will be set, read file will based file extension  # noqa: E501

        :param records_to_add_file_type: The records_to_add_file_type of this AddDataRequest.  # noqa: E501
        :type: str
        """

        self._records_to_add_file_type = records_to_add_file_type

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
        if issubclass(AddDataRequest, dict):
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
        if not isinstance(other, AddDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
