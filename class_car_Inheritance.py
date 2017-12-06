#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  car_class.py
class Car():
    """一次模拟汽车的简单尝试"""
    
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gastank = 0
        
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
        
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    ##2.Using method to change the attribute
    def update_odometer(self, mileage):
        """将里程表读数设定为指定的值
            禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    ##3.Using method to increase attribute
    def increment_odometer(self, miles):
        """将里程表读数增加指定的值"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("Miles must be positive!")
    
    def fill_gas_tank(self, percentage):
        """将邮箱加满到指定百分比"""
        if percentage >= self.gastank:
            self.gastank = percentage
        else:
            print("You have more gas the you thought.")

###将实例用作属性###
class Battery():
    """一次模拟电动汽车电池的简单尝试"""
    
    def __init__(self, battery_size=70):
        """初始化电池的属性"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """打印一条描述电池容量的信息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")
        
    def get_range(self):
        """打印一条消息, 指出电池的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
        
    def upgrade_battery(self):
        if self.battery_size <= 85:
            self.battery_size = 85
        

class ElectricCar(Car):
    """电动汽车的独特之处"""
    
    def __init__(self, make, model, year):
        """初始化父类的属性, 再初始化电动汽车的特有属性"""
        super().__init__(make, model, year)
        #self.battery_size = 70
        self.battery = Battery()
        
        '''      
    def describe_battery(self):
        """打印一条描述电池容量的信息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")
        '''
        
                
    def fill_gas_tank(self,no):
        """电动车没有油箱"""
        print("This car doesn't need a gas tank!")
        

if __name__ == '__main__':
    '''
    my_new_car = Car('audi', 'a4', 2016)
    
    print(my_new_car.get_descriptive_name())
    
    #Change the value of attribute
    ##1.Change it directly
    
    my_new_car.odometer_reading = 23
    
    ##1
    
    ###2
    
    my_new_car.update_odometer(22)
    my_new_car.read_odometer()
    
    my_new_car.update_odometer(222)
    my_new_car.read_odometer()
    
    my_new_car.update_odometer(25)
    my_new_car.read_odometer()
    
    ###2
    
    ###3
    my_used_car = Car('subaru', 'outback', 2013)
    print(my_used_car.get_descriptive_name())
    
    my_used_car.update_odometer(23500)
    my_used_car.read_odometer()
    
    my_used_car.increment_odometer(100)
    my_used_car.read_odometer()
    print("\n" + my_used_car.model.title() + "'s tank is " +
    str(my_used_car.gastank) + "% full.")
    my_used_car.fill_gas_tank(80)
    print("\n" + my_used_car.model.title() + "'s tank is " +
    str(my_used_car.gastank) + "% full.")
    my_used_car.fill_gas_tank(60)
    print()
    '''
        
    my_tesla = ElectricCar('tesla', 'model s', 2016)
    print(my_tesla.get_descriptive_name())
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()
    my_tesla.battery.upgrade_battery()
    my_tesla.battery.get_range()
    
    '''my_tesla.battery.battery_size = 85
    my_tesla.battery.get_range()
    my_tesla.fill_gas_tank(80)
    '''
    
