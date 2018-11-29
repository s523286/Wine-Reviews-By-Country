# opens the file to read and write from 
s = open("s.txt","r")
r = open("r.txt", "w")

# setting thisKey and min to 0
thisKey = ""
min = 0.0

# It is going to read every line in and strip and split it
for line in s:
  data = line.strip().split("\t")

# if the data isnt in key value pairs then it will continue
  if len(data) != 2:
    continue

# Setting country and points to data
  country, points = data

  if country != thisKey:
    if thisKey:
      # output the key value pair result
      r.write(thisKey + '\t' + str(min)+'\n')

    # start over when changing keys
    thisKey = country 
    min = points
  
  # statment to find the minimum points
  if int(points) < min:
    min = int(points)

# output the final entry when done
r.write(thisKey + '\t' + str(min)+'\n')

# closes the files
s.close()
r.close()