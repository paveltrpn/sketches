
from math import cos, sin
from common import IdRw

class mtrx3List(object):
    __slots__ = ["data"]
    
    def __init__(self) -> None:
        self.data = [float(x-x) for x in range(9)]

    def __setitem__(self, key: int, value: float):
        self.data[key] = value

    def __getitem__(self, key: int) -> float:
        return self.data[key]

def mtrx3ListFromEuler(yaw: float, pitch: float, roll: float) -> mtrx3List:
    cosy = cos(yaw)
    siny = sin(yaw)
    cosp = cos(pitch)
    sinp = sin(pitch)
    cosr = cos(roll)
    sinr = sin(roll)

    rt = mtrx3List()

    rt[0] = cosy*cosr - siny*cosp*sinr
    rt[1] = -cosy*sinr - siny*cosp*cosr
    rt[2] = siny * sinp

    rt[3] = siny*cosr + cosy*cosp*sinr
    rt[4] = -siny*sinr + cosy*cosp*cosr
    rt[5] = -cosy * sinp

    rt[6] = sinp * sinr
    rt[7] = sinp * cosr
    rt[8] = cosp

    return rt

class CVec3List(object):
    __slots__ = ["data", "capacity", "dataSize"]
    
    def __init__(self, arr: list) -> None:
        if not (len(arr)%3 == 0):
            print("CVec3Arrayf(): WARNING! Initial array lenght is not in rate of 3!")

        self.data = [float(elem) for elem in arr]
        self.capacity = len(arr)
        self.dataSize = len(arr)*4 # size of array.array("f", [...]) element is 4 bytes 

    def applyMtrx3Naive(self, A: mtrx3List) -> None:
        """Perform multiplication of internal array of vector3 by a matrix3x3.

        :type A: matrix 3 by 3
        """
        for arId in range(0, self.capacity, 3):
            for i in range(3): 
                tmp = 0
                for j in range(3):
                	tmp = tmp + A[IdRw(i, j, 3)]*self.data[arId+j]
                self.data[arId+i] = tmp
    
    def applyMtrx3(self, A: mtrx3List) -> None:
        for arId in range(0, self.capacity, 3):
            x = self.data[arId+0]
            y = self.data[arId+1]
            z = self.data[arId+2]
            
            self.data[arId+0] = x * A[0] + y * A[3] + z * A[6]
            self.data[arId+1] = x * A[1] + y * A[4] + z * A[7]
            self.data[arId+2] = x * A[2] + y * A[5] + z * A[8]
            