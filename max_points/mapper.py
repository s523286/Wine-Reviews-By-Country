# opens the file to read and write from
i = open("wineData.txt", "r")
o = open("o.txt", "w")

# reading the lines in 
for line in i:
  # splitting and stripping the data
  data = line.strip().split("\t")
  if (len(data) == 13):
    # titles the fields
    country, description, designation, points, price, province, region_1, region_2, taster_name, taster_twitter_handle, title, variety, winery = data
    # writing out the o file with the intermediate key-value pairs
    o.write(country + "\t" + points + "\n")
    print(country + "\t" + points + "\n")

# closes the files
i.close()
o.close()


