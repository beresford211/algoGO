
def minDepthOfaBinaryTree(node):
    min_val = float("inf")
    
    def crawlNodes(n, v):

        if n.left:
            crawlNodes(n.left, v + 1)
        
        if n.right:
            crawlNodes(n.right, v + 1)

        if n.left is None and n.right is None:
            min_val = min(min_val, v)

    crawlNodes(node, 1)
