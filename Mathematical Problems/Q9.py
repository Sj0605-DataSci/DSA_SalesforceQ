'''
593. Valid Square - Medium

Given the coordinates of four points in 2D space p1, p2, p3 and p4, 
return true if the four points construct a square.

The coordinate of a point pi is represented as [xi, yi]. 
The input is not given in any order.

A valid square has four equal sides with positive length and 
four equal angles (90-degree angles).

Example 1:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: true
Example 2:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
Output: false

'''

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        res=0
        def l(a,b):
            length=(((a[0]-b[0])**2)+((a[1]-b[1])**2))
            return length
        d=[l(p1,p2),l(p1,p3),l(p1,p4),l(p2,p3),l(p2,p4),l(p3,p4)]
        d.sort()
        return True if 0<d[0]==d[1]==d[2]==d[3] and d[4]==d[5] else False 

