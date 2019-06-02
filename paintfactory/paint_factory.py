#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Paint Factory Puzzle
# Author: mu.ammad.ud.din@gmail.com
# Last Update: 09 March 2019
# License: MIT


import sys
from order_services.customer_order import CustomerOrder
from delivery_services.delivery_order import deliverOrder
from paintmaker.paint_maker import PaintMaker

if __name__ == '__main__':

    if len(sys.argv) > 1:
        orderLocation = sys.argv[1]
        customerOrder = CustomerOrder(orderLocation)
        orders = customerOrder.analyzeCustomerOrders()
    else:
        orderLocation = 'orders/demo_order.txt'
        customerOrder = CustomerOrder(orderLocation)
        orders = customerOrder.analyzeCustomerOrders()
    
    if orders is not None:
        paintMaker = PaintMaker(orders)
        deliveryReports = paintMaker.executeOrders()
        
        for report in deliveryReports:
            print(deliverOrder(report[0], report[1], report[2]))
            
            
    