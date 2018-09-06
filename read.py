message = []
with open('reviews.txt', 'r') as files:
	for file in files:
		message.append(file)
		if len(message) % 1000 == 0:
			print('進度: ', len(message), '/', 1000000)
print('總長度: ', len(message), '筆資料')
print(message[0])
avg = 0
i = 0
while i < 1000000:
	avg = len(message[i]) + avg
	i += 1
avg = int(avg / i)
print('平均長度: ', avg)

