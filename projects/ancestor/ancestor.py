# Write a function that, given the dataset and the ID of an individual in the dataset, 
# returns their earliest known ancestor – the one at the farthest distance from the input
# individual. If there is more than one ancestor tied for "earliest", return the one 
# with the lowest numeric ID. If the input individual has no parents, the function should 
# return -1.

# import sys
# sys.path.append('../graph')
# from graph import Graph
# from util import Queue, Stack

def earliest_ancestor(ancestors, root, parent=None):
    # if starting node in tree
    if root in [v[1] for v in ancestors]:
        # iterate thru tree
        for i in ancestors:
            # starting node
            if root == i[1]:
                # when starting node found iterate up tree to lca
                return earliest_ancestor(ancestors, i[0], parent=True)

    # when lca reached        
    elif parent == True:
        return root

    else:
        # no lca found, input node has no parents
        return -1


# Pseudocode
# instantiate graph, add vertices/nodes to graph
# add edges to graph, child -> parent direction
# instantiate queue, add a path from the starting node to queue
# instantiate set
# while queue not empty, dequeue 1st path
# grab last vertex from path

############
# actually i can avoid all of this with recursive implementaiton and adding another input

if __name__ == "__main__":
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), 
                        (5, 7), (4, 5), (4, 8),
                        (8, 9), (11, 8), (10, 1)]


    print(earliest_ancestor(test_ancestors, 1))
    print(earliest_ancestor(test_ancestors, 2))
    print(earliest_ancestor(test_ancestors, 3))
    print(earliest_ancestor(test_ancestors, 4))
    print(earliest_ancestor(test_ancestors, 5))
    print(earliest_ancestor(test_ancestors, 6))
    print(earliest_ancestor(test_ancestors, 7))
    print(earliest_ancestor(test_ancestors, 8))
    print(earliest_ancestor(test_ancestors, 9))
    print(earliest_ancestor(test_ancestors, 10))
    print(earliest_ancestor(test_ancestors, 11))