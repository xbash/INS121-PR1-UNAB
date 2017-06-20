arr = [5, 2, 3, 4]
arr2 = []
for i in range( len( arr ), 1, -1 ):
    print("arr[i] = ", arr[i -1])
    arr2.append( arr[ i - 1 ] )
for i in range( len( arr2 ) ):
    print("arr2[i] = ", arr2[i] )
for i in range( 10 , 0, -1):
    print (i) 
