# Referenced Dr. Case's Slides on MapReduce in Python
# reducer.py will use the key/value pairs: country, points
# This file sums the points for each country
s = open("s.txt", "r")
r = open("r.txt", "w")

oldKey = None
thisKey = ""
thisValue = 0.0

for line in s:
    data = line.strip().split('\t')
    if len(data) != 2:  # if bad input line
        continue  # ignore it

    country, points = data  # read into variables

    if country != thisKey:
        if thisKey:
            # output the last key value pair result
            r.write(thisKey + '\t' + str(thisValue) + '\n')

        # start over when changing keys
        thisKey = country
        thisValue = 0

    # apply the aggregation function
    thisValue += int(points)

r.write(thisKey + '\t' + str(thisValue) + '\n')

s.close()
r.close()
