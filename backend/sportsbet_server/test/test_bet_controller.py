# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from sportsbet_server.models.bet import Bet  # noqa: E501
from sportsbet_server.test import BaseTestCase


class TestBetController(BaseTestCase):
    """BetController integration test stubs"""

    def test_add_bet(self):
        """Test case for add_bet

        Add a new bet
        """
        query_string = [('user_id', 'user_id_example'),
                        ('event_ids', 'event_ids_example'),
                        ('amount', 'amount_example')]
        headers = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/api/v3/bet',
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_bet(self):
        """Test case for delete_bet

        Deletes a bet
        """
        headers = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/api/v3/bet/{betId}'.format(bet_id=789),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_bet_by_id(self):
        """Test case for get_bet_by_id

        Find bet by ID
        """
        headers = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/api/v3/bet/{betId}'.format(bet_id=789),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
