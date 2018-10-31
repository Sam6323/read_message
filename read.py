message = []
with open('reviews.txt', 'r') as files:
	for file in files:
		message.append(file)
		if len(message) % 1000 == 0:
			print('進度: ', len(message), '/', 1000000)
print('總長度: ', len(message), '筆資料')
# print(message[0])

print(message[0])
avg = 0
for len_avg in message:
	avg = avg + len(len_avg)
avg = int(avg / len(message))
print('平均長度: ', avg)

#篩選<100的數量
new = []
for line in message:
	if len(line) < 100:
		new.append(line)	
print('總共有: ', len(new), '行小於100個字')

# 文字計數
wc = {} # wc = word_count
for line in message:
	data = line.split() # split預設為空白,不輸入會使用預設值
	
	for word in data:
		if word in wc:
			wc[word] += 1
			
		else:
			wc[word] = 1 # 新增key
			
for word in wc: # 印出出現超過1000000次的字
	if wc[word] > 1000000:
		print(word, wc[word])

while True: # 輸入要查詢的字
	key = input('請輸入要查詢的字: ')
	if key == 'q':
		break
	if key in wc:
		print(key, '共出現: ', wc[key])
	else:
		print('查詢不到這個字 !!!')




