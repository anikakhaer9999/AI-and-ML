# -*- coding: utf-8 -*-
"""simulatedanneling.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KfXb_PZ7V1mrD0Tr1TBJ2yDmuMj1CFuD
"""

import random
def calc_cost(state):
  cost = 0
  for i in range(len(state)):
    for j in range(i+1,len(state)):
      if state[i]>state[j]:
        cost = cost+1
  return cost
  

def State_generation(current_state, current_state_cost):
  copy_current_state = list.copy(current_state)
  smallest_cost = float('inf')
  i = random.randint(0,len(state)-1)
  j = random.randint(0, len(state)-1)
  current_state[i], current_state[j] = current_state[j], current_state[i]
  current_cost = calc_cost(current_state)
  if smallest_cost > current_cost:
    smallest_state = list.copy(current_state)
    smallest_cost = current_cost
    return smallest_state, smallest_cost
  else:
    deltae = current_cost - cost
    prob = pow(2.71828, (deltae))
    rand_def = random.random()
    if rand_def < prob:
      smallest_state = list.copy(current_state)
      smallest_cost = current_cost
      return smallest_state, smallest_cost
    else:
      return smallest_state, smallest_cost


def goal_test(state):
	if calc_cost(state) == 0:
		return True
	else:
		return False

#state = [2, 1, 5, 0, 8, 4, 10, 0, 20, 10]
state = [2, 1, 5, 0, 8]
cost = calc_cost(state)

while goal_test(state) == False:
  state,cost = State_generation(state,cost)
print(state)
print(cost)