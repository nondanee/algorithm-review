# -*- coding: utf-8 -*-
"""
Created on Sun Oct 01 18:05:26 2017

@author: Nzix
"""

def radix_sort(nums,radix = 10):

    queue_group = []
    for i in range(0,radix):
        queue_group.append([])
    
    bit = 0
    goon = 1
    while goon:
            
        goon = 0
        for i in range(0,len(nums)):
            queue_group[nums[i]//(radix**bit)%radix].append(nums[i])
            goon = 1 if nums[i] >= (radix**(bit+1)) and goon == 0 else 0
        
        store = 0
        for i in range(0,len(queue_group)):
            for j in range(0,len(queue_group[i])):
                nums[store + j] = queue_group[i][j]
            
            store = store + len(queue_group[i])
            queue_group[i] = []
            
        bit = bit + 1
        

def main():
    example = [329,457,657,839,436,720,355]
    print example
    radix_sort(example)
    print example
    
if __name__ == "__main__":
    main()