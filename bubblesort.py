# -*- coding: utf-8 -*-
"""
Created on Sun Oct 01 16:31:06 2017

@author: Nzix
"""

def bubble_sort(nums):
    for i in range(0,len(nums)-1):
        exchange = 0
        for j in range(0,len(nums)-1-i):
            if nums[j] > nums[j + 1]:
                nums[j],nums[j + 1] = nums[j + 1],nums[j]
                exchange = exchange + 1
        if exchange == 0:
            break
        
#        print "trip",i+1,nums 

def main():
    example = [12,2,16,30,28,10,16,20,6,18]
    print example
    bubble_sort(example)
    print example
    
if __name__ == "__main__":
    main()