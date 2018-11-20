# Referenced Dr. Case's Slides on MapReduce in Python
# reducer.py will use the key/value pairs: country, points
# This file sums the points for each country

# opens s.txt as a read-only file (contains the sorted list)
s = open("s.txt", "r")
# opens r.txt as a file to write to
# r = open("r.txt", "w")

# instantiating variables for later use
oldKey = None
thisKey = ""
thisValue = 0

# for loop to iterate through each line
for line in s:
    # seperates each value with a tab
    data = line.strip().split('\t')
    # if statement to ignore a bad input line
    if len(data) != 2:
        continue
    # read in our variables and set them equal to data
    country, points = data

    # make sure country is not null
    if country != thisKey:
        if thisKey:
            # output the last key value pair result
            print(thisKey + '\t' + str(thisValue) + '\n')

        # start over when changing keys
        thisKey = country
        thisValue = 0

    # apply the sum function
    thisValue += int(points)

# output the final key and value
print(thisKey + '\t' + str(thisValue) + '\n')

# close the files
s.close()
# r.close()
