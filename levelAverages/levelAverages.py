from collections import deque

def levelAverages(node):

    if node.val is None:
        return []

    queue = deque()
    queue.append(node)
    arr = []
    while (len(queue) > 0):
        len_count = len(queue)
        total = 0

        for _ in range(len(queue)):
            c_node = queue.popleft()
            total += c_node.val 
            if c_node.left:
                queue.append(c_node.left)
            elif c_node.right:
                queue.append(c_node.right)

        arr.append(total/len_count)
