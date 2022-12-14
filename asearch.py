# -*- coding: utf-8 -*-
"""Asearch.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YRx26ZA5WGfjmvt4fxDEj3YQ_eBeNpcP
"""

import heapq
nodeDictionary = {0: 'S', 1: 'A', 2: 'B', 3: 'C', 4: 'D'}
adjList=[[[1,1],[2,4]],[[2,2],[3,5],[4,12]],[[3,2]],[[4,3]],[]]
hlist=[7,6,2,1,0]
qlist=[]
pathrecordlist=[]
class node:
    def __init__(self, nodeNumber, previousNode, actual_cost, total_cost):
        self.nodeNumber = nodeNumber
        self.previousNode = previousNode
        self.actual_cost = actual_cost
        self.total_cost = total_cost

    def __lt__(self, new):
        return self.total_cost < new.total_cost

First_node = node(0,None,0,7)

heapq.heappush(qlist,First_node)
while qlist:
  x_node = heapq.heappop(qlist)
  if x_node.nodeNumber== 4: 
    print(x_node.actual_cost)
    pathrecordlist.append(x_node.nodeNumber)
    while x_node.previousNode != None:
      pathrecordlist.append(x_node.previousNode.nodeNumber)
      x_node = x_node.previousNode
    for j in reversed(range(len(pathrecordlist))):
      print(nodeDictionary[pathrecordlist[j]])
    break
  for p in range(len(adjList[x_node.nodeNumber])): 
    newnodeNumber = adjList[x_node.nodeNumber][p][0] 
    newpreviousNode = x_node 
    newactual_cost = x_node.actual_cost + adjList[x_node.nodeNumber][p][1]
    newtotal_cost = hlist[newnodeNumber] + newactual_cost

    newNode = node(newnodeNumber, newpreviousNode,newactual_cost, newtotal_cost)
    heapq.heappush(qlist, newNode)