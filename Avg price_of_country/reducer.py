# Reference from Dr. Case's Slides on MapReduce in Python
# reducer.py will use the key/value pairs: country, price

# This file is used find the average price for each bottle in the country
s = open("s.txt", "r")
r = open("r.txt", "w")

oldKey = None
thisKey = ""
thisValue = 0.0
count=0.0

for line in s:
    data = line.strip().split('\t')
# if bad input line
    if len(data) != 2:  
# ignore it
        continue  

# read into variables
    country, price = data  

    if country != thisKey:
        if thisKey:
# resultant ouput in the form of key value pair
            r.write(thisKey + ',' + str(thisValue/count) + '\n')
            print(thisKey + '\t' + str(thisValue/count) + '\n')

# start over when changing keys
        thisKey = country
        thisValue = 0.0
        count = 0.0

# apply the aggregation function
    thisValue += float(price)
# apply the count function
    count += 1
# final ouput in the key value pair i.e.,(country, average)
r.write(thisKey + ',' + str(thisValue/count) + '\n')
print(thisKey + '\t' + str(thisValue/count) + '\n')

s.close()
r.close()
