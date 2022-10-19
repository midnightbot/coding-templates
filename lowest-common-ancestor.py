nodes = [p,q]
## find lowest common ancestor of nodes
def expand(self,root,nodes):
  if root == None:
      return None

  elif root in nodes:
      return root

  left = self.expand(root.left,nodes)
  right = self.expand(root.right,nodes)

  if left and right:
      return root

  elif left:
      return left
  elif right:
      return right
    
return self.expand(root,nodes)
