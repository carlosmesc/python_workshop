#-*- coding: utf-8 -*-

# Python Exercise 3
# Date: 1st of February
# Author: Carlos Javier Martin Escabia
# Python Workshop (Cisco Engineer Incubator Program)

# LIBRARIES
import ipaddress
import collections
import re
import sys

# Exercise 3

def exercise_3(file = 'ShowIpRoute_path'):

	regex = re.compile(r'(?P<Pro>\D.*) (?P<Pre>\b\d[\d|\.]+\d\b) (?P<A_D>.*) via (?P<Next_hop>\b\d[\d|\.]+\d\b).* (?P<L_U>\b\d[\d|\:]+\d\b), (?P<O_int>.*)')
	output = {'L':'local','C':'connected','S':'static','R':'RIP','M':'mobile','B':'BGP',
			  'D':'EIGRP','EX':'EIGRP external','O':'OSPF','IA':'OSPF inter area',
       		  'N1':'OSPF NSSA external type 1','N2':'OSPF NSSA external type 2',
      		  'O E1':'OSPF external type 1','O E2':'OSPF external type 2','E':'EGP',
      		  'i':'IS-IS','su':'IS-IS summary','i L1':'IS-IS level-1','i L2':'IS-IS level-2',
       		  'ia':'IS-IS inter area','*':'candidate default','U':'per-user static route',
       		  'o':'ODR','P':'periodic downloaded static route','H':'NHRP','l':'LISP',
       		  'a':'application route','+':'replicated route','%':'next hop override'}

	try:
		text = open(file, 'r') # Reads the ShowIpRoute.txt
		line = 0 # Number of lines
		while True:
			new_line = text.readline() # Reads each line
			if (new_line == ''):
				break
			match = regex.match(new_line) # Looks for matches
			if(match):
				line = line + 1 
				print "LINE " + str(line) # Results for each line
				print "Protocol: \t\t" + output[match.group('Pro')]
				print "Prefix: \t\t" + match.group('Pre')
				print "AD/Metric: \t\t" + match.group('A_D')
				print "Next-Hop: \t\t" + match.group('Next_hop')
				print "Last-Update: \t\t" + match.group('L_U')
				print "Outbound interface: \t" + match.group('O_int') + "\n"

	except IOError:
		print "Can not find the txt file"

	text.close() # Closes the file


# Calls the functions

exercise_3('ShowIpRoute.txt')