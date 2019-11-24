#File: JennyOrderReceiptArray.py

#Project: CSIS2101 - ASSIGNMENT 10(final)

#Author: Jenny P. Nguyen

#History: November 24th, 2019


import Item

def main():

    dTotalPrice = 0.0         
    iTotalWeight = 0
    
    # Put the 4 items being ordered in item1 through item 4         
    item1 = Item.Item(24.99, 14, "Wireless Mouse")         
    item2 = Item.Item(22.49, 27, "USB Keyboard")         
    item3 = Item.Item(24.99, 12, "HDMI Cable")         
    item4 = Item.Item(7.99, 7, "Reading Glasses")         
    item4.set_quantity(2);   
		
    # Show the details of the order using show()         
    print("Here are your shopping cart contents. \n")         

    listTotal = [item1, item2, item3, item4]
    
		
    # Compute the total price and total weight in this section using FOR LOOP

    

    for item in listTotal:

        print(item1)
        print(item2)
        print(item3)
        print(item4)


        dTotalPrice += item.getOrderPrice()     
        iTotalWeight += item.getOrderWeightInOunces()
        
        print("The total price of your order is $" + str(dTotalPrice));
        print("The total shipping weight is", (int)(iTotalWeight / 16),
              "pounds", iTotalWeight % 16 , "ounces");
        print("\n")

main()



