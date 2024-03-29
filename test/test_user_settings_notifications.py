# coding: utf-8

"""
    Overseerr API

    This is the documentation for the Overseerr API backend.  Two primary authentication methods are supported:  - **Cookie Authentication**: A valid sign-in to the `/auth/plex` or `/auth/local` will generate a valid authentication cookie. - **API Key Authentication**: Sign-in is also possible by passing an `X-Api-Key` header along with a valid API Key generated by Overseerr. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from overseerr_api.models.user_settings_notifications import UserSettingsNotifications  # noqa: E501

class TestUserSettingsNotifications(unittest.TestCase):
    """UserSettingsNotifications unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserSettingsNotifications:
        """Test UserSettingsNotifications
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserSettingsNotifications`
        """
        model = UserSettingsNotifications()  # noqa: E501
        if include_optional:
            return UserSettingsNotifications(
                discord_enabled = True,
                discord_enabled_types = 1.337,
                discord_id = '',
                email_enabled = True,
                notification_types = overseerr_api.models.notification_agent_types.NotificationAgentTypes(
                    discord = 1.337, 
                    email = 1.337, 
                    pushbullet = 1.337, 
                    pushover = 1.337, 
                    slack = 1.337, 
                    telegram = 1.337, 
                    webhook = 1.337, 
                    webpush = 1.337, ),
                pgp_key = '',
                pushbullet_access_token = '',
                pushover_application_token = '',
                pushover_sound = '',
                pushover_user_key = '',
                telegram_bot_username = '',
                telegram_chat_id = '',
                telegram_enabled = True,
                telegram_send_silently = True
            )
        else:
            return UserSettingsNotifications(
        )
        """

    def testUserSettingsNotifications(self):
        """Test UserSettingsNotifications"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
