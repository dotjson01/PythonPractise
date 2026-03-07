def chai_customer():                                                                                 # somebody is asking about chai
    print("Welome ! Which chai would you like")                                                      # printing the statement only  
    order = yield                                                                                    # someone giving a order and that order coming from yield and storing the yield into variable name -> (order)
    while True:                                                                                      # always true loop
        print(f"Preparing {order}")                                                                  #  printing the statement of above order 
        order = yield                                                                                # why again ?  if again new orders comes , in this the new order in not there so yield stop


stall = chai_customer()                                                                              # storing the chai reference
next(stall)                                                                                          # starting point of generator and sending to yield

stall.send("Masala Chai")                                                                            # sending to stall 
stall.send("Lemon Chai ")                                                                         


# if yield does not recieve anything it will stop the program
# print("Welome ! Which chai would you like") 
