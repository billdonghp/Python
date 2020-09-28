import numpy as np
import pandas as pd


def npRandom():
    s = np.random.randint(0, 100, size=(10, 10))  # numpy.ndarray
    print(s)
    print(f'f_max:{np.max(s)}')
    print(f'f_mean:{np.mean(s)}')
    print(type(s))


def npSum():
    print(s.sum())  # 所有元素进行求和
    print(s.sum(axis=0))  # 矩阵每一列相加
    print(s.sum(axis=1))  # 矩阵的每一行相加


def npSub():
    print(s[:2, 0:3:2])  # 取行 , 列


def pdSeries():
    data = pd.Series(mlist, index=['a', 'b', 'c'])
    print(data)


def pdDataFrame():
    s_Frame = pd.DataFrame(mlist, columns=['flag', 'number', 'string'])
    print(s_Frame)
    print('-' * 30)
    print(s_Frame['flag'])


def dfInfo():
    df = pd.DataFrame(
        {
            'id': [
                1001, 1002, 1003, 1001, 1004, 1005, 1006, 1007, 1008, 1009,
                1010, 1011, 1012
            ],
            'data':
            pd.date_range('20120102', periods=13),
            'name': [
                'java', 'python', 'c++', 'Groovy', '', '', '', '', '', '', '',
                '', ''
            ],
            'price':
            list(range(13))
        },
        columns=['id', 'data', 'name', 'price'])
    print(df.shape)  # 维度查看
    print(df.info())  # 数据表基本信息（维度、列名称、数据格式、所占空间等）
    print('-' * 30)
    print(df.dtypes)  # 每一列数据的格式
    print(df['name'].dtypes)  # 某列数据格式
    print('-' * 30)
    print(df.isnull())  # 是否为空
    print(df['name'].isnull())  # 某列是否为空

    print('-' * 30)
    print(df['id'].unique())  # 某列唯一值
    print(df.values)  # 查看数据表的值
    print(df.columns)  # 查看列名称
    # 查看前5行，后5行
    print(df.head())
    print(df.tail())


if __name__ == "__main__":
    # npRandom()
    s = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
    # npSum()
    # npSub()
    mlist = [[True, 3.14, 'hello'], [False, 26, 'world'],
             [True, 18, 'student']]
    # pdSeries()

    # pdDataFrame()
    # dfInfo()
    df = pd.read_excel('tmp001.xlsx')
    # 提取单行数据 Series
    print(type(df.loc[3]))
    # 按索引提取区域行数据 DataFrame
    print(type(df.loc[2:4]))
    # 使用iloc按位置区域提取数据 DataFrame
    print(type(df.iloc[:3, :2]))
    print(df.shape[0])
    for i in range(int(df.shape[0])):
        df.loc[i]['result'] = df.loc[i]['代理商']
        #print(i, dealer)
    #df.to_excel('excel_to_python.xlsx', sheet_name='bluewhale_cc')
    print(df)