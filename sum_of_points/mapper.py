f = open("C:/44517/Group1MapReduce/data/winemag-data-130k-v2.csv","r")
o = open("C:/44517/Group1MapReduce/results/results.txt", "w") 

for line in f:
	data = ine.strip().split(",")
	if len(data) == 6:
		country, description, designation, points, price, province, region_1, region_2, taster_name, taster_twitter_handle, title, variety, winery = data
		o.write("{0}\t{1}".format(country, points))
f.close()
o.close()