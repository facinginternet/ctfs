
res = [0, -15, 6, -2, -12, 17, -17, 26, -4, -68, 44, 20, -6, -61, 59, -56, 44, 5, 5, -69, 61, -61, 0, 15, 58, -11, 10, -57, 49, -5, 13, -57, 0, 4, 70]
start = 'x'
flag = ''

for i in res:
	start = chr(ord(start) + i)
	flag += start

print(flag)