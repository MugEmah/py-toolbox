# -*- coding: utf-8 -*-
"""
Created on Sat Aug 16 00:15:04 2025

@author: mugee
"""


# f strings
# =============================================================================
# user_name = 'Bob'
# user_age = 10
# user_information = f'{user_name} is {user_age} years old'
# bad_approach = user_name + ' is ' + str(user_age) + ' years old'
# 
# print(user_information)
# =============================================================================

# =============================================================================
# # single line if statements
# user_age = 17
# user_name = 'Bob'
# user_status = 'an adult' if user_age >=18 else 'a child'
# # =============================================================================
# # if user_age < 18:
# #     user_status = 'child'
# # else:
# #     user_status = 'adult'
# # =============================================================================
# print(f'{user_name} is {user_age} years old, and is {user_status}.')
# 
# =============================================================================

# =============================================================================
# # list comprehension
# simple_list = [f'{i}{_}' for _ in range(0, 11,2) for i in ('a','b','c') if i == 'a']
# #for _ in range(0,11,1):
# #    simple_list.append(_)
# print(simple_list)
# =============================================================================

# =============================================================================
# # lambda functions
# #def double_value(num):
# #   return num*2
# double_value = lambda num: num*2
# print(double_value(10))
# 
# #some functions want a function as an argument
# random_list = [('Anna',25),('Bob',40),('Lisa',10)]
# sorted_list = sorted(random_list, key=lambda user_tuple:user_tuple[1])
# 
# print(sorted_list)
# =============================================================================

#exercise
battleship_board =[f'{letter}{num}' for letter in ('A','B','C','D','E') for num in range(1, 6) if f'{letter}{num}'!='C3']
print(battleship_board)








