# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 19:45:37 2017

@author: Nzix
"""

def prim(dist,unreachmark):
    nodes_unchosen = set(range(1,len(dist)))
    nodes_chosen = set([0])
    edges_chosen = []
    while len(nodes_unchosen) != 0:
        weight_minimum = unreachmark
        edge_chosen_thistime = (-1,-1,unreachmark)
        node_chosen_thistime = -1
        for node_chosen in nodes_chosen:
            for node_unchosen in nodes_unchosen:
                if dist[node_chosen][node_unchosen] <= weight_minimum:
                    weight_minimum = dist[node_chosen][node_unchosen]
                    node_chosen_thistime = node_unchosen
                    edge_chosen_thistime = (node_chosen,node_unchosen,weight_minimum)
                
        nodes_unchosen.remove(node_chosen_thistime)
        nodes_chosen.add(node_chosen_thistime)
        edges_chosen.append(edge_chosen_thistime)
        
#    for edge in edges_chosen:
#        print "v{},v{} w={}".format(edge[0]+1,edge[1]+1,edge[2])
    return edges_chosen



def main():
    dist = [[999,6,1,5,6,999],
            [6,999,5,999,3,999],
            [1,5,999,5,6,4],
            [5,999,5,999,999,2],
            [999,3,6,999,999,6],
            [999,999,4,2,6,999]]
    unreachmark = 999
    prim(dist,unreachmark)
    
if __name__ == "__main__":
    main()  