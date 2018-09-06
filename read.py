message = []
with open('reviews.txt', 'r') as files:
	for file in files:
		message.append(file)
		print('進度: ', len(message), '/', 1000000)
print(message[0])

