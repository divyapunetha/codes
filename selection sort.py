arr = []
n = int(raw_input())
for i in range (n):
	m = int(raw_input())
	arr.append(m)
print arr
N = len(arr)
for j in range (0,N):
	min = j
	for k in range(j+1,N):
		if (arr[k] < arr[min]):
			min = k
	arr[i] , arr[min] = arr[min] , arr[i]
print arr



