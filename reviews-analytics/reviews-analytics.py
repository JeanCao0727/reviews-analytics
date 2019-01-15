data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		print(len(data)) #每读一行就把行数印出来
print(len(data))
#以上是处理档案的部分，熟记

print(len(data))

print(data[0])

