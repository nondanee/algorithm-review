# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 13:49:48 2017

@author: Nzix
"""

def two_way_merge_sort(nums):
    
    trip = 1
    while True:
        way_length = 2 ** (trip - 1)
        if way_length >= len(nums):
            return 
        
        treated_number = 0
        while treated_number < len(nums):
            
            first_way = nums[treated_number:treated_number + way_length]
            second_way = nums[treated_number + way_length:treated_number + way_length * 2]
            
            first_pointer = 0
            second_pointer = 0
            sorted_number = 0
            
            while sorted_number < len(first_way) + len(second_way):
                if first_pointer > len(first_way) - 1:
                    nums[treated_number + sorted_number] = second_way[second_pointer]
                    second_pointer = second_pointer + 1
                elif second_pointer > len(second_way) - 1:
                    nums[treated_number + sorted_number] = first_way[first_pointer]
                    first_pointer = first_pointer + 1
                
                elif first_way[first_pointer] < second_way[second_pointer]:
                    nums[treated_number + sorted_number] = first_way[first_pointer]
                    first_pointer = first_pointer + 1
                elif first_way[first_pointer] >= second_way[second_pointer]:
                    nums[treated_number + sorted_number] = second_way[second_pointer]
                    second_pointer = second_pointer + 1
                    
                sorted_number = sorted_number + 1
                
            treated_number = treated_number + len(first_way) + len(second_way)
            
#        print "trip",trip,nums
        
        trip = trip + 1

def main():
    example = [49,38,65,97,76,13,27]
    print example
    two_way_merge_sort(example)
    print example

if __name__ == "__main__":
    main()