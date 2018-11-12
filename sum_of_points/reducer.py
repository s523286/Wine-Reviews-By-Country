def reducer():

	totalPoints = 0
	oldKey = None

	for line in sys.stdin:
		data = line.strip().split("\t")

		if len(data) != 2:
			continue

		thisKey, thisPoints = data

		if oldKey and oldKey != thisKey:
			print "{0}\t{1}".format(oldKey, totalPoints)

			totalPoints = 0

		oldKey = thisKey
		salesTotal += float(thisPoints)