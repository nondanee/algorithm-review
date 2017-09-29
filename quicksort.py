# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 12:59:04 2017

@author: Nzix
"""

def quick_sort(nums,front=None,back=None):
   
    front = 0 if front == None else front
    back = len(nums) - 1 if back == None else back
  
    if back - front < 1:
        return

#    standard = nums[0]
#    nums[0] = None
#    front = 0
#    back = len(nums) - 1
        
    front_previous = front
    back_previous = back
    standard = nums[front]
    nums[front] = None
    
    while front != back:
        if nums[back] != None:
            if nums[back] < standard:
                nums[front] = nums[back]
                front = front + 1
                nums[back] = None
            elif nums[back] >= standard:
                back = back - 1

        elif nums[front] != None:
            if nums[front] > standard:
                nums[back] = nums[front]
                back = back - 1
                nums[front] = None
            elif nums[front] <= standard:
                front = front + 1
    
    assert front == back
    nums[front] = standard
    
#    quickorder(nums,0,front)
#    quickorder(nums,back+1,len(nums)-1)
    
    quick_sort(nums,front_previous,front)
    quick_sort(nums,back+1,back_previous)
    
    
def main():
    example = [92,96,100,110,42,35,30,88]
    print example
    quick_sort(example)
    print example

if __name__ == "__main__":
    main()
