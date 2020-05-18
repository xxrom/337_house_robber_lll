from typing import List


class Node:

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:

  def isLeaf(self, node: Node) -> bool:
    if node.left == None and node.right == None:
      return True
    return False

  def maxChildSum(self, node: Node, withNode: bool) -> int:
    # if withNode == True => find only in '0' positions
    # if withNOde == False => find anywhere ['0', '1']

    rightNode = None
    leftNode = None

    if node.right != None:
      rightNode = self.dist[node.right]
    if node.left != None:
      leftNode = self.dist[node.left]

    rightSum = 0
    leftSum = 0

    if withNode == True:
      if rightNode != None:
        rightSum = rightNode['0']['sum']
      if leftNode != None:
        leftSum = leftNode['0']['sum']

    else:
      if rightNode != None:
        rightSum = rightNode['1']['sum']
        if rightNode['0']['sum'] > rightNode['1']['sum']:
          rightSum = rightNode['0']['sum']

      if leftNode != None:
        leftSum = leftNode['1']['sum']
        if leftNode['0']['sum'] > leftNode['1']['sum']:
          leftSum = leftNode['0']['sum']

    maxValue = max(rightSum, leftSum)
    print('maxChild at %d = %d [r=%d, l=%d]' %
          (node.val, maxValue, rightSum, leftSum))

    return maxValue

  def fill(self, node: Node, level=0) -> None:
    if node == None:
      return

    if node not in self.dist:
      # Init self.dist obj
      self.dist[node] = {
          '0': {
              'path': str(level),
              'sum': 0
          },
          '1': {
              'path': str(level),
              'sum': 0
          },
      }

    print(node.val)

    if self.isLeaf(node):

      # Fill self.dist
      self.dist[node]['1'] = {'path': str(node.val), 'sum': node.val}
      print('leaf reached', node.val, self.dist[node])
      return

    else:
      self.fill(node.right, level + 1)
      self.fill(node.left, level + 1)

      self.dist[node] = {
          '0': {
              'path': '+',
              'sum': self.maxChildSum(node, False)
          },
          '1': {
              'path': '+',
              'sum': node.val + self.maxChildSum(node, True)
          }
      }

      return

  def rob(self, root: Node) -> int:
    self.dist = {}

    self.fill(root)
    print(self.dist[root])

    return 0


my = Solution()

n = Node(3, Node(2, Node(2), Node(3)), Node(3, Node(1)))
ans = my.rob(n)
print("ans", ans)
'''
       3(c)
     /     \
   2(b)    3(d)
  /    \       \
2(f)   3(a)   1(e)
'''
