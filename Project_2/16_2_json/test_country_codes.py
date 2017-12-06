#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_country_codes.py

import unittest
from country_codes import get_country_code

class CCTestCase(unittest.TestCase):
    """测试country_code中获取国别码的方法"""
    
    def setUp(self):
        """创建一组国家和应返回的国别码，供测试使用"""
        self.country_list = ['Andorra', 'United Arab Emirates', 'Afghanistan', 
        'China']
        self.cc_list = ['ad', 'ae', 'af', 'cn']
    
    def test_CC(self):
        """能正确返回这些国别码吗？"""
        for country,cc in zip(self.country_list, self.cc_list):
            CC = get_country_code(country)
            self.assertEqual(CC, cc)
    

if __name__ == '__main__':
    unittest.main()
