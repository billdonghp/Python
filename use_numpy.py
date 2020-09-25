import numpy as np
import pandas as pd
if __name__ == "__main__":
    s = np.random.randint(0, 100, size=(10, 10))  # numpy.ndarray
    print(s)
    print(f'f_max:{np.max(s)}')
    print(f'f_mean:{np.mean(s)}')
    print(type(s))

    s = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
    # print(s)
    print(s[:2, 0:3:2])  # 取行  列
    mlist = [[True, 3.14, 'hello'], [False, 26, 'world'],
             [True, 18, 'student']]
    data = pd.Series(mlist, index=['a', 'b', 'c'])
    print(data)

    s_Frame = pd.DataFrame(mlist, columns=['flag', 'number', 'string'])
    print(s_Frame)

    print(s_Frame['flag'])