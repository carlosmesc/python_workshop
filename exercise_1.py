#-*- coding: utf-8 -*-

# Python Exercise 1
# Date: 1st of February
# Author: Carlos Javier Martin Escabia
# Python Workshop (Cisco Engineer Incubator Program)

# LIBRARIES
import ipaddress
import collections
import re
import sys

# HELPFUL FUNCTIONS

# Converts a decimal number into binary

def dec2bin(dec):

    bin = ''
    while dec // 2 != 0:
        bin = str(dec % 2) + bin
        dec = dec // 2
    return str(dec) + bin

# Exercise 1

def exercise_1():

	while True:
		ip_address_ = raw_input("Enter IP address: ")
		try:
			ip_address_ = unicode(ip_address_, "utf-8") # Changes the string's format according to the library
			ip_address_ = ipaddress.ip_address(ip_address_)
			break
		except ValueError:
			print("Invalid IP address format")

	while True:
		try:
			subnet_mask = raw_input("Enter subnet mask in decimal format: ")
			mask = int(subnet_mask[1:])
			if ((subnet_mask[0] != '/') or (mask < 0) or (mask > 32)):
				raise	# If the mask is incorrect, an exception is thrown
			break
		except:
			print("Subnet mask is invalid")

	ip_division = str(ip_address_).split(".") # Divides the IP address string in four octects
	binary_mask = list() # Defines a list to save the binary mask

	for j in range(32):
		value = int(j < mask) 
		binary_mask.append(str(value))

	byte1_mask = binary_mask[0:8]
	byte2_mask = binary_mask[8:16]
	byte3_mask = binary_mask[16:24]
	byte4_mask = binary_mask[24:32]

	# Prints the decimal value of each octect

	b1 = ip_division[0]
	b2 = ip_division[1]
	b3 = ip_division[2]
	b4 = ip_division[3]

	# Creates the IP final string

	byte1 = int(b1) & int(''.join(byte1_mask),2)
	byte2 = int(b2) & int(''.join(byte2_mask),2)
	byte3 = int(b3) & int(''.join(byte3_mask),2)
	byte4 = int(b4) & int(''.join(byte4_mask),2)

	final_address = str(byte1) + "." + str(byte2) + "." + str(byte3) + "." + str(byte4) + subnet_mask
	final_address = unicode(final_address, "utf-8") # Changes the string's format according to the library
	final_address = ipaddress.ip_network(final_address) # Gets the IP address

	# Prints the binary value of each octect

	final_bin_table = [] # Saves the final binary value of each octect (1 byte = 8 bits)

	for index in range (4):
		bin_table = list() # Saves the binary value of each octect
		bin_len = len(str(dec2bin(int(ip_division[index])))) # Binary value's lenght
		zeros = 8-bin_len; # Numbers of 0's to fill the bin_table
		for i in range (zeros):
			bin_table.append("0") # Completes the table with 0's if neccesary until reaching 8 bits
		bin_table.append(str(dec2bin(int(ip_division[index]))))
		result = ''
		for x in bin_table:
	  		result = result+''.join(x)
		final_bin_table.append(str(result))

	# Prints the result

	print("  " + str(b1) + "         " + str(b2) + "       " + str(b3) + "       " + str(b4))
	print(str(final_bin_table[0]) + " " + str(final_bin_table[1]) + " " + str(final_bin_table[2]) + " " + str(final_bin_table[3]))
	print("Network Address is: " + str(final_address.network_address)) # Gets the network address
	print("Broadcast Address is: " + str(final_address.broadcast_address)) # Gets the broadcast address


# Calls the function

exercise_1()