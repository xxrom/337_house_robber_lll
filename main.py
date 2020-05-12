from typing import List


class Node:

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:

  def rob(self, root: Node) -> int:
    return 0


my = Solution()

n = Node(3, Node(2, None, Node(3)), Node(3, Node(1)))
ans = my.rob(n)
print("ans", ans)
'''
       3(c)
     /     \
   2(b)    3(d)
  /    \       \
2(f)   3(a)   1(e)
'''
