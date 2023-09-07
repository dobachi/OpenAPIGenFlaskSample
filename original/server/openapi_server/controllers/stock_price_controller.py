import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.stock_price import StockPrice  # noqa: E501
from openapi_server import util


def stock_price(security_cd):  # noqa: E501
    """株価取得

    現在の株価を取得する # noqa: E501

    :param security_cd: 証券コードを指定する
    :type security_cd: str

    :rtype: Union[StockPrice, Tuple[StockPrice, int], Tuple[StockPrice, int, Dict[str, str]]
    """
    return 'do some magic!'
