# -*- coding: utf-8 -*-
"""
Created on Sat Aug 16 00:36:39 2025

@author: mugee
"""


# =============================================================================
# # create a function
# def print_x_times(something, loop_amount=5):
#     counter = 0
#     print(global_var)
#     while counter < loop_amount:
#         print(something)
#         counter += 1
#     return 'Function is running well'
# =============================================================================

# =============================================================================
# # hypotenus calcultor function
# def hypotenus_calc(side_a=1, side_b=1):
# 
# #Calculate the hypotenus using the pythogorus theorem
#     hypotenus = (side_a**2 + side_b**2)**(1/2)
# 
# #Output result
#     return round(hypotenus,2)
# =============================================================================

# exercise
def shout(output_string='hello', repitition_amount=5):
    if repitition_amount > 10:
        print('You\'re a bit too loud')
    else:
        for _ in range(repitition_amount):
            print(output_string.upper())
        
    return 'Done'
    
# =============================================================================
# # call
# print('print')
# global_var = 'This is a global variable'
# test = print_x_times('test', 6)
# =============================================================================
# =============================================================================
# 
# #print(test)
# print(hypotenus_calc(4,3))
# =============================================================================

print(shout('hey there',12)) 