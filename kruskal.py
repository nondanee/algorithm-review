# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 15:03:25 2017

@author: Nzix
"""
import operator

def kruskal(dist):
    edges = []
    for i in range(0,len(dist)):
        for edge in dist[i]:
            edges.append((i,edge[0],edge[1]))#(start,end,weight)
    edges_sorted = sorted(edges, key = operator.itemgetter(2))
    edges_chosen = []
    
    components = []
    for i in range(0,len(dist)):
        components.append(set((i,)))
    
    for edge in edges_sorted:
        if len(components) == 1:
            break
        
        start_node = edge[0]
        end_node = edge[1]
        weight = edge[2]
        start_component_index = -1
        end_component_index = -1
        
        for i in range(0,len(components)):
            if start_node in components[i]:
                start_component_index = i
            if end_node in components[i]:
                end_component_index = i
                
        if start_component_index == end_component_index:
            continue
                
        component_updated = components[start_component_index] | components[end_component_index]
        components[start_component_index] = component_updated
        del components[end_component_index]
        edges_chosen.append((start_node,end_node,weight))
        
#    for edge in edges_chosen:
#        print "v{},v{} w={}".format(edge[0]+1,edge[1]+1,edge[2])
    return edges_chosen
    
    
    
def main():
    dist = [[[1,6],[2,1],[3,5]],
            [[0,6],[2,5],[4,3]],
            [[0,1],[1,5],[3,5],[4,6],[5,4]],
            [[0,5],[2,5],[5,2]],
            [[1,3],[2,6],[5,6]],
            [[2,4],[3,2],[4,6]]]
    kruskal(dist)
    
if __name__ == "__main__":
    main()