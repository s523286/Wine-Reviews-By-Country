# Reference from Dr. Case's slides on MapReduce in Python
# mapper.py will map our data to key/value pairs

 # open file, read-only raw data
f = open("wineData.txt","r") 

# open file, write - just our key, value pairs
o = open("o.txt", "w")

# input comes from STDIN (standard input)
for line in f:
    line = line.strip()
    line = line.split("\t")

    if len(line) ==13:
        country = line[0]
        price = line[4]
# Prints the output in the format of country, price
        o.write("{0}\t{1}\n".format(country, price))
f.close()
o.close()
       