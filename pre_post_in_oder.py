self.ans = []
        
        
def preorder(root):
  if root is not None:
    self.ans.append(root.val)

    if root.left:
      preorder(root.left)

    if root.right:
      preorder(root.right)

        
def postorder(root):
  if root is not None:
    if root.left:
      postorder(root.left)

    if root.right:
      postorder(root.right)


    self.ans.append(root.val)
    
    
    
def inorder(root):          
  if root is not None:
    if root.left:
      inorder(root.left)

    self.ans.append(root.val)

    if root.right:
      inorder(root.right)
