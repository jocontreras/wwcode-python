""" The Challenge
Author: Jennifer Contreras
Description: Aling Nena’s Sari-sari store wants a robot that will ask the
customer their total bill and payment amount and tell them their change
(for now, we can allow negative change).
"""
total_bill = input('How much is your total bill? ')

payment = input('How much is your payment? ')

change = float(payment)- float(total_bill)

print("Hi! Your change is %.2f" % change )
