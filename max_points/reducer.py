# opens the file in read mode
s = open("s.txt","r")
# opens the file in write mode
r = open("r.txt", "w")

# setting thisKey to null and max to 0.0
thisKey = ""
max = 0.0

# It is reading every line in and strip and split it using tab as limiter
for line in s:
  data = line.strip().split("\t")

# if the data is not in the key value pairs then it will skip
  if len(data) != 2:
    continue

# Setting country and points to data
  country, points = data
  #print(country + points)
  if country != thisKey:
    if thisKey:
      # output the key value pair result
      r.write(thisKey + '\t' + str(max) +'\n')
      print(thisKey + '\t' + str(max) +'\n')

    # Assigning the country and points to thisKey and max parameters.
    thisKey = country 
    max = points
  
  # statment to find the maximum points
  if points >= max:
    max = points

# output the final entry when done
r.write(thisKey + '\t' + str(max) +'\n')
print(thisKey + '\t' + str(max) +'\n')

# closes the files
s.close()
r.close()