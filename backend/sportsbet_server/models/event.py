# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from sportsbet_server.models.base_model_ import Model
from sportsbet_server import util


class Event(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, event_start: str=None, event_end: str=None, local_player: str=None, visitor_player: str=None, category: str=None, rlf: float=None, rfv: float=None, rfe: float=None, ptl: float=None, ptv: float=None, pte: float=None, gv0: float=None, gv1: float=None, gv2: float=None, gv3: float=None):  # noqa: E501
        """Event - a model defined in Swagger

        :param id: The id of this Event.  # noqa: E501
        :type id: str
        :param event_start: The event_start of this Event.  # noqa: E501
        :type event_start: str
        :param event_end: The event_end of this Event.  # noqa: E501
        :type event_end: str
        :param local_player: The local_player of this Event.  # noqa: E501
        :type local_player: str
        :param visitor_player: The visitor_player of this Event.  # noqa: E501
        :type visitor_player: str
        :param category: The category of this Event.  # noqa: E501
        :type category: str
        :param rlf: The rlf of this Event.  # noqa: E501
        :type rlf: float
        :param rfv: The rfv of this Event.  # noqa: E501
        :type rfv: float
        :param rfe: The rfe of this Event.  # noqa: E501
        :type rfe: float
        :param ptl: The ptl of this Event.  # noqa: E501
        :type ptl: float
        :param ptv: The ptv of this Event.  # noqa: E501
        :type ptv: float
        :param pte: The pte of this Event.  # noqa: E501
        :type pte: float
        :param gv0: The gv0 of this Event.  # noqa: E501
        :type gv0: float
        :param gv1: The gv1 of this Event.  # noqa: E501
        :type gv1: float
        :param gv2: The gv2 of this Event.  # noqa: E501
        :type gv2: float
        :param gv3: The gv3 of this Event.  # noqa: E501
        :type gv3: float
        """
        self.swagger_types = {
            'id': str,
            'event_start': str,
            'event_end': str,
            'local_player': str,
            'visitor_player': str,
            'category': str,
            'rlf': float,
            'rfv': float,
            'rfe': float,
            'ptl': float,
            'ptv': float,
            'pte': float,
            'gv0': float,
            'gv1': float,
            'gv2': float,
            'gv3': float
        }

        self.attribute_map = {
            'id': 'id',
            'event_start': 'event_start',
            'event_end': 'event_end',
            'local_player': 'local_player',
            'visitor_player': 'visitor_player',
            'category': 'category',
            'rlf': 'rlf',
            'rfv': 'rfv',
            'rfe': 'rfe',
            'ptl': 'ptl',
            'ptv': 'ptv',
            'pte': 'pte',
            'gv0': 'gv0',
            'gv1': 'gv1',
            'gv2': 'gv2',
            'gv3': 'gv3'
        }
        self._id = id
        self._event_start = event_start
        self._event_end = event_end
        self._local_player = local_player
        self._visitor_player = visitor_player
        self._category = category
        self._rlf = rlf
        self._rfv = rfv
        self._rfe = rfe
        self._ptl = ptl
        self._ptv = ptv
        self._pte = pte
        self._gv0 = gv0
        self._gv1 = gv1
        self._gv2 = gv2
        self._gv3 = gv3

    @classmethod
    def from_dict(cls, dikt) -> 'Event':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Event of this Event.  # noqa: E501
        :rtype: Event
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Event.


        :return: The id of this Event.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Event.


        :param id: The id of this Event.
        :type id: str
        """

        self._id = id

    @property
    def event_start(self) -> str:
        """Gets the event_start of this Event.


        :return: The event_start of this Event.
        :rtype: str
        """
        return self._event_start

    @event_start.setter
    def event_start(self, event_start: str):
        """Sets the event_start of this Event.


        :param event_start: The event_start of this Event.
        :type event_start: str
        """

        self._event_start = event_start

    @property
    def event_end(self) -> str:
        """Gets the event_end of this Event.


        :return: The event_end of this Event.
        :rtype: str
        """
        return self._event_end

    @event_end.setter
    def event_end(self, event_end: str):
        """Sets the event_end of this Event.


        :param event_end: The event_end of this Event.
        :type event_end: str
        """

        self._event_end = event_end

    @property
    def local_player(self) -> str:
        """Gets the local_player of this Event.


        :return: The local_player of this Event.
        :rtype: str
        """
        return self._local_player

    @local_player.setter
    def local_player(self, local_player: str):
        """Sets the local_player of this Event.


        :param local_player: The local_player of this Event.
        :type local_player: str
        """

        self._local_player = local_player

    @property
    def visitor_player(self) -> str:
        """Gets the visitor_player of this Event.


        :return: The visitor_player of this Event.
        :rtype: str
        """
        return self._visitor_player

    @visitor_player.setter
    def visitor_player(self, visitor_player: str):
        """Sets the visitor_player of this Event.


        :param visitor_player: The visitor_player of this Event.
        :type visitor_player: str
        """

        self._visitor_player = visitor_player

    @property
    def category(self) -> str:
        """Gets the category of this Event.


        :return: The category of this Event.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category: str):
        """Sets the category of this Event.


        :param category: The category of this Event.
        :type category: str
        """

        self._category = category

    @property
    def rlf(self) -> float:
        """Gets the rlf of this Event.


        :return: The rlf of this Event.
        :rtype: float
        """
        return self._rlf

    @rlf.setter
    def rlf(self, rlf: float):
        """Sets the rlf of this Event.


        :param rlf: The rlf of this Event.
        :type rlf: float
        """

        self._rlf = rlf

    @property
    def rfv(self) -> float:
        """Gets the rfv of this Event.


        :return: The rfv of this Event.
        :rtype: float
        """
        return self._rfv

    @rfv.setter
    def rfv(self, rfv: float):
        """Sets the rfv of this Event.


        :param rfv: The rfv of this Event.
        :type rfv: float
        """

        self._rfv = rfv

    @property
    def rfe(self) -> float:
        """Gets the rfe of this Event.


        :return: The rfe of this Event.
        :rtype: float
        """
        return self._rfe

    @rfe.setter
    def rfe(self, rfe: float):
        """Sets the rfe of this Event.


        :param rfe: The rfe of this Event.
        :type rfe: float
        """

        self._rfe = rfe

    @property
    def ptl(self) -> float:
        """Gets the ptl of this Event.


        :return: The ptl of this Event.
        :rtype: float
        """
        return self._ptl

    @ptl.setter
    def ptl(self, ptl: float):
        """Sets the ptl of this Event.


        :param ptl: The ptl of this Event.
        :type ptl: float
        """

        self._ptl = ptl

    @property
    def ptv(self) -> float:
        """Gets the ptv of this Event.


        :return: The ptv of this Event.
        :rtype: float
        """
        return self._ptv

    @ptv.setter
    def ptv(self, ptv: float):
        """Sets the ptv of this Event.


        :param ptv: The ptv of this Event.
        :type ptv: float
        """

        self._ptv = ptv

    @property
    def pte(self) -> float:
        """Gets the pte of this Event.


        :return: The pte of this Event.
        :rtype: float
        """
        return self._pte

    @pte.setter
    def pte(self, pte: float):
        """Sets the pte of this Event.


        :param pte: The pte of this Event.
        :type pte: float
        """

        self._pte = pte

    @property
    def gv0(self) -> float:
        """Gets the gv0 of this Event.


        :return: The gv0 of this Event.
        :rtype: float
        """
        return self._gv0

    @gv0.setter
    def gv0(self, gv0: float):
        """Sets the gv0 of this Event.


        :param gv0: The gv0 of this Event.
        :type gv0: float
        """

        self._gv0 = gv0

    @property
    def gv1(self) -> float:
        """Gets the gv1 of this Event.


        :return: The gv1 of this Event.
        :rtype: float
        """
        return self._gv1

    @gv1.setter
    def gv1(self, gv1: float):
        """Sets the gv1 of this Event.


        :param gv1: The gv1 of this Event.
        :type gv1: float
        """

        self._gv1 = gv1

    @property
    def gv2(self) -> float:
        """Gets the gv2 of this Event.


        :return: The gv2 of this Event.
        :rtype: float
        """
        return self._gv2

    @gv2.setter
    def gv2(self, gv2: float):
        """Sets the gv2 of this Event.


        :param gv2: The gv2 of this Event.
        :type gv2: float
        """

        self._gv2 = gv2

    @property
    def gv3(self) -> float:
        """Gets the gv3 of this Event.


        :return: The gv3 of this Event.
        :rtype: float
        """
        return self._gv3

    @gv3.setter
    def gv3(self, gv3: float):
        """Sets the gv3 of this Event.


        :param gv3: The gv3 of this Event.
        :type gv3: float
        """

        self._gv3 = gv3