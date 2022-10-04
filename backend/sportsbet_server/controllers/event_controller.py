import connexion
import six

from sportsbet_server import util


def get_events():  # noqa: E501
    """Returns events available to bet on

    list of events # noqa: E501


    :rtype: Dict[str, int]
    """
    events = [
        { "category": "Futbol de Chile - Primera Division", "event_end": "2020-08-01 08:50", "event_start": "2020-08-01 08:50", "gv0": 1.2, "gv1": 1.2, "gv2": 1.2, "gv3": 1.2, "id": "07cb3c2c-b40c-472f-b05c-7168ac4327e0", "local_player": "U. de Chile", "pte": 1.2, "ptl": 1.2, "ptv": 1.2, "rfe": 1.2, "rfv": 1.2, "rlf": 1.2, "visitor_player": "U. de Chile" },
        { "category": "Futbol de Chile - Primera Division", "event_end": "2020-08-01 08:50", "event_start": "2020-08-01 08:50", "gv0": 1.2, "gv1": 1.2, "gv2": 1.2, "gv3": 1.2, "id": "07cb3c2c-b40c-472f-b05c-7168ac4327e0", "local_player": "U. de Chile", "pte": 1.2, "ptl": 1.2, "ptv": 1.2, "rfe": 1.2, "rfv": 1.2, "rlf": 1.2, "visitor_player": "U. de Chile" },
        { "category": "Futbol de Chile - Primera Division", "event_end": "2020-08-01 08:50", "event_start": "2020-08-01 08:50", "gv0": 1.2, "gv1": 1.2, "gv2": 1.2, "gv3": 1.2, "id": "07cb3c2c-b40c-472f-b05c-7168ac4327e0", "local_player": "U. de Chile", "pte": 1.2, "ptl": 1.2, "ptv": 1.2, "rfe": 1.2, "rfv": 1.2, "rlf": 1.2, "visitor_player": "U. de Chile" }
    ]
    return events
