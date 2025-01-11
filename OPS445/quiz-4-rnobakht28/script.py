#!/usr/bin/env python3

class ProductStock:
 
    def __init__(self, name, stock):
        self.stock = stock
        self.name = name
        self.in_stock = True



 
    def __sub__(self, amt):
        self.stock -= amt
        print(f'You take {amt} down, and pass it around')
    
    def __str__(self):
       return str(self.stock)  + " bottles of root beer on the wall, " + str(self.stock) + " bottles of root beer"

    def __repr__(self):
        return self.name + " " + str(self.stock) + "x"
    


