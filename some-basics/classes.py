# -*- coding: utf-8 -*-
"""
Created on Sat Aug 16 10:18:16 2025

@author: mugee
"""


# =============================================================================
# # a basic class
# class TestClass:
#     test_var = (1,2,3,4)
#     another_var = 'Oh shiit! sumn in the water'
#     def test_func(self):
#         print('function in a class')
#         print(self.test_var)
#     
#     def another_func(self, test_param='test'):
#         print(test_param)
#         
# # create an instance
# test = TestClass()
# test.another_var = 'nothing in the water'
# 
# print(test.test_var)
# print(test.another_var)
# 
# test2 = TestClass()
# print(test2.another_var)
# 
# test.test_var = 'this aint numbers no more'
# print(test.test_var)
# 
# test.test_var = [45,23,65,45,87,97]
# print(test.test_var)
# print(test2.test_var)
# 
# test.test_func()
# test.another_func()
# =============================================================================

# =============================================================================
# # mage class
# class Mage:
#     def __init__(self,health,mana):
#         self.health = health
#         self.mana = mana
#         print('mage class was created')
#         print(self.health)
#         
#     def attack(self,target):
#         target.health -= 10
#     
# class Monster:
#     health = 40
#     
# mage = Mage(100,200)
# monster = Monster()
# 
# print(monster.health)
# mage.attack(monster)
# print(monster.health)
# =============================================================================

# =============================================================================
# # inheritance
# class Human:
#     def __init__(self,health):
#         self.health = health
#     
#     def attack(self):
#         print('attack')
# 
# class Warrior(Human):
#     def __init__(self,health,defense):
#         super().__init__(health)
#         self.defense = defense
# 
# class Barbarian(Human):
#     def __init__(self,health,damage):
#         super().__init__(health)
#         self.damage = damage    
#         
# warrior = Warrior(50,5.5)
# barbarian = Barbarian(100,8.8)
# 
# warrior.attack()
# barbarian.attack()
# 
# print(warrior.health)
# print(barbarian.health)
# =============================================================================

# exercise
class Entity:
    def attack(self):
        print(f'attack with {self.damage} damage')
        
        
class Monster(Entity):
    def __init__(self,health,damage):
        self.health = health
        self.damage = damage
        
    def __repr__(self):
        return f'a monster with {self.health} hp'
        
monster = Monster(100,15)

print(monster.health)
monster.attack()

print(monster)










