x = input('input array:  ')
array = list(map(float, x.split()))
size = len(array)
A = sum(array)/size
print(A)