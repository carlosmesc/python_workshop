#-*- coding: utf-8 -*-

# Python Exercise 2
# Date: 1st of February
# Author: Carlos Javier Martin Escabia
# Python Workshop (Cisco Engineer Incubator Program)

# LIBRARIES
import ipaddress
import collections
import re
import sys

# Exercise 2

def exercise_2(file = 'commands_path'):
	
	try:
		text = open(file, 'r') # Reads the commands.txt
		i = 0
		text_list = list() # Saves the matches

		while True:
			new_line = text.readline() # Reads a line in each iteration
			if (new_line == ''):
				break
			m = re.search(r'(?:^switchport\s+trunk\s+allowed\s+vlan\s+)(?P<vlans>[\d,]+)', new_line) # Looks for a match in new_line
			if (m):
				text_list.append(m.group('vlans'))
				i = i + 1

		filt_list = filter(None, [x for xs in text_list for x in xs.split(',')])

		# Common and Unique VLANs

		common_vlans = [item for item, count in collections.Counter(filt_list).items() if count == i]
		unique_vlans = [item for item, count in collections.Counter(filt_list).items() if count == 1]
		common_vlans = map(int, common_vlans)
		unique_vlans = map(int, unique_vlans) 
		common_vlans = map(str, sorted(common_vlans))
		unique_vlans = map(str, sorted(unique_vlans))

		# Prints the results

		print ("List_1: " + str(common_vlans))
		print ("List_2: " + str(unique_vlans))

	except IOError:
		print "Can not find the txt file"

	text.close() # Closes the file


# Calls the function

exercise_2('commands.txt')