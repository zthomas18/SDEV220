#Zach Thomas
# M03 OOP Sorting an Array of 0's, 1's and 2's
# 4/5/2024

#creating a class to solve the problem
class Solution:
    
    #defining a function to sort the 0's, 1's and 2's
    def sort012(self,arr,n):
        
        #creating variables to use as pointers to represent different indexes (we \\
        #can use these to iterate through the list and swap numbers)
        low = 0
        mid = 0
        high = n-1
        
        #we will use the middle pointer to focus on specific indexes and then swap \\
        #the values with values to the left (lower) or right (higher)
       
        #keep iterating this loop until our mid pointer is past the high pointer
        while mid <= high:
            
            #if the value of the focussed index(mid) is 0, then we will move it to\\
            #the left by swapping with low and then move to the next index
            if arr[mid] == 0:
                arr[mid], arr[low] = arr[low], arr[mid]
                low += 1
                mid += 1
                
            #if the value is 1, then we will leave it here and move to the next index
            elif arr[mid] == 1:
                mid += 1
                
            #if the value is 2, we will move it to the right by swapping it with high
            #we will decrease the index of high and gradually move it towards the \\
            #middle as we add 2's
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1