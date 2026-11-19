"""10D02-最近影友"""

import numpy as np

def best_match(ratings, user_id):
    # 归一化
    norms = np.linalg.norm(ratings, axis=1, keepdims=True)
    normalized = ratings / norms

    # 批量求相似度
    cosines = normalized @ normalized.T

    # 复制候选数组并去掉自己
    candidates = cosines[user_id - 1].copy()    # 编号 = 索引 + 1
    candidates[user_id - 1] = -1
    best_id = candidates.argmax()

    return best_id + 1, candidates[best_id]     # 编号 = 索引 + 1


if __name__ == '__main__':
    ratings = np.array([[5, 1, 2, 4],
                        [4, 2, 1, 5],
                        [1, 5, 5, 1],
                        [5, 1, 2, 4],
                        [3, 3, 3, 3]])
    best_id, sim = best_match(ratings, 1)
    print(f"{best_id} {sim:.3f}")
