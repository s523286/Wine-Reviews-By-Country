#Referenced Dr. Case's slides on MapReduce in Python
#mapper.py will map our data, wineData.txt, to key/value pairs
f = open("wineData.txt","r")  # open file, read-only raw data
o = open("o.txt", "w") # open file, write - just our key, value pairs
for line in f:  
    data = line.strip().split("\t")
    if len(data) == 13:
        country, description, designation, points, price, province, region_1, region_2, taster_name, taster_twitter_handle, title, variety, winery = data
        o.write("{0}\t{1}\n".format(country, points))
f.close()
o.close()
