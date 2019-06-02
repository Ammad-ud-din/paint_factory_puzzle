#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Paint Factory Puzzle
# Author: mu.ammad.ud.din@gmail.com
# Last Update: 09 March 2019
# License: MIT


from support_services.utils import compareCustomers, compareChoices, analyzePop, compare_to_key


class PaintMaker(object):
    
    def __init__(self,orders):
        self.orders = orders
        
    def executeOrders(self):
        
        deliveryReports = []
        for i in range(len(self.orders)):
            paint, nPaintColors, customer_id = self.makePaint(self.orders[i], i + 1)
            deliveryReports.append([paint, nPaintColors, customer_id])
            
        return deliveryReports
    
    def makePaint(self,order, customer_id):
        customers = order['customers']
        
        customers = sorted(customers, key=compare_to_key(compareCustomers))
        customers = [sorted(choices, key=compare_to_key(compareChoices)) for choices in customers]

        nPaintColors = order['nPaintColors']
        paint = set()
        stack = []
        backtrack_i = None
    
        
        j = 0
        while j < len(customers):
            
            choices = customers[j]
    
            isCustomerSatisfied = False
    
            
            i = backtrack_i or 0
            backtrack_i = None
            while i < len(choices):
                choice = choices[i]
    
                isPop = analyzePop(choice, paint)
    
                if not isPop:
                    if i == len(choices) - 1:
                        stack.append(i)
                        
                        i += 1
                        isCustomerSatisfied = False
                    else:
                        
                        i += 1
                        continue
                else:
                    
                    isCustomerSatisfied = True
                    paint.add(choice)
                    stack.append(i)
                    break
    
            if not isCustomerSatisfied:
                if [(len(x) - 1) for x in customers][:len(stack)] == stack:
                    paint = None
                    break
                else:
                    for customer_i, choice_i in enumerate(stack):
                        if choice_i < len(customers[customer_i]) - 1 and backtrack_i is None:
                            j = customer_i - 1
                            backtrack_i = choice_i + 1
                            stack = stack[:customer_i]
                        if backtrack_i is not None:
                            try:
                                paint.remove(customers[customer_i][choice_i])
                            except KeyError:
                                pass
    
            j += 1
        
        return paint, nPaintColors, customer_id

    
    
    