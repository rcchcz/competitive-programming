# https://leetcode.com/problems/bulb-switcher/
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))  

'''
Approach 1: Math
Intuition
The idea behind this problem is to find the number of bulbs
that are on after n rounds. In each round, we toggle some
of the bulbs.

As all the bulbs are initially off, at the end only bulbs that
are toggled an odd number of times will remain on.
Now, whenever we are at a round i we know we toggle all
bulbs having a factor i. Thus, we need to find the bulbs
which have an odd number of factors, as those bulbs will be
toggled an odd number of times (once by each factor).

It might be unintuitive, but with a few examples, we can
easily see that a perfect square number has an odd number
of factors, since any number's factors come in pairs of two
different numbers, but the square root of the number will be
paired with itself.

Let's take an example to make it more clear. Suppose n = 10.
So, the number of rounds is 10. In each round, we will toggle
some of the bulbs.

(...)

So, taking the floor value of the square root of n will give us
the number of perfect squares in the range 1 to n.
Hence, sqrt(n) is our answer to this problem.
'''  