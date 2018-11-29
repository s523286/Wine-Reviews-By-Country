# Referenced Dr. Case's slides on MapReduce in Python
# mapper.py will map our data, wineData.txt, to key/value pairs

# opens wineData.txt as a read only file
f = open("wineData.txt","r")
# opens o.txt as a file to write to
o = open("o.txt", "w")

# for loop to iterate through all the lines
for line in f:
    # sets variable, data, as each line seperated by a tab
    data = line.strip().split("\t")
    # if statement to skip bad lines
    if len(data) == 13:
        # sets variable names to each column in data
        country, description, designation, points, price, province, region_1, region_2, taster_name, taster_twitter_handle, title, variety, winery = data
        # writes the country column and points column in o.txt
        o.write("{0}\t{1}\n".format(country, points))
        print(country + '\t' + str(points) + '\n')

# closes both files
f.close()
o.close()
