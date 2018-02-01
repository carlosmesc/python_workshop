#-*- coding: utf-8 -*-

# Python Exercise 4
# Date: 1st of February
# Author: Carlos Javier Martin Escabia
# Python Workshop (Cisco Engineer Incubator Program)

# LIBRARIES
import ipaddress
import collections
import re
import sys

# Exercise 4

def exercise_4():
	
	# Templates

	access_template = ['switchport mode access',
                       'switchport access vlan {}',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']

	trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk allowed vlan {}']
	flag = 1
	while flag > 0:
		try:
			if_mode = raw_input("Enter interface mode (access/trunk): ")
			if (if_mode != "access" and if_mode != "trunk"):
				print "Incorrect interface mode"
				flag = 2
			else:
				break
		except ValueError:
			print "Incorrect interface mode"

	if_type_number = raw_input("Enter interface type and number: ")
	if (if_mode == "access"):
		vlan_num = raw_input("Enter VLAN number: ")
		access_temp = access_template
		access_temp[1] = access_temp[1].format(vlan_num)
		print ""
		print "OUTPUT: \n"
		print "Interface " + if_type_number
		for i in access_temp:
			print i

	if (if_mode == "trunk"):
		allow_vlans = raw_input("Enter allowed VLANs: ")
		trunk_temp = trunk_template
		trunk_temp[2] = trunk_temp[2].format(allow_vlans)
		print ""
		print "OUTPUT: \n"
		print "Interface " + if_type_number
		for j in trunk_temp:
			print j

# Calls the function

exercise_4()