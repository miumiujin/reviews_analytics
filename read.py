data = []
count = 0
with open("reviews.txt", "r") as f :
	for line in f :
		data.append(line)
		count += 1
		if count % 20000 == 0 :
			print(len(data)) # f本身沒有長度，因此沒辦法數


print(data[2])