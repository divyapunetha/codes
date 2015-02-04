__author__ = 'divya'
def insertionSort(ar):
    n = len(ar)
    V = ar[n-1]
    for i in range(1,n):
        for j in range(n-1,0,-1):
            if V<ar[j-1]:
                ar[j]=ar[j-1]
                print ar
            else:
                ar[j] = V
                break
        return ar
m = input()
ar = [int(i) for i in raw_input().strip().split()]
d = insertionSort(ar)
print d
