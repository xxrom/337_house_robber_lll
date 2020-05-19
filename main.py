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
        rightSum = rightNode['miss']['sum']
      if leftNode != None:
        leftSum = leftNode['miss']['sum']

    else:
      if rightNode != None:
        rightSum = rightNode['include']['sum']
        if rightNode['miss']['sum'] > rightSum:
          rightSum = rightNode['miss']['sum']

      if leftNode != None:
        leftSum = leftNode['include']['sum']
        if leftNode['miss']['sum'] > leftSum:
          leftSum = leftNode['miss']['sum']

    maxValue = rightSum + leftSum
    print('maxChild (%s) at %.2f = %.2f [r=%.2f, l=%.2f]' %
          (withNode, node.val, maxValue, rightSum, leftSum))

    return maxValue

  def fill(self, node: Node) -> None:
    if node == None:
      return

    if node not in self.dist:
      # Init self.dist obj
      self.dist[node] = {
          'miss': {
              'sum': 0
          },
          'include': {
              'sum': 0
          },
      }

    print(node.val)

    if self.isLeaf(node):

      # Fill self.dist
      self.dist[node]['include'] = {'sum': node.val}
      print('leaf reached', node.val)
      print(self.dist[node])
      return

    else:
      self.fill(node.right)
      self.fill(node.left)

      self.dist[node] = {
          'miss': {
              'sum': self.maxChildSum(node, False)
          },
          'include': {
              'sum': node.val + self.maxChildSum(node, True)
          }
      }

      return

  def rob(self, root: Node) -> int:
    if root == None:
      return 0

    self.dist = {}

    self.fill(root)
    print(self.dist[root])

    rootItem = self.dist[root]

    return rootItem['miss']['sum'] if rootItem['miss']['sum'] > rootItem[
        'include']['sum'] else rootItem['include']['sum']


my = Solution()

n = Node(3, Node(2, Node(3)), Node(3, Node(1)))
# n = Node(3, Node(20, Node(0), Node(3)), Node(3, Node(1)))
ans = my.rob(n)
print("ans", ans)
'''
       3(c)
     /     \
   2(b)    3(d)
  /    \       \
0.5(f)   3(a)   1(e)
'''

# Runtime: 96 ms, faster than 5.36% of Python3 online submissions for House Robber III.
# Memory Usage: 24.1 MB, less than 6.67% of Python3 online submissions for House Robber III.
