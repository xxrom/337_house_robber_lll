```tsx
       3(c)
     /     \
   2(b)    3(d)
  /    \       \
2(f)   3(a)   1(e)


a = {
  0: { path: None, sum: 0},
  1: { path: a, sum: 3}
},
f = {
  0: { path: None, sum: 0},
  1: { path: f, sum: 2},
}
to parent -> 1
b = {
  # maxChildSum - 1 => any, 0 - only 0 (without node)
  0: { path: _- + maxChildSum(1) [3(a->1)], sum: 3},
  1: { path: b- + maxChildSum(0) [0], sum: 2}
}
to parent -> c (root) -> go to leaf in right child

e = {
  0: { path: None, sum: 0},
  1: { path: e, sum: 1},
},
to parent -> d
d = {
  0: { path: _- + maxChildSum(1) [e->1], sum: 1},
  1: { path: d- + macChildSum(0) [None], sum: 3}
}
to parent -> c (root)

c = {
  0: { path: _- + maxChildSum(1) [left->[b->0=3], right->[d->1=3]], sum: 3+3 = 6},
  1: { path: c- + maxChildSum(0) [left->[b->0=3], right->[d->0=1]], sum: 3+1+3(c) = 7} <- ans
}

---

leaf - root

path0 - without root
path1 - with root
{
  node: root,
  path0: _-2-_,
  maxSum0: 2,
  path1: 3-_-3,
  maxSum1: 6,
},
{
  node: 2,
  path0: 3-_,
  maxSum0: 3,
  path1: _-2,
  maxSum1: 2,
}

```