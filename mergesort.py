__author__ = 'divya'
def merge_sort(arr):
    if len(arr)>1:
        a = len(arr)//2
        b = arr[:a]
        c = arr[a:]
        merge_sort(b)
        merge_sort(c)
        i = 0
        j = 0
        k = 0
        while i<len(b) and j<len(c):
            if b[i]<c[j]:
                arr[k]=b[i]
                i=i+1
            else:
                arr[k]=c[j]
                j=j+1
            k = k+1
        while i<len(b):
            arr[k]=b[i]
            i=i+1
            k=k+1
        while j<len(c):
            arr[k]=c[j]
            j=j+1
            k=k+1
arr = [54,26,93,17,77,31,44,55,20]
merge_sort(arr)
print(arr)


