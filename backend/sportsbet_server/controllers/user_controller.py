import connexion
import six

from sportsbet_server.models import User  # noqa: E501
from sportsbet_server import util

def get_users(body=None):
    return 'To-DO'
    
def create_user(body=None):  # noqa: E501
    """Create user

    This can only be done by the logged in user. # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_user(id=None, nickname=None, email=None, md5=None, credit=None):  # noqa: E501
    """Create user

    This can only be done by the logged in user. # noqa: E501

    :param id: 
    :type id: str
    :param nickname: 
    :type nickname: str
    :param email: 
    :type email: str
    :param md5: 
    :type md5: str
    :param credit: 
    :type credit: float

    :rtype: User
    """
    return 'do some magic!'


def create_users_with_list_input(body=None):  # noqa: E501
    """Creates list of users with given input array

    Creates list of users with given input array # noqa: E501

    :param body: 
    :type body: list | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = [User.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def delete_user(username):  # noqa: E501
    """Delete user

    This can only be done by the logged in user. # noqa: E501

    :param username: The name that needs to be deleted
    :type username: str

    :rtype: None
    """
    return 'do some magic!'


def get_user_by_id(user_id):  # noqa: E501
    """Get user by user name

     # noqa: E501

    :param username: The name that needs to be fetched. Use user1 for testing. 
    :type username: str

    :rtype: User
    """
    return 'do some magic!'


def login_user(username=None, password=None):  # noqa: E501
    """Logs user into the system

     # noqa: E501

    :param username: The user name for login
    :type username: str
    :param password: The password for login in clear text
    :type password: str

    :rtype: str
    """
    return 'do some magic!'


def logout_user():  # noqa: E501
    """Logs out current logged in user session

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def update_user(username, body=None):  # noqa: E501
    """Update user

    This can only be done by the logged in user. # noqa: E501

    :param username: name that need to be deleted
    :type username: str
    :param body: Update an existent user in the event
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_user(username, id=None, nickname=None, email=None, md5=None, credit=None):  # noqa: E501
    """Update user

    This can only be done by the logged in user. # noqa: E501

    :param username: name that need to be deleted
    :type username: str
    :param id: 
    :type id: str
    :param nickname: 
    :type nickname: str
    :param email: 
    :type email: str
    :param md5: 
    :type md5: str
    :param credit: 
    :type credit: float

    :rtype: None
    """
    return 'do some magic!'
