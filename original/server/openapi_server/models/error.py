from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class Error(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, message=None, field=None):  # noqa: E501
        """Error - a model defined in OpenAPI

        :param message: The message of this Error.  # noqa: E501
        :type message: str
        :param field: The field of this Error.  # noqa: E501
        :type field: str
        """
        self.openapi_types = {
            'message': str,
            'field': str
        }

        self.attribute_map = {
            'message': 'message',
            'field': 'field'
        }

        self._message = message
        self._field = field

    @classmethod
    def from_dict(cls, dikt) -> 'Error':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Error of this Error.  # noqa: E501
        :rtype: Error
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message(self) -> str:
        """Gets the message of this Error.

        エラーメッセージ  # noqa: E501

        :return: The message of this Error.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this Error.

        エラーメッセージ  # noqa: E501

        :param message: The message of this Error.
        :type message: str
        """

        self._message = message

    @property
    def field(self) -> str:
        """Gets the field of this Error.

        エラー種別  # noqa: E501

        :return: The field of this Error.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field: str):
        """Sets the field of this Error.

        エラー種別  # noqa: E501

        :param field: The field of this Error.
        :type field: str
        """

        self._field = field
