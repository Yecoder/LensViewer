# -------------------------------------------------------------------------
# Target:计算双透镜组合的组合焦距
# Input:透镜1的焦距Focallength1，透镜2的焦距Focallength2，透镜间距Distance
#
# Output:组合透镜的焦距
#
# Test:
#
# Author:Ye
# Contact:yehk2019@163.com
# Date:2023/3/16 18:19
# -------------------------------------------------------------------------
"""
文件说明：
"""


def DoubleThinLensCombination(FocalLength1, FocalLength2, Distance):
    OpticalPower1 = 1 / FocalLength1
    OpticalPower2 = 1 / FocalLength2
    CombinedOpticalPower = OpticalPower1 + OpticalPower2 - OpticalPower1 * OpticalPower2 * Distance
    CombinedFocalLength = 1 / CombinedOpticalPower
    return CombinedOpticalPower, CombinedFocalLength
