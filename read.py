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

# 現在我們想要將特定長度的樣本點篩選出來
# 想法 : 先設一個新的空清單，然後寫一個迴圈讀取原本的資料，再去設想要的條件將符合條件的樣本點篩選出來
new = []
for d in data:
	if len(d) < 150 :
		new.append(d)
print("一共有" , len(new), "筆留言長度小於150") #要退回去，等到 for迴圈跑完才print
print(new[24494])

# 這時候我們想對字串進行篩選，ex : 是否含有 great 這個單字
great = []
for d in data:
	if "great" in d :
		great.append(d)
print("一共有" , len(great), "筆留言提到 great")	
print(great[198640])

#更高級的寫法可以一次將四行化簡成一行就好
great = [d for d in data if "great" in d] # a.k.a清單快寫法
#print(great)

great_count = []
for d in data:
	if "great" in d :
		great_count.append(1)
print("一共有" , len(great), "筆留言提到 great")	
# 如果我們想要計次而不是把每個出現的資料都記下來的時候
great_count = [1 for d in data if "great" in d]
print(len(great_count))