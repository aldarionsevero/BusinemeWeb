# -*- coding: utf-8 -*-
from api.busline import BuslineAPI
from api.models.busline import Busline
from api.models.company import Company
from api.models.terminal import Terminal
from exception.api import ApiException
from django.test import SimpleTestCase
from mock import Mock
from mock import patch


class testBusilineAPI(SimpleTestCase):

    """docstring for testBusilineAPI"""

    def setUp(self):
        self.api = BuslineAPI()

        self.buslines = [
            self.create_busline(),
            self.create_busline(line_number="002"),
            self.create_busline(line_number="003")]

    @patch('api.busline.requests.get')
    def test_all(self, mock_get):
        mock_response = Mock()
        expected = {"meta": {"limit": 1000, "next": "null", "offset": 0, "previous": "null", "total_count": 1}, "objects": [{"company": {"id": 26, "name": "VIAÃ‡ÃƒO SATÃ‰LITE", "resource_uri": "/api/v1/company/26"}, "description": "Gama Oeste/\"M\" Norte (Comercial)", "fee": 3.0, "id": 613, "line_number": "205.1", "resource_uri": "/api/v1/busline/613", "route_size": 45.31, "terminals": [
            {"address": "null", "description": "SETOR M NORTE", "id": 15, "resource_uri": "/api/v1/terminal/15"}, {"address": "null", "description": "GAMA", "id": 28, "resource_uri": "/api/v1/terminal/28"}], "via": "VIA ACES. HRG/OESTE - GAMA"}]}
        mock_response.json.return_value = expected
        mock_get.return_value = mock_response

        all_url = "http://localhost:8080/api/v1/busline/"

        all_buslines = self.api.all()

        mock_get.assert_called_once_with(all_url)
        mock_response.json.assert_called_once()

    def create_busline(self, line_number="001", description="Test description",
                       via="Via someplace", route_size=0.0, fee=0.0, company=None,
                       terminals=[]):
        busline = Busline()
        busline.line_number = line_number
        busline.description = description
        busline.via = via
        busline.route_size = route_size
        busline.fee = fee
        busline.company = company
        busline.terminals = terminals
        return busline
