arr = [1,2,3,4,5,6,7,8,9]
arr2 = []
for i in range(len(arr)):
    arr2.append(arr[(len(arr)-1)-i])
    print(arr2[i])
