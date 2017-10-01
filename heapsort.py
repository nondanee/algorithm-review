# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 22:24:50 2017

@author: Nzix
"""

def heap_sort(nums,reverse = 1):# big heap default(reverse)

    def adjust_simple_tree(nums,parent,big):
        
        # big = 1    big heap
        # big = 0    small heap
        
        # i          parent
        # 2i + 1     left child (if exist)
        # 2i + 2     right child (if exist)
    
        left_child = parent * 2 + 1 if parent * 2 + 1 <= len(nums) - 1 else None
        right_child = parent * 2 + 2 if parent * 2 + 2 <= len(nums) - 1 else None
        
        
        if left_child == None:# parent is a leaf node
            return 
        
        elif right_child == None:
            if ( nums[left_child] < nums[parent] ) ^ big:
                nums[parent],nums[left_child] = nums[left_child],nums[parent]
        
        elif nums[left_child] == nums[right_child]:# default exchange left_child with parent
            if ( nums[left_child] < nums[parent] ) ^ big:
                nums[parent],nums[left_child] = nums[left_child],nums[parent]
                adjust_simple_tree(nums,left_child,big)
        
        elif ( nums[left_child] < nums[right_child] ) ^ big:
            if ( nums[left_child] < nums[parent] ) ^ big:
                nums[parent],nums[left_child] = nums[left_child],nums[parent]
                adjust_simple_tree(nums,left_child,big)
        
        elif ( nums[right_child] < nums[left_child] ) ^ big:
            if ( nums[right_child] < nums[parent] ) ^ big:
                nums[parent],nums[right_child] = nums[right_child],nums[parent]
                adjust_simple_tree(nums,right_child,big)
      
    # inital heap
    last_branch_node = (len(nums) - 1) // 2
    for branch_node in range(last_branch_node,-1,-1):
        adjust_simple_tree(nums,branch_node,reverse)
            
    # shallow cpoy
    origin = nums[:]
    
    # pop from heap
    for i in range(0,len(nums)):
        nums[i] = origin[0]
        origin[0] = origin[len(origin)-1]
        origin.pop()
        
        last_branch_node = (len(nums) - 1) // 2
        for branch_node in range(last_branch_node,-1,-1):
            adjust_simple_tree(origin,branch_node,reverse)



def main():
    example = [15,9,7,8,20,-1,7,4]
    print example
    heap_sort(example,reverse = 0)
    print example
    
if __name__ == "__main__":
    main()