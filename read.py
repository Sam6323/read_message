message = []
with open('reviews.txt', 'r') as files:
	for file in files:
		message.append(file)
		if len(message) % 1000 == 0:
			print('進度: ', len(message), '/', 1000000)
print('總長度: ', len(message), '筆資料')
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