class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        # rec1 is completely to the left of rec2
        if rec1[2] <= rec2[0]:
            return False

        # rec2 is completely to the left of rec1
        if rec2[2] <= rec1[0]:
            return False

        # rec1 is completely below rec2
        if rec1[3] <= rec2[1]:
            return False

        # rec2 is completely below rec1
        if rec2[3] <= rec1[1]:
            return False

        return True