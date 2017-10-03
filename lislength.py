# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 14:13:12 2017

@author: Nzix
"""
from quicksort import quick_sort

def les_length(nums1,nums2):
    
    # init memo
    memo = []
    for i in range(0,len(nums2)):
        memo.append([0]*len(nums1))
        
    for i in range(0,len(nums2)):
        for j in range(0,len(nums1)):
        # for j in range(i,len(nums1)):
        # make length of nums1 larger than nums2 (exchange), using only upper triangle matrix is enough
            common = bool(nums2[i] == nums1[j])
            before = 0
            if i-1>=0:
                if memo[i-1][j] >= before:
                    before = memo[i-1][j]
            if j-1>=0:
                if memo[i][j-1] >= before:
                    before = memo[i][j-1]
                        
            memo[i][j] = before + common
            
#    for i in range(0,len(memo)):
#        print memo[i]
    
    return memo[len(nums2)-1][len(nums1)-1]


def lis_length(nums):
    nums_sorted = nums[:]
    quick_sort(nums_sorted)
    return les_length(nums,nums_sorted)


def main():
    example = [10,9,2,5,3,7,101,18]
    print example
    print lis_length(example)


if __name__ == "__main__":
    main()