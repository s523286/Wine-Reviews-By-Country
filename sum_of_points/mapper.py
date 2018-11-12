#!/usr/bin/python

import sys

for line in sys.stdin:
	data = line.strip().split("\t")
	country, description, designation, points, price, province, region_1, region_2, taster_name, taster_twitter_handle, title, variety, winery = data
	print "{0}\t{1}".format(country, points)
