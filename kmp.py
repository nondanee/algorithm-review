# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 21:05:02 2017

@author: Nzix
"""

def kmp_search(string,pattern):
    
    def generate_next_array():
        next_array = [-1,0] + [0]*(len(pattern)-2)
        # 初始化next数组值为 0 1 1 1 1 1 1 ...
        # python的next是保留字啊 ...
        
        for x in range(2,len(pattern)):
            
        # 假设 x = 5 (第6个)
        # 前一个 x = 4 (第5个)
        # x x x x|x y
        #     x x x x y 起始偏移为 4 - next[4]
        #               因为计算next[x-1]时已经保证偏移小于j-1 - next[x-1]没有重叠部分完全匹配的位置
        #               偏移为x-1 - next[x-1]是第一次完全匹配位置
        #               故每次偏移不必从1开始(起码偏1, 不可能偏0的, 就是因为j位置对不上了才要找next)
                        
        
        # x x x x x|x            
        #     x x x x x
        # |-->|          假设当前偏移 offset = 2
        #     |---|      重叠部分 overlapping = j(5) - offset(2) = 3项, 
        #                需遍历重叠部分, 有不匹配就向后偏移, 全匹配(第一次全匹配)就是最小偏移
                 
        
        # x x x x x|x            
        #           x x x x x
        # |-------->|    offset_max = j = 5 最大偏移为j, 偏移到最大表明没有公共前缀, 从模板最初开始
        
        # x x x x x|x            
        #       x x x x x
        #           ^    
        #           2    假设偏移为3重叠部分全部匹配, 则与主串比较的位置为i = x(5) - offset(3) = 2 = next[x]
        #                反过来运算可以计算偏移为offset = x - next[x]
        
            offset_previous = (x-1) - next_array[(x-1)]
            offset = offset_previous
            offset_max = x
            full_match = 0
            overlapping = x - offset
            while full_match == 0 and offset < offset_max:
                for i in range(0,overlapping):
                    if pattern[i] != pattern[offset+i]:
                        full_match = 0
                        offset = offset + 1
                        break
                    else:
                        full_match = 1       
            next_array[x] = x - offset
        return next_array
        
    next_array = generate_next_array()
#    print next_array
    
    i = 0
    j = 0
    while j < len(string):
        if string[i] == pattern[j]:
            i = i + 1
            j = j + 1
            if j == len(pattern):
                return i - j # start position
        else:
            j = next_array[j]
            if j == -1:
                i = i + 1
                j = j + 1                
    return -1 # failed


def main():
    string = "abcabaaabaabcac"
    pattern = "abaabcac"
    print kmp_search(string,pattern)


if __name__ == "__main__":
    main()
