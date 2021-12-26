data = []
count = 0
with open("reviews.txt", "r") as f :
	for line in f :
		data.append(line)
		count += 1
		if count % 50000 == 0 : #求餘數
			print(len(data)) # f本身沒有長度，因此沒辦法數
print("檔案讀取完了，總共有", len(data), "筆資料")
# 到此為止我們已經把所有的資料都裝進 data 這個清單
print(data[0])


# 現在我們想要算出這 1,000,000 筆資料的平均長度
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

#這時候我們想要把每一個字都去計數(count)

wc = {} # word_count ，每一個字的計數
for d in data: 
	words = d.split(" ") # 這邊要注意，d 代表一個字串(str)
	for word in words: # words 是一個清單(字串本質上也可以當清單) ，裡面裝了用 " " 分割後的 d
		if word in wc: # 如果這個 word 有出現過
			wc[word] += 1 # 去wc這個字典 ，可以把wc[word]想成 "查找" 的行為 ，查找這個 word 是否有出現過 ，有的話就 +1 
		else:
			wc[word] = 1 # 如果沒有出現的話就先讓它等於 1 ，也就是新增新的 key 進 wc 字典
# print(wc) # 直接把 wc 印出來會很醜 ，所以再額外設一個迴圈讓視覺上比較整潔
for word in wc:
	if wc[word] > 10000: # 一個一個印出來太費時了 ，我們只想知道出現超過100次的 key ，沒有超過的先不印
		print(word, wc[word]) # word 代表 key ，而 wc[word] 代表出現的次數
	# break # (技巧) 為了避免把所有的 data 都印出來 ，可以在前面加一個 break ，等於只跑了一圈
print(len(wc)) # 用來數 wc 這個字典有多少個 key
print(wc["Allen"]) # 用來查找 "Allen" 是否存在 wc這個字典

# 最後我們來寫一個功能來讓使用者查詢關鍵字
while True:
	word = input("請問你想查什麼字 : ")
	if word == "q": #為了讓最後有辦法離開這個迴圈
		break
	if word in wc:
		print(word, "出現過的次數為", wc[word], "次")
	else:
		print("這個字沒有出現過~") # 如果沒有加上這行的話 ，最後如果查的單字不在字典裡的話會當掉
print("感謝使用本查詢功能~")


