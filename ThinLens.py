# -------------------------------------------------------------------------
# Target:计算薄透镜的光焦度
# Input:
#           
# Output:
#
# Test:
#
# Author:Ye
# Contact:yehk2019@163.com
# Date:2023/3/17 13:19
# -------------------------------------------------------------------------
"""
文件说明：
"""


class ThinLens:
    C1 = 0
    C2 = 0
    t = 0
    n = 1.5

    def phi(self):
        phi = (self.n - 1) * (self.C1 - self.C2)
        return phi

    def d1(self):
        d1 = 0
        return d1

    def d2(self):
        d2 = 0
        return d2

