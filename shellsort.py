# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 10:44:58 2017

@author: Nzix
"""

from insertsort import direct_insert_sort

def shell_sort(nums,increment):
    for step_length in increment:
        for start in range(0,step_length):
            group = []
            step = 0
            while start + step * step_length < len(nums):
                group.append(nums[start + step * step_length])
                step = step + 1
                
            direct_insert_sort(group)
            for step in range(0,len(group)):
                nums[start + step * step_length] = group[step]
                
#        print "trip",nums

def main():
    example = [12,2,16,30,28,10,16,20,6,18]
    increment = [5,3,1]
    print example
    shell_sort(example,increment)
    print example
    
if __name__ == "__main__":
    main()