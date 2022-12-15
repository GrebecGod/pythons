from datetime import datetime
import re
from tkinter import N

class Nigga:

    raise_amount=1.04
    num_of_slaves=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        Nigga.num_of_slaves+=1
    @property
    def email(self):
        return'{}.{}@gmail.com '.format(self.first, self.last)
    def fullname(self):
        return'{} {} '.format(self.first, self.last)
    #@fullname.setter
    #def fullname(self,name):
        #first,last=name.split(' ')
        #self.first=first
        #self.last=last
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount=amount
    @classmethod
    def from_string(cls, nig_str):
        first, last, pay=nig_str.split('-')
        return cls(first, last, pay)
    @staticmethod
    def isworkday(day):
        if day.weekday()==6 or day.weekday()==7:
            return False
        return True
    def __repr__(self):
        return "Nigga('{}', '{}', '{}')".format(self.first, self.last, self.pay)
    def __str__(self) -> str:
        return '{} - {}'.format(self.fullname(), self.email)
    def __add__(self,other):
        return self.pay+other.pay
class Developer(Nigga):
    raise_amount=1.10

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang
class Manager(Nigga):

     def __init__(self,first,last,pay,niggers=None):
        super().__init__(first,last,pay)
        if niggers==None:
            self.niggers=[]
        else :
            self.niggers=niggers
     def add_nig(self,nig):
        if nig not in self.niggers:
            self.niggers.append(nig)
     def remove_nig(self,nig):
        if nig in self.niggers:
            self.niggers.remove(nig)
     def print_emps(self):
         for nig in self.niggers:
             print('-->', nig.fullname())


         

#print(Nigga.num_of_slaves)
dev_1=Nigga("Correy", "Bens", 5000,)
dev_2=Nigga("Test", "Nigger", 911,)
mgr_1=Manager("Sue","Smith",69000,[dev_1])

dev_1.first="Nigger"
dev_1.fullname="Osama Laden"
print(dev_1.first)
print(dev_1.email)
print(dev_1.fullname())
"""""
mgr_1.print_emps()
mgr_1.add_nig(dev_2)
mgr_1.print_emps()
mgr_1.remove_nig(dev_1)
mgr_1.print_emps()
print(dev_1.email)
print(dev_1.pay)

import datetime
my_date=datetime.date(2022,6,24)
print(Nigga.isworkday(my_date))

nig_str_1='John-Doe-70000'
nig_str_2='Steve-Smith-80000'
nig_str_3='Osama-Laden-91100'

first, last, pay=nig_str_1.split('-')

new_emp_1=Nigga.from_string(nig_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)

Nigga.set_raise_amount(1.05)
print(nig_1.pay)
nig_1.apply_raise()
print(nig_1.pay)
nig_1.raise_amount=1.05
print(nig_1.pay)
print(nig_1.raise_amount)
print(Nigga.raise_amount)
print(nig_1.raise_amount)
print(nig_2.raise_amount)
print(Nigga.num_of_slaves)

"""
print("Veritas Temporis")



