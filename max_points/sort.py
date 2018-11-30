# opens the file in read mode
o = open("o.txt", "r")
# opens the file in write mode
s = open("s.txt", "w")
#read the lines one by one
lines = o.readlines()
#sort the lines
lines.sort()
#read the lines and print them
for line in lines:
  s.write(line)
#close the file
o.close()
#close the file
s.close()