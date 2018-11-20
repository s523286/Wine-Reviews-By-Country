# Referenced Dr. Case's slides on MapReduce in python
# sort.py will sort our key/value pairs alphabetically

# opens o.txt as a read only file (contains key-value pairs from mapper)
o = open( "o.txt", "r")
# opens s.txt as a file to write to
s = open("s.txt", "w")

# reads in all the lines of the file and sorts them
lines = o.readlines()
lines.sort()

# writes out each sorted line to the s.txt file
for line in lines:
    s.write(line)

# closes both files
o.close()
s.close()