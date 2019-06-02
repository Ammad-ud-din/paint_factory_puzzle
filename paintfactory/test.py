#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Paint Factory Puzzle
# Author: mu.ammad.ud.din@gmail.com
# Last Update: 09 March 2019
# License: MIT



import os
import unittest
from unittest import TestCase

from order_services.customer_order import CustomerOrder
from delivery_services.delivery_order import deliverOrder
from paintmaker.paint_maker import PaintMaker

class TestPaintMaker(TestCase):
    
    def test_demo_order(self):
        
        orderLocation = os.path.join("orders", "demo_order.txt")
        customerOrder = CustomerOrder(orderLocation)
        orders = customerOrder.analyzeCustomerOrders()
        paintMaker = PaintMaker(orders)
        report = paintMaker.executeOrders()
        groundTruth = ["Case #1: 1 0 0 0 0",
                      "Case #2: IMPOSSIBLE"]

        self.assertEqual(deliverOrder(report[0][0], report[0][1], report[0][2]), groundTruth[0])
        self.assertEqual(deliverOrder(report[1][0], report[1][1], report[1][2]), groundTruth[1])
        
    
    def test_order1(self):
        
        orderLocation = os.path.join("orders", "order1.txt")
        customerOrder = CustomerOrder(orderLocation)
        orders = customerOrder.analyzeCustomerOrders()
        paintMaker = PaintMaker(orders)
        report = paintMaker.executeOrders()[0]
        groundTruth = "Case #1: 0 0"

        self.assertEqual(deliverOrder(report[0], report[1], report[2]), groundTruth)
        
        
    def test_order2(self):
        
        orderLocation = os.path.join("orders", "order2.txt")
        customerOrder = CustomerOrder(orderLocation)
        orders = customerOrder.analyzeCustomerOrders()
        paintMaker = PaintMaker(orders)
        report = paintMaker.executeOrders()[0]
        groundTruth = "Case #1: 1 0 1 0 0"

        self.assertEqual(deliverOrder(report[0], report[1], report[2]), groundTruth)

    
    def test_order3(self):
        
        orderLocation = os.path.join("orders", "order3.txt")
        customerOrder = CustomerOrder(orderLocation)
        orders = customerOrder.analyzeCustomerOrders()
        paintMaker = PaintMaker(orders)
        report = paintMaker.executeOrders()[0]
        groundTruth = "Case #1: 1 1 1"

        self.assertEqual(deliverOrder(report[0], report[1], report[2]), groundTruth)

    def test_order4(self):
        
        orderLocation = os.path.join("orders", "order4.txt")
        customerOrder = CustomerOrder(orderLocation)
        orders = customerOrder.analyzeCustomerOrders()
        paintMaker = PaintMaker(orders)
        report = paintMaker.executeOrders()[0]
        groundTruth = "Case #1: IMPOSSIBLE"

        self.assertEqual(deliverOrder(report[0], report[1], report[2]), groundTruth)
        
    def test_order5(self):
        
        orderLocation = os.path.join("orders", "order5.txt")
        customerOrder = CustomerOrder(orderLocation)
        orders = customerOrder.analyzeCustomerOrders()
        paintMaker = PaintMaker(orders)
        report = paintMaker.executeOrders()[0]
        groundTruth = "Case #1: 0 0 0 0 1"

        self.assertEqual(deliverOrder(report[0], report[1], report[2]), groundTruth)
        
    def test_order6(self):
        
        orderLocation = os.path.join("orders", "order6.txt")
        customerOrder = CustomerOrder(orderLocation)
        orders = customerOrder.analyzeCustomerOrders()
        paintMaker = PaintMaker(orders)
        report = paintMaker.executeOrders()[0]
        groundTruth = "Case #1: 0 0 1"

        self.assertEqual(deliverOrder(report[0], report[1], report[2]), groundTruth)
        
    def test_order7(self):
        
        orderLocation = os.path.join("orders", "order7.txt")
        customerOrder = CustomerOrder(orderLocation)
        orders = customerOrder.analyzeCustomerOrders()
        paintMaker = PaintMaker(orders)
        report = paintMaker.executeOrders()
        groundTruth = ["Case #1: 0 0 0 0 0",
                      "Case #2: IMPOSSIBLE"]

        self.assertEqual(deliverOrder(report[0][0], report[0][1], report[0][2]), groundTruth[0])
        self.assertEqual(deliverOrder(report[1][0], report[1][1], report[1][2]), groundTruth[1])

    def test_order8(self):
        
        orderLocation = os.path.join("orders", "order8.txt")
        customerOrder = CustomerOrder(orderLocation)
        orders = customerOrder.analyzeCustomerOrders()
        paintMaker = PaintMaker(orders)
        report = paintMaker.executeOrders()
        groundTruth = ["Case #1: 1 0 0 0 0",
                      "Case #2: IMPOSSIBLE",
                      "Case #3: 1 1 1 0 0",
                      "Case #4: 1",
                      "Case #5: 1 0 1 0 0",
                      "Case #6: IMPOSSIBLE",
                      "Case #7: 1 0 0 0 0",
                      "Case #8: 0 0 0 0",
                      "Case #9: 0 1 0 0 0",
                      "Case #10: 1 1 0"]

        self.assertEqual(deliverOrder(report[0][0], report[0][1], report[0][2]), groundTruth[0])
        self.assertEqual(deliverOrder(report[1][0], report[1][1], report[1][2]), groundTruth[1])
        self.assertEqual(deliverOrder(report[2][0], report[2][1], report[2][2]), groundTruth[2])
        self.assertEqual(deliverOrder(report[3][0], report[3][1], report[3][2]), groundTruth[3])
        self.assertEqual(deliverOrder(report[4][0], report[4][1], report[4][2]), groundTruth[4])
        self.assertEqual(deliverOrder(report[5][0], report[5][1], report[5][2]), groundTruth[5])
        self.assertEqual(deliverOrder(report[6][0], report[6][1], report[6][2]), groundTruth[6])
        self.assertEqual(deliverOrder(report[7][0], report[7][1], report[7][2]), groundTruth[7])
        self.assertEqual(deliverOrder(report[8][0], report[8][1], report[8][2]), groundTruth[8])
        self.assertEqual(deliverOrder(report[9][0], report[9][1], report[9][2]), groundTruth[9])
    

if __name__ == '__main__':
    unittest.main()
