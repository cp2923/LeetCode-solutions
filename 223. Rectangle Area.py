class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        leftX = max(A,E)
        leftY = max(B,F)
        rightX = min(C,G)
        rightY = min(D,H)

        area = (C-A) *(D-B) +(G-E) * (H-F)

        if rightX > leftX and rightY > leftY:
            return area - (rightX - leftX) * (rightY - leftY)
        else:
            return area
