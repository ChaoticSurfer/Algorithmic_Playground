from collections import deque

class Node:
    def __init__(self, previous_node, result, index, operation):
        self.index = index
        self.previous_node = previous_node
        self.result = result
        self.operation = operation


frontier = deque()
l = [9, 8, 7, 6, 5, 4, 3, 2, 1]
frontier.append(Node(None, l[0], 0, "init"))
result = None
counter = 0
while len(frontier) != 0:
    node = frontier.pop()
    index = node.index
    new_index = index + 1

    if new_index == len(l):
        if node.result == 2023:
            result = node
            break
        continue
    frontier.append(Node(node, node.result + l[new_index], new_index, "+"))
    frontier.append(Node(node, node.result - l[new_index], new_index, "-"))
    frontier.append(Node(node, node.result / l[new_index], new_index, "/"))
    frontier.append(Node(node, node.result * l[new_index], new_index, "*"))

r = []
node = result
while node.previous_node is not None:
    r.append(node.operation)
    node = node.previous_node
print(list(reversed(r)))
