# -*- coding: utf-8 -*-

# from django.test import SimpleTestCase
# from models.busline import Busline
# from models.company import Company
# from models.terminal import Terminal


# class TestBusline(SimpleTestCase):

# 	def test_instance(self):
#         busline = Busline()
#         busline.line_number = '111'
#         busline.description = 'test'
#         busline.via = 'test'
#         busline.route_size = '111'
#         busline.fee = '111'
#         busline.company = ForeignKey('Company')
#         busline.terminals = models.ForeignKey('Terminal')
#         busline.save()
#         self.assertIsNotNone(busline)

# def save_on_db(self):
# db_before = Busline.objects.all()
# busline = Busline()
# busline.line_number = '111'
# busline.description = 'test'
# busline.via = 'test'
# busline.route_size = '111'
# busline.fee = '111'
# busline.company = Company()
# busline.terminals = Terminal()
# busline.save()
# db_after = Busline.objects.all()
# self.assertTrue(db_after != db_before)

#     def test_filter_by_line_number(self):
#         resp = Busline.filter_by_line_number('111')
#         self.assertNotEquals(resp, [])
