"""10D01-编队坐标"""

import numpy as np

def transform_points(S, R, points):
    return (S @ (R @ points.T)).T


if __name__ == '__main__':
    # 输出用例：绕原点逆时针旋转 90°，再 x 放大 2 倍、y 放大 3 倍
    S = np.array([[2, 0],
                  [0, 3]])
    R = np.array([[0, -1],
                  [1, 0]])
    points = np.array([[1, 0],
                       [0, 1],
                       [1, 1],
                       [-1, 2]])

    print(transform_points(S, R, points))
    # [[ 0  3]
    #  [-2  0]
    #  [-2  3]
    #  [-4 -3]]
