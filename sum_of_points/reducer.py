def reducer():
	thisKey = ""
	thisValue = 0

	for line in sys.stdin:
		data= line.strip().split("\t")

		if len(data) !=2:
			continue
		country, points = data

		if country != thisKey:
			if thisKey:
				print"{0}\t{1}\n".format(thisKey, thisValue)
			thisKey = country	
			thisValue = 0
		thisValue += int(points)
	print"{0}\t{1}\n".format(thisKey, thisValue)

