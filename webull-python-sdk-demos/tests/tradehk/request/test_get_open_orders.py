import unittest

from webullsdkcore.client import ApiClient
from webullsdkcore.exception.exceptions import ServerException
from webullsdktradehk.request.get_open_orders_request import OpenOrdersListRequest

optional_api_endpoint = "<api_endpoint>"
your_app_key = "<your_app_key>"
your_app_secret = "<your_app_secret>"
account_id = "<your_account_id>"
api_client = ApiClient(your_app_key, your_app_secret)


class TestOpenOrdersListRequest(unittest.TestCase):
    def test_get_open_orders_list(self):
        request = OpenOrdersListRequest()
        request.set_endpoint(optional_api_endpoint)
        request.set_account_id(account_id)
        request.set_page_size(10)

        try:
            response = api_client.get_response(request)
            print(response.json())
        except ServerException as se:
            print(se.get_error_code(), ":", se.get_error_msg())