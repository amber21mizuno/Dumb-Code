#File: Item.py

#Project: CSIS2101 - ASSIGNMENT 10(final)

#Author: Jenny P. Nguyen

#History: November 24th, 2019


class Item:

    #define the four private variables so it sets in the data attribute
    def __init__(self, pr, wio, desc):
        self.__price = pr
        self.__weight_in_oz = wio
        self.__description = desc
        self.__quantity = 1

    #get functions

    def get_price(self):
        return self.__price
    
    def get_weight_in_oz(self):
        return self.__weight_in_oz
    
    def get_description(self):
        return self.__description

    def get_quantity(self):
        return self.__quantity

    #set functions

    def set_price(self, pr):
        self.__price = pr

    def set_weight_in_oz(self, wio):
        self.__weight_in_oz = wio

    def set_description(self,desc):
        self.__description = desc

    def set_quantity(self, qty):
        self.__quantity = qty

    #functions to get the total Order Cost and the total Weight

    def getOrderPrice(self):
        orPr = (self.__quantity * self.__price)
        return orPr
    def getOrderWeightInOunces(self):
        orWIO = (self.__quantity * self.__weight_in_oz)
        return orWIO

    # __str__ function

    def __str__(self):

        totalStr = ""
        totalStr += str(self.__price) + " each for " + str(self.__quantity) + " " + (self.__description) + "\n"

        return totalStr
        
        
