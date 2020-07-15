# import sys
# sys.path.append('../graph')

from graph import Graph
from util import Queue, Stack

# Write a function that, given the dataset and the ID of an individual in the dataset, 
# returns their earliest known ancestor – the one at the farthest distance from the input
# individual. If there is more than one ancestor tied for "earliest", return the one 
# with the lowest numeric ID. If the input individual has no parents, the function should 
# return -1.


def earliest_ancestor(ancestors, root):
