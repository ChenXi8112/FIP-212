"""10D01-编队坐标"""

def transform_points(S, R, points):
    return (S @ (R @ points.T)).T
