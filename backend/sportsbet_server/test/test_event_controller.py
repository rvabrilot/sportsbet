# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from sportsbet_server.test import BaseTestCase


class TestEventController(BaseTestCase):
    """EventController integration test stubs"""

    def test_get_events(self):
        """Test case for get_events

        Returns events available to bet on
        """
        response = self.client.open(
            '/api/v3/event',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
