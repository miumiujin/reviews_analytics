data = []
count = 0
with open("reviews.txt", "r") as f :
	for line in f :
		data.append(line)
		count += 1
		if count % 50000 == 0 : #求餘數
			print(len(data)) # f本身沒有長度，因此沒辦法數
print("檔案讀取完了，總共有", len(data), "筆資料")
# 現在我們想要算出這 1000,000 筆資料的平均長度
sum_length = 0
for d in data :
	sum_length += len(d) # sum_length = sum_length + len(d) ，將每一筆留言的長度跟目前留言的總數加在一起 ，再存回去
	#print(sum_length)
print("平均的留言長度是", sum_length/len(data))

