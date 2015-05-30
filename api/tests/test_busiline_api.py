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

    @patch('api.busline.requests.get')
    def test_all(self, mock_get):
        mock_get = mock_get
        mock_response = Mock()
        mock_response.json.return_value = self.all_buslines_dict()
        mock_get.return_value = mock_response
        all_url = "http://localhost:8080/api/v1/busline/"

        all_buslines = self.api.all()

        mock_get.assert_called_once_with(all_url)
        mock_response.json.assert_called_once()

    @patch('api.busline.requests.get')
    def test_filter_by_line(self, mock_get):
        mock_get = mock_get
        mock_response = Mock()
        mock_response.json.return_value = self.buslines_by_number()
        mock_get.return_value = mock_response
        all_url = "http://localhost:8080/api/v1/busline/?line_number__contains=17&limit=0"

        all_buslines = self.api.filter_by_line('17')

        mock_get.assert_called_once_with(all_url)
        mock_response.json.assert_called_once()

    @patch('api.busline.requests.get')
    def test_filter_by_description(self, mock_get):
        mock_get = mock_get
        mock_response = Mock()
        mock_response.json.return_value = self.buslines_by_description()
        mock_get.return_value = mock_response
        all_url = "http://localhost:8080/api/v1/busline/?description__contains=setor&limit=0"

        all_buslines = self.api.filter_by_description('setor')

        mock_get.assert_called_once_with(all_url)
        mock_response.json.assert_called_once()

    @patch('api.busline.requests.get')
    def test_filter_by_multiple(self, mock_get):
        mock_get = mock_get
        mock_response = Mock()
        mock_response.json.return_value = self.buslines_by_description()
        mock_get.return_value = mock_response
        all_url = "http://localhost:8080/api/v1/busline/?line_number__contains=917&description__contains=setor&limit=0"

        all_buslines = self.api.filter_by_multiple(
            line_number='917', description='setor')

        mock_get.assert_called_once_with(all_url)
        mock_response.json.assert_called_once()

    def all_buslines_dict(self):
        return {
            "meta": {"limit": 1000, "next": "null", "offset": 0, "previous": "null", "total_count": 6},
            "objects": [
                {"company": {"id": 7, "name": "SÃƒO JOSÃ‰", "resource_uri": "/api/v1/company/7"},
                 "description": "Riacho Fundo/RodoviÃ¡ria do Plano Piloto (Eixo)", "fee": 2.0, "id": 76,
                 "line_number": "0.172", "resource_uri": "/api/v1/busline/76", "route_size": 22.57,
                 "terminals": [
                    {"address": "null", "description": "RIACHO FUNDO",
                        "id": 6, "resource_uri": "/api/v1/terminal/6"},
                    {"address": "null", "description": "RODOVIÃRIA DO PLANO PILOTO",
                        "id": 19, "resource_uri": "/api/v1/terminal/19"}
                ], "via": "AV. RIACHO FUNDO I SUL"},
                {"company": {"id": 7, "name": "SÃƒO JOSÃ‰", "resource_uri": "/api/v1/company/7"},
                 "description": "Riacho Fundo/RodoviÃ¡ria do Plano Piloto  (Eixo)", "fee": 2.0, "id": 557,
                 "line_number": "172.1", "resource_uri": "/api/v1/busline/557", "route_size": 26.48,
                 "terminals": [
                    {"address": "null", "description": "RIACHO FUNDO",
                        "id": 6, "resource_uri": "/api/v1/terminal/6"},
                    {"address": "null", "description": "RODOVIÃRIA DO PLANO PILOTO",
                        "id": 19, "resource_uri": "/api/v1/terminal/19"}
                ], "via": "AV. RIACHO FUNDO I SUL"},
                {"company": {"id": 62, "name": "RÃPIDO BRASILIA", "resource_uri": "/api/v1/company/62"},
                 "description": "Escola Classe 405 Sul/ASTECA (ISM)", "fee": 0.0, "id": 558,
                 "line_number": "172.2", "resource_uri": "/api/v1/busline/558", "route_size": 25.84,
                 "terminals": [
                    {"address": "null", "description": "E.C. 405 SUL",
                        "id": 78, "resource_uri": "/api/v1/terminal/78"},
                    {"address": "null", "description":
                        "ASTECA (ISM)", "id": 129, "resource_uri": "/api/v1/terminal/129"}
                ], "via": "VIA EQS 206/205 COMÃ‰RCIO LOCAL SUL"},
                {"company": {"id": 7, "name": "SÃƒO JOSÃ‰", "resource_uri": "/api/v1/company/7"},
                 "description": "Riacho Fundo/RodoviÃ¡ria do Plano Piloto (Eixo-Noturna)", "fee": 2.0, "id": 559,
                 "line_number": "172.4", "resource_uri": "/api/v1/busline/559", "route_size": 22.57, "terminals": [
                    {"address": "null", "description": "RIACHO FUNDO",
                        "id": 6, "resource_uri": "/api/v1/terminal/6"},
                    {"address": "null", "description": "RODOVIÃRIA DO PLANO PILOTO",
                        "id": 19, "resource_uri": "/api/v1/terminal/19"}
                ], "via": "AV. RIACHO FUNDO I SUL"},
                {"company": {"id": 29, "name": "VIAÃ‡ÃƒO VIVA BRASÃLIA,VIAÃ‡ÃƒO PLANETA", "resource_uri": "/api/v1/company/29"},
                 "description": "Taguatinga Sul/CEET 01/APAED", "fee": 0.0, "id": 151,
                 "line_number": "0.309", "resource_uri": "/api/v1/busline/151", "route_size": 35.08, "terminals": [
                    {"address": "null", "description": "AREAL - QS 10",
                     "id": 37, "resource_uri": "/api/v1/terminal/37"},
                    {"address": "null", "description": "APAED", "id": 59,
                     "resource_uri": "/api/v1/terminal/59"}
                ], "via": "AV. ÃGUAS CLARAS"},
                {"company": {"id": 29, "name": "VIAÃ‡ÃƒO VIVA BRASÃLIA,VIAÃ‡ÃƒO PLANETA", "resource_uri": "/api/v1/company/29"},
                    "description": "APAED/Taguatinga Sul/CEET 01", "fee": 0.0, "id": 690,
                    "line_number": "309.1", "resource_uri": "/api/v1/busline/690", "route_size": 50.6, "terminals": [
                        {"address": "null", "description": "APAED", "id": 59,
                         "resource_uri": "/api/v1/terminal/59"}
                ], "via": "VIA M3 - CEILÃ‚NDIA"},
                {"company": {"id": 10, "name": "VIAÃ‡ÃƒO CIDADE BRASÃLIA", "resource_uri": "/api/v1/company/10"},
                 "description": "Setor \"O\" (via M-2)/SAAN(Estrutural)", "fee": 3.0, "id": 380,
                 "line_number": "0.917", "resource_uri": "/api/v1/busline/380", "route_size": 32.17, "terminals": [
                    {"address": "null", "description": "SETOR \"O\"",
                        "id": 8, "resource_uri": "/api/v1/terminal/8"},
                    {"address": "null", "description": "FINAL DA QUADRA 02 DO SAAN",
                        "id": 117, "resource_uri": "/api/v1/terminal/117"}
                ], "via": "VIA O4 - CEILÃ‚NDIA"}
            ]}

    def buslines_by_number(self):
        return {
            "meta": {"limit": 1000, "next": "null", "offset": 0, "previous": "null", "total_count": 6},
            "objects": [
                {"company": {"id": 7, "name": "SÃƒO JOSÃ‰", "resource_uri": "/api/v1/company/7"},
                 "description": "Riacho Fundo/RodoviÃ¡ria do Plano Piloto (Eixo)", "fee": 2.0, "id": 76,
                 "line_number": "0.172", "resource_uri": "/api/v1/busline/76", "route_size": 22.57,
                 "terminals": [
                    {"address": "null", "description": "RIACHO FUNDO",
                        "id": 6, "resource_uri": "/api/v1/terminal/6"},
                    {"address": "null", "description": "RODOVIÃRIA DO PLANO PILOTO",
                        "id": 19, "resource_uri": "/api/v1/terminal/19"}
                ], "via": "AV. RIACHO FUNDO I SUL"},
                {"company": {"id": 7, "name": "SÃƒO JOSÃ‰", "resource_uri": "/api/v1/company/7"},
                 "description": "Riacho Fundo/RodoviÃ¡ria do Plano Piloto  (Eixo)", "fee": 2.0, "id": 557,
                 "line_number": "172.1", "resource_uri": "/api/v1/busline/557", "route_size": 26.48,
                 "terminals": [
                    {"address": "null", "description": "RIACHO FUNDO",
                        "id": 6, "resource_uri": "/api/v1/terminal/6"},
                    {"address": "null", "description": "RODOVIÃRIA DO PLANO PILOTO",
                        "id": 19, "resource_uri": "/api/v1/terminal/19"}
                ], "via": "AV. RIACHO FUNDO I SUL"},
                {"company": {"id": 62, "name": "RÃPIDO BRASILIA", "resource_uri": "/api/v1/company/62"},
                 "description": "Escola Classe 405 Sul/ASTECA (ISM)", "fee": 0.0, "id": 558,
                 "line_number": "172.2", "resource_uri": "/api/v1/busline/558", "route_size": 25.84,
                 "terminals": [
                    {"address": "null", "description": "E.C. 405 SUL",
                        "id": 78, "resource_uri": "/api/v1/terminal/78"},
                    {"address": "null", "description":
                        "ASTECA (ISM)", "id": 129, "resource_uri": "/api/v1/terminal/129"}
                ], "via": "VIA EQS 206/205 COMÃ‰RCIO LOCAL SUL"},
                {"company": {"id": 7, "name": "SÃƒO JOSÃ‰", "resource_uri": "/api/v1/company/7"},
                 "description": "Riacho Fundo/RodoviÃ¡ria do Plano Piloto (Eixo-Noturna)", "fee": 2.0, "id": 559,
                 "line_number": "172.4", "resource_uri": "/api/v1/busline/559", "route_size": 22.57, "terminals": [
                    {"address": "null", "description": "RIACHO FUNDO",
                        "id": 6, "resource_uri": "/api/v1/terminal/6"},
                    {"address": "null", "description": "RODOVIÃRIA DO PLANO PILOTO",
                        "id": 19, "resource_uri": "/api/v1/terminal/19"}
                ], "via": "AV. RIACHO FUNDO I SUL"}
            ]}

    def buslines_by_description(self):
        return {
            "meta": {"limit": 1000, "next": "null", "offset": 0, "previous": "null", "total_count": 6},
            "objects": [
                {"company": {"id": 10, "name": "VIAÃ‡ÃƒO CIDADE BRASÃLIA", "resource_uri": "/api/v1/company/10"},
                 "description": "Setor \"O\" (via M-2)/SAAN(Estrutural)", "fee": 3.0, "id": 380,
                 "line_number": "0.917", "resource_uri": "/api/v1/busline/380", "route_size": 32.17, "terminals": [
                    {"address": "null", "description": "SETOR \"O\"",
                        "id": 8, "resource_uri": "/api/v1/terminal/8"},
                    {"address": "null", "description": "FINAL DA QUADRA 02 DO SAAN",
                        "id": 117, "resource_uri": "/api/v1/terminal/117"}
                ], "via": "VIA O4 - CEILÃ‚NDIA"}
            ]}
