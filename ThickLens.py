# -------------------------------------------------------------------------
# Target:计算厚透镜的光焦度
# Input:
#           
# Output:
#
# Test:
#
# Author:Ye
# Contact:yehk2019@163.com
# Date:2023/3/17 11:30
# -------------------------------------------------------------------------
"""
文件说明：
"""


class ThickLens:
    C1 = 0
    C2 = 0
    t = 10
    n = 1.5

    def __init__(self, C1, C2, t, n):
        self.C1 = C1
        self.C2 = C2
        self.t = t
        self.n = n

    def tau(self):
        tau = self.t / self.n
        return tau

    def phi1(self):
        phi1 = (self.n - 1) * self.C1
        return phi1

    def phi2(self):
        phi2 = - (self.n - 1) * self.C2
        return phi2

    def phi(self):
        tau = self.tau()
        phi = (self.n - 1) * (self.C1 - self.C2 + (self.n - 1) * self.C1 * self.C2 * tau)
        return phi

    def d1(self):
        d1 = self.phi2() / self.phi() * self.tau()
        return d1

    def d2(self):
        d2 = - self.phi1() / self.phi() * self.tau()
        return d2
