#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_Employee_info.py

if __name__ == '__main__':
    import unittest
    from Employee_info import Employee
    
    class TestEmployee(unittest.TestCase):
        """针对Employee类的测试"""
        
        def setUp(self):
            """创建一个雇员实例，供使用的测试方法"""
            self.me = Employee('Lance', 'Zhou', 300000)
            self.incomes = [300000, 305000, 320000]
            
        def test_give_default_raise(self):
            """测试默认的年薪增长"""
            self.me.give_raise()
            self.assertEqual(self.incomes[1], self.me.income)
            
        def test_give_custom_raise(self):
            """测试给定的年薪增长"""
            self.me.give_raise(20000)
            self.assertEqual(self.incomes[2], self.me.income)
            
    unittest.main()
