# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 19:18:37 2017

@author: Nzix
"""

def djikstra(dist,start,unreachable):
    distances = []
    for i in range(0,len(dist)):
        distances.append({"through":[i],"length":unreachable,"chosen":False})
    nodes_chosen = [start]
    
    while True:
        shortest_distance = unreachable
        node_chosen_thistime = -1
        
        for i in range(0,len(distances)):
            if i == start:
                continue
            elif distances[i]["chosen"] == True:
                continue
            elif len(nodes_chosen) == 1 and dist[nodes_chosen[-1]][i] != unreachable:# first time
                distances[i]["through"] = distances[nodes_chosen[-1]]["through"] + [i]
                distances[i]["length"] = dist[nodes_chosen[-1]][i]
            elif distances[nodes_chosen[-1]]["length"] + dist[nodes_chosen[-1]][i] < distances[i]["length"]:
                distances[i]["through"] = distances[nodes_chosen[-1]]["through"] + [i]
                distances[i]["length"] = distances[nodes_chosen[-1]]["length"] + dist[nodes_chosen[-1]][i]
                
            if distances[i]["length"] < shortest_distance:
                node_chosen_thistime = i
                shortest_distance = distances[i]["length"]

        if shortest_distance == unreachable:
            break
        
        nodes_chosen.append(node_chosen_thistime)
        distances[node_chosen_thistime]["chosen"] = True
        
#    for i in range(0,len(distances)):
#        print "v{} {} {}".format(i,distances[i]["through"],distances[i]["length"])
#    print nodes_chosen
        
    return nodes_chosen


def main():
    dist = [[99999,99999,10,99999,30,100],
            [99999,99999,5,99999,99999,99999],
            [99999,99999,99999,50,99999,99999],
            [99999,99999,99999,99999,99999,10],
            [99999,99999,99999,20,99999,60],
            [99999,99999,99999,99999,99999,99999]]

    unreachable = 99999
    djikstra(dist,0,unreachable)
    

if __name__ == "__main__":
    main()