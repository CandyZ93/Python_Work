#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_city_country.py


if __name__ == '__main__':
    import unittest
    from city_functions import city_info
    
    class CitiesTestCase(unittest.TestCase):
        """测试city_functions.py"""
        
        def test_city_country(self):#记住括号里的self
            """能够正确的处理像Wuhan, China这样的城市名吗？"""
            '''neat_name = city_neatname('wuhan', 'china')
            self.assertEqual(neat_name, 'Wuhan, China')'''
            city_info1 = city_info('santigo', 'chile')
            #self.assertEqual(city_info1, 'Santigo, Chile')
            
        def  test_city_country_population(self):#记住括号里的self
            """能够正确处理像Wuhan, China - population 10000000这样的信息吗"""
            city_info2 = city_info('wuhan', 'china', 10000000)
            self.assertEqual(city_info2, 'Wuhan, China - population 10000000')
                        
    unittest.main()#don't forget this part unittest.main()
    

