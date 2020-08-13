import csv
counts = {}
with open("favorites.csv", "r") as file:
	reader = csv.DictReader(file)

	for row in reader:
		title = row["title"].lower()

		if title in counts:
			counts[title] += 1
		else:
			counts[title] = 1

#lambda(functino), item(parameter) : item[1] (what is returned)
for title, count in sorted(counts.items(),key=lambda item: item[1], reverse=True): #.items() hands you two values
	print(title, count, sep="|")
