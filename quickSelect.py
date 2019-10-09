def quickSelect(array,left,right,kth):
	# left:start index; right:end index; kth:the goal
	if(kth>0 and kth<= right-left+1):
		number = right-left+1

		median = []

		i=0
		# '//' gets the integral result
		while(i < number//5):
			median.append(findMedian(array,left+5*i,5))
			i+=1
        # check if there are any groups less than 5 
		if(i*5 < number):
			median.append(findMedian(array,left+5*i,number%5))
			i+=1
			# the result of (i+=1) regards as how many elements in the median array now

		if i == 1:
			medOfMedians = median[i-1]
		else:
			# find kth-smallest
			medOfMedians = quickSelect(median,0,i-1,i//2)
        
        # medians of medians can be reasonable pivots. We can partition arrays around it
        # the index of pivot is returned to the position value
		position = doPartition(array, left, right, medOfMedians)

        # calculate the length of left side in the array
		length = position-left+1
		if(length == kth):
			return array[position]
		elif(length > kth):
        	# recur for the left subarray
			return quickSelect(array,left,position-1,kth)
		else:
        	# recur for the right subarray
			return quickSelect(array,position+1,right,kth-length)
	
	else: 
		return "more than the number of elements in the array"

# standard partition process of quicksort()
def doPartition(array, left, right, mm):
	
	# pivot places at right position (last element)
	for i in range(left,right):
		if array[i] == mm:
			swap(array,right,i)
			break

	# mm = array[right]
	check = left
    
	for j in range(left,right):
		if array[j] <= mm:
			swap(array,check,j)
			check+=1

	swap(array, check, right)
	return check

def swap(array, x, y):
	temp = array[x]
	array[x] = array[y]
	array[y] = temp


def findMedian(array, left, number):
	# left:left index
    list=[]
    for i in range(left,left+number):
    	list.append(array[i])
    
    list.sort()
    # return the middle element
    return list[number//2];	


def main():

	import random
	import datetime
	# assume all elements are distinct
	# array=[69,81,30,38,9,2,47,61,32,79]
	# nOfEle needs to be 1 more than number because range's rule 
	nOfEle = 11; 
	items = list(range(1,nOfEle))
	random.shuffle(items)
	# print items
	
	k = 8
	# find kth smallest element
	start = datetime.datetime.now()
	print k,"'th smallest element is ",quickSelect(items,0,len(items)-1,k)
	end = datetime.datetime.now()
	delta = end-start
	# if want to change to nanosecond, *1000
	print delta.microseconds

if __name__ == '__main__':
	main()