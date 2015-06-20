from models.terminal import Terminal
from django.conf import settings
from exception.api import ApiException
import requests
import json


class TerminalAPI(object):
    def all(self):
        url = settings.API_URL + 'terminal/?limit=0'
        return self._get_filtered_list(url)

    def _get_filtered_list(self, url):
        r"""
        Load the json returned by the requisition and then ruturns the objects.
        """
        try:
            terminals = requests.get(url)
            return self._terminals_list(terminals.json())
        except Exception, e:
            print e
            raise ApiException(str(e))

    def _json_to_object(self, terminal_json):
        """Parse the terminal, inside the json, to object."""

        terminal = Terminal()
        for attribute in terminal_json.keys():
            setattr(terminal, attribute, terminal_json[attribute])
        return terminal

    def _terminals_list(self, terminals_json):
        r"""
        Parse the terminals, inside the json, to objects (plural), since\
        its a list.
        """
        terminals_list = []
        for terminals in terminals_json["objects"]:
            terminals_list.append(self._json_to_object(terminals))

        return terminals_list
