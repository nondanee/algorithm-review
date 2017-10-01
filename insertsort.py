# -*- coding: utf-8 -*-
"""
Created on Sun Oct 01 15:48:27 2017

@author: Nzix
"""

def direct_insert_sort(nums):
    
    def batch_right_shift_one_step(nums,start,end):
        for k in range(end,start-1,-1):
            nums[k + 1] = nums[k]

    for i in range(0,len(nums)):
        j = i
        while j >= 0:
            if nums[i] >= nums[j - 1] or j == 0:
                temp = nums[i]
                batch_right_shift_one_step(nums,j,i-1)
                nums[j] = temp
                break
            elif nums[i] < nums[j - 1]:
                j = j - 1
            
#        print "step",i+1,nums
    
def main():
    example = [13,6,3,31,9,27,5,11]
    print example
    direct_insert_sort(example)
    print example
    
if __name__ == "__main__":
    main()