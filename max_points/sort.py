o = open("o.txt", "r")
s = open("s.txt", "w")

lines = o.readlines()
lines.sort()

for line in lines:
  s.write(line)

o.close()
s.close()