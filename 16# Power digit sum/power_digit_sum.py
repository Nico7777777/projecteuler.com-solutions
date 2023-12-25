result = ['1']
for i in range(1000):
	rest = 0
	for j in range(len(result)-1, -1, -1):
		interm = int( result[j] ) * 2 + rest
		rest = interm//10
		result[j] = str( interm % 10 )
	if rest != 0:
		result.insert(0, rest)

the_sum = 0
for i in  result:
	the_sum += int(i)
print(the_sum)
