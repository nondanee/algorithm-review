# -*- coding: utf-8 -*-
"""
Created on Sun Oct 01 15:48:27 2017

@author: Nzix
"""

def half_insert_sort(nums):
    
    def batch_right_shift_one_step(nums,start,end):
        for k in range(end,start-1,-1):
            nums[k + 1] = nums[k]

    for i in range(0,len(nums)):
        low = 0
        high = i - 1
        while low <= high:
            middle = (low + high)//2
            if nums[middle] <= nums[i]:
                low = middle + 1
            elif nums[middle] > nums[i]:
                high = middle - 1
            elif nums[middle] == nums[i]:
                break
            
        middle = (low + high)//2 # why do cal once more, see analysis
        temp = nums[i]
        batch_right_shift_one_step(nums,middle+1,i-1)
        nums[middle+1] = temp
            
#        print "step",i+1,nums
    
def main():
    example = [21,25,49,25,16,8]
    print example
    half_insert_sort(example)
    print example
    
if __name__ == "__main__":
    main()

'''    
analysis

init low  0
init high 2

21 25 49 [20]
its position is 0

     <25 <21 out cal
mid   1   0-->0   -1
low   0   0
high 1-1 0-1

21 25 49 [22]
its position is 1

     <25 >21 out cal
mid   1   0-->0   0
low   0  0+1
high 1-1  0

21 25 49 [26]
its position is 2

     >25 <49 out cal
mid   1   2-->2   1
low  1+1  2
high  2  2-1

21 25 49 [50]
its position is 3

     >25 <49 out cal
mid   1   2-->2   2
low  1+1 2+1
high  2   2

correct postion is (cal mid once more) + 1
'''