# -*- coding: utf-8 -*-
"""
Created on Sun Oct 01 16:34:30 2017

@author: Nzix
"""

def simple_select_sort(nums):
    
    for i in range(0,len(nums)):
        smallest_below_i = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[smallest_below_i]:
                smallest_below_i = j
        nums[i],nums[smallest_below_i] = nums[smallest_below_i],nums[i]
        
#        print "step",i+1,nums

def main():
    example = [21,25,49,25,16,8]
    print example
    simple_select_sort(example)
    print example
    
if __name__ == "__main__":
    main()