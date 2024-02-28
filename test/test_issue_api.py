# coding: utf-8

"""
    Overseerr API

    This is the documentation for the Overseerr API backend.  Two primary authentication methods are supported:  - **Cookie Authentication**: A valid sign-in to the `/auth/plex` or `/auth/local` will generate a valid authentication cookie. - **API Key Authentication**: Sign-in is also possible by passing an `X-Api-Key` header along with a valid API Key generated by Overseerr. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from overseerr_api.api.issue_api import IssueApi  # noqa: E501


class TestIssueApi(unittest.TestCase):
    """IssueApi unit test stubs"""

    def setUp(self) -> None:
        self.api = IssueApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_issue_comment_comment_id_delete(self) -> None:
        """Test case for issue_comment_comment_id_delete

        Delete issue comment  # noqa: E501
        """
        pass

    def test_issue_comment_comment_id_get(self) -> None:
        """Test case for issue_comment_comment_id_get

        Get issue comment  # noqa: E501
        """
        pass

    def test_issue_comment_comment_id_put(self) -> None:
        """Test case for issue_comment_comment_id_put

        Update issue comment  # noqa: E501
        """
        pass

    def test_issue_count_get(self) -> None:
        """Test case for issue_count_get

        Gets issue counts  # noqa: E501
        """
        pass

    def test_issue_get(self) -> None:
        """Test case for issue_get

        Get all issues  # noqa: E501
        """
        pass

    def test_issue_issue_id_comment_post(self) -> None:
        """Test case for issue_issue_id_comment_post

        Create a comment  # noqa: E501
        """
        pass

    def test_issue_issue_id_delete(self) -> None:
        """Test case for issue_issue_id_delete

        Delete issue  # noqa: E501
        """
        pass

    def test_issue_issue_id_get(self) -> None:
        """Test case for issue_issue_id_get

        Get issue  # noqa: E501
        """
        pass

    def test_issue_issue_id_status_post(self) -> None:
        """Test case for issue_issue_id_status_post

        Update an issue's status  # noqa: E501
        """
        pass

    def test_issue_post(self) -> None:
        """Test case for issue_post

        Create new issue  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
