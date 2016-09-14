#!/usr/bin/env python
# coding:utf-8


from selenium import webdriver
import unittest, warnings


class NewVisitiorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()
	
	def test_can_start_a_list_and_retrieve_it_later(self):

		self.browser.get('httP://localhost:8000')

		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

if __name__ == '__main__':
	with warnings.catch_warnings(record=True):
		unittest.main()