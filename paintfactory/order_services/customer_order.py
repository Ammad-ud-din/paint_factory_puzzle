#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Paint Factory Puzzle
# Author: mu.ammad.ud.din@gmail.com
# Last Update: 09 March 2019
# License: MIT


class CustomerOrder(object):
    
    def __init__(self, orderLocation):
        self.orderLocation = orderLocation
        self.orderInfo = None
    
    def readOrderDetails(self):
        
        try: 
            with open(self.orderLocation) as fs:
                self.orderInfo = fs.readlines()
            fs.close()
        except IOError:
            print('Customer Order \"' ,self.orderLocation, '\" not found.\nPlease double-check the order location and name')
        
    
    
    def analyzeCustomerOrders(self):
    
        self.readOrderDetails()
        
        if self.orderInfo is not None:
            
            self.orderInfo = iter(self.orderInfo)
            numOfOrder = int(next(self.orderInfo))
            self.orders = []
        
            for _ in range(numOfOrder):
                obj = {}
        
                
                nPaintColors = int(next(self.orderInfo))
                nCustomers = int(next(self.orderInfo))
        
                obj['nPaintColors'] = nPaintColors
                obj['customers'] = []
        
                for _ in range(nCustomers):
                    self.customer = []
        
                    splitted = str(next(self.orderInfo)).rstrip("\n").split(" ")
                    numOfChoices = int(splitted.pop(0))
        
                    for i in range(numOfChoices):
                        # window size of two
                        color, end = splitted[(i * 2):(i * 2) + 2]
                        self.customer.append((int(color), int(end)))
        
                    obj['customers'].append(self.customer)
        
                self.orders.append(obj)
            
            return self.orders
    
