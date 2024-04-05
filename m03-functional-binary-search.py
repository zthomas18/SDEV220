#Zach Thomas
# M03 OOP Sorting an Array of 0's, 1's and 2's
# 4/5/2024

class Solution:	
    def binarysearch(self, arr, n, k):
        low = 0                         #pointer for beginning of array
        high = n-1                      #pointer for end (n) of array
    
        while low<=high:                #while our low and high pointers have not passed each other in index value, this loop will continue
        
            middle = int((high+low)/2)  #initiate each instance of the loop with a new middle pointer between our high and low pointers
            if arr[middle] == k:        #if the value at our middle pointer == k, then return that value
                return int(middle)
            elif arr[middle] > k:       #if the value of our middle pointer is greater than k:
                high = middle-1         #move our high point index left of the middle point so we can focus on all the numbers < the middle point
            else:                       #this code will be reached if the k number is not at or below the middle point
                low = middle+1          #move the low point to the right of the middle point so we can focus on the numbers above the middle point
        return -1                       #if the number is not greater than, less than or equal to the middle point, the code will return -1