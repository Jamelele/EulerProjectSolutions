import time

start = time.time()

n = 1000
k = 0

for i in range(0, n, 3):
	print(i)
	k += i

for i in range(0, n, 5):
	print(i)
	k += i

for i in range(0, n, 15):
	k -= i

end = time.time()

print(k)