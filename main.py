class Node:

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:

  def isLeaf(self, node: Node) -> bool:
    return node.left == None and node.right == None

  def maxChildSumArray(self,
                       rightChild=[0, 0],
                       leftChild=[0, 0],
                       includeCurrentNode=False) -> int:
    # if withNode == True => find only in '0' positions
    # if withNOde == False => find anywhere ['0', '1']
    return ((rightChild[0] + leftChild[0]) if includeCurrentNode == True else
            (max(rightChild) + max(leftChild)))

  def fill(self, node: Node) -> [float, float]:
    if node == None:
      node = Node()

    if self.isLeaf(node):
      return [0, node.val]
    else:
      rightChildSum = self.fill(node.right)
      leftChildSum = self.fill(node.left)

      return [
          self.maxChildSumArray(rightChildSum, leftChildSum, False),
          node.val + self.maxChildSumArray(rightChildSum, leftChildSum, True)
      ]

  def rob(self, root: Node) -> int:
    return max(self.fill(root))


my = Solution()

# n = Node(3, Node(2, Node(3)), Node(3, Node(1)))
n = Node(3, Node(20, Node(0), Node(3)), Node(3, Node(1)))
ans = my.rob(n)
print("ans", ans)

# URL: https://leetcode.com/problems/house-robber-iii/discuss/376297/Python3-Dynamic-Programming-%2B-Depth-First-Search
# TODO: optimize => without self.dist object and return just two number and compare them =)
'''
       3(c)
     /     \
   2(b)    3(d)
  /    \       \
0.5(f)   3(a)   1(e)
'''

# Old version with self.dist map
# Runtime: 96 ms, faster than 5.36% of Python3 online Nodesubmissions for House Robber III.
# Memory Usage: 24.1 MB, less than 6.67% of Python3 online Nodesubmissions for House Robber III.

# Light way without self.dist object (optimized)
# Runtime: 44 ms, faster than 89.45% of Python3 online submissions for House Robber III.
# Memory Usage: 16 MB, less than 33.33% of Python3 online submissions for House Robber III.