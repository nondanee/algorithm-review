# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 22:57:19 2017

@author: Nzix
"""




def floyd(dist,unreachmark):
    #initialize
    nums = len(dist)
    path = []
    for i in range(0,nums):
        path.append([-1]*nums)
    
    
    def getShortestPath(route,start,end):
        hub = path[start][end]
        if hub == -1:
            return
        index = route.index(end)
        route.insert(index,hub)
        getShortestPath(route,start,hub)
        getShortestPath(route,hub,end)
    
    #insert hub
    for num in range(0,nums):
        # every loop confirm shortest path passing [from 0 to num] nodes, based on the result last loop [from 0 to num-1]
        for i in range(0,nums):
            if i == num:
                continue
            for j in range(0,nums):
                if j == num:
                    continue
                if dist[i][num] == unreachmark or dist[num][j] == unreachmark:
                    continue
                elif dist[i][num] + dist[num][j] < dist[i][j]:
                    dist[i][j] = dist[i][num] + dist[num][j]
                    path[i][j] = num
    
    #result out
    for i in range(0,nums):
        for j in range(0,nums):
            route = [i,j]
            getShortestPath(route,i,j)
            print i,"to",j,route,dist[i][j]


def main():
    dist = [[0,6,99999,4,6,2,3,4,5,2],
            [8,0,3,5,99999,1,8,8,7,3],
            [3,7,0,7,7,9,99999,8,7,99999],
            [5,4,99999,0,4,3,1,1,8,4],
            [2,8,7,5,0,5,7,1,9,2],
            [5,9,6,2,7,0,8,3,2,5],
            [3,5,5,8,8,99999,0,7,8,2],
            [7,3,1,2,6,1,8,0,99999,9],
            [9,2,5,99999,99999,8,2,6,0,99999],
            [3,8,8,2,7,7,1,3,8,0]]
    unreachmark = 99999
    #dist = [[0,1,4,999],[999,0,2,5],[999,999,0,1],[2,999,999,0]]
    #unreachmark = 999
    floyd(dist,unreachmark)
    
if __name__ == "__main__":
    main()
    