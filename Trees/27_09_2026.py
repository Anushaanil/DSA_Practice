def averageOfLevels(root: TreeNode | None) -> list[float]:
    ans = []
    queue = [root]
    
    while queue:
        cur = queue.popleft()
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
        
        ans.append(cur.val)
        
    return ans