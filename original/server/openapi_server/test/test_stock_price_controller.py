import unittest

from flask import json

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.stock_price import StockPrice  # noqa: E501
from openapi_server.test import BaseTestCase


class TestStockPriceController(BaseTestCase):
    """StockPriceController integration test stubs"""

    def test_stock_price(self):
        """Test case for stock_price

        株価取得
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1/sc/{security_cd}/stockPrice'.format(security_cd='4722'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
