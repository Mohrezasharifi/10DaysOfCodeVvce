#program to execute left rotation on an array
#The array is already given within the program
#The array is indicated by 'arr'
#The number of left rotation is indicated by 'lr'
#leftRotate is used to rotate the array

#The given array
arr = [1, 2, 3, 4, 5]

def leftRotate(arr, lr, n): 
	for i in range(lr): 
		leftRotatebyOne(arr, n) 

#This function is to left Rotate arr[] of size n by 1
def leftRotatebyOne(arr, n): 
	t = arr[0] 
	for i in range(n-1): 
		arr[i] = arr[i+1] 
	arr[n-1] = t 

#t indicates 'temporary variable'	

#This function to print the rotated array 
def printArray(arr,size): 
	print("The rotated array is: ")
	for i in range(size): 
		print ("%d"% arr[i],end=" ") 

#The array is rotated 4 to the left
leftRotate(arr, 4, 5) 

printArray(arr, 5) 

"""
The rotated array is:
5 1 2 3 4