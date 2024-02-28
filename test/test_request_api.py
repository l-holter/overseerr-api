# coding: utf-8

"""
    Overseerr API

    This is the documentation for the Overseerr API backend.  Two primary authentication methods are supported:  - **Cookie Authentication**: A valid sign-in to the `/auth/plex` or `/auth/local` will generate a valid authentication cookie. - **API Key Authentication**: Sign-in is also possible by passing an `X-Api-Key` header along with a valid API Key generated by Overseerr. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from overseerr_api.api.request_api import RequestApi  # noqa: E501


class TestRequestApi(unittest.TestCase):
    """RequestApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RequestApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_request_count_get(self) -> None:
        """Test case for request_count_get

        Gets request counts  # noqa: E501
        """
        pass

    def test_request_get(self) -> None:
        """Test case for request_get

        Get all requests  # noqa: E501
        """
        pass

    def test_request_post(self) -> None:
        """Test case for request_post

        Create new request  # noqa: E501
        """
        pass

    def test_request_request_id_delete(self) -> None:
        """Test case for request_request_id_delete

        Delete request  # noqa: E501
        """
        pass

    def test_request_request_id_get(self) -> None:
        """Test case for request_request_id_get

        Get MediaRequest  # noqa: E501
        """
        pass

    def test_request_request_id_put(self) -> None:
        """Test case for request_request_id_put

        Update MediaRequest  # noqa: E501
        """
        pass

    def test_request_request_id_retry_post(self) -> None:
        """Test case for request_request_id_retry_post

        Retry failed request  # noqa: E501
        """
        pass

    def test_request_request_id_status_post(self) -> None:
        """Test case for request_request_id_status_post

        Update a request's status  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()