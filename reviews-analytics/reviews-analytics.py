data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
#以上是处理档案的部分，熟记
		count += 1
		if count % 1000 == 0:
			print(len(data)) 
#👆每读一千行就把已印出的行数印出来,可以看载入的多块, %求余数
print('档案读取完了，共有', len(data), '笔资料')
sum_len = 0
for d in data:
	sum_len = sum_len + len(d) #累积每笔长度
	print(sum_len)
print('avg is', sum_len/len(data))
#👆每笔字串当作d,看这一百万笔留言的平均字数
