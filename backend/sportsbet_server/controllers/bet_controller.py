import connexion
import six

from sportsbet_server.models import Bet


def add_bet(user_id, event_ids, amount, api_key=None):
    """Add a new bet

    Add a new bet # noqa: E501

    :param user_id: ID of user who made the bet
    :type user_id: str
    :param event_ids: Comma separated list of eventIds that this bet is on
    :type event_ids: str
    :param amount: amount of credits for this bet to be taken from the user
    :type amount: str
    :param api_key: 
    :type api_key: str

    :rtype: Bet
    """
    return 'do some magic!'


def delete_bet(bet_id, api_key=None):  # noqa: E501
    """Deletes a bet

    delete a bet # noqa: E501

    :param bet_id: Bet id to delete
    :type bet_id: int
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def get_bet_by_id(bet_id, api_key=None):  # noqa: E501
    """Find bet by ID

    Returns a single bet # noqa: E501

    :param bet_id: ID of bet to return
    :type bet_id: int
    :param api_key: 
    :type api_key: str

    :rtype: Bet
    """
    return 'do some magic!'
