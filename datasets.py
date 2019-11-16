'''
    数据集
    使用示例
        trainX, trainY, testX, testY = mnist(noTrSamples=500, noTsSamples=200, digits=[3,8,9,2])
'''
import numpy as np


def mnist(num_train=2000, num_val=200, num_test=1000, digits=[3, 8]):
    """
    生成数据集，数据量为总量
    :param num_train: 训练集数据量
    :param num_val: 验证集数据量
    :param num_test: 测试集数据量
    :param digits: 需要的数字
    :return: 训练集数据(num_train*784)，训练集标签(num_train,)，测试集数据，测试集标签，验证集数据，验证集标签
    """
    # 读取数据
    fd = open('data/train-images.idx3-ubyte')
    loaded = np.fromfile(file=fd, dtype=np.uint8)
    train_data = loaded[16:].reshape((60000, 28 * 28)).astype(float)

    fd = open('data/train-labels.idx1-ubyte')
    loaded = np.fromfile(file=fd, dtype=np.uint8)
    train_label = loaded[8:].reshape((60000)).astype(float)

    fd = open('data/t10k-images.idx3-ubyte')
    loaded = np.fromfile(file=fd, dtype=np.uint8)
    test_data = loaded[16:].reshape((10000, 28 * 28)).astype(float)

    fd = open('data/t10k-labels.idx1-ubyte')
    loaded = np.fromfile(file=fd, dtype=np.uint8)
    test_label = loaded[8:].reshape((10000)).astype(float)

    # 将数据压缩到0-1之间
    train_data = train_data / 255.0
    test_data = test_data / 255.0

    trX = np.zeros((num_train, 28 * 28))
    tsX = np.zeros((num_test, 28 * 28))
    valX = np.zeros((num_val, 28 * 28))
    trY = np.zeros(num_train)
    tsY = np.zeros(num_test)
    valY = np.zeros(num_val)

    # 每一类选出一样多的数据
    if num_train % len(digits) != 0:
        raise ValueError(
            "训练集总数不能整除数字类别数!")
    else:
        num_train_per_class = num_train // len(digits)

    if num_test % len(digits) != 0:
        raise ValueError(
            "测试集总数不能整除数字类别数!")
    else:
        num_test_per_class = num_test // len(digits)

    if num_val % len(digits) != 0:
        raise ValueError(
            "验证集总数不能整除数字类别数!")
    else:
        num_val_per_class = num_val // len(digits)

    count = 0
    for di in digits:
        # 训练集
        idl = np.where(train_label == di)[0]
        np.random.shuffle(idl)
        idl_ = idl[: num_train_per_class]
        idx = list(range(count * num_train_per_class, (count + 1) * num_train_per_class))
        trX[idx, :] = train_data[idl_, :]
        trY[idx] = train_label[idl_]

        # 验证集
        valIdl = idl[num_train_per_class:num_train_per_class + num_val_per_class]
        idx = list(range(count * num_val_per_class, (count + 1) * num_val_per_class))
        valX[idx, :] = train_data[valIdl, :]
        valY[idx] = train_label[valIdl]

        # 测试集
        idl = np.where(test_label == di)[0]
        np.random.shuffle(idl)
        idl = idl[: num_test_per_class]
        idx = list(range(count * num_test_per_class, (count + 1) * num_test_per_class))
        tsX[idx, :] = test_data[idl, :]
        tsY[idx] = test_label[idl]
        count += 1

    # 数据重新排列
    train_idx = np.random.permutation(trX.shape[0])
    trX = trX[train_idx, :]
    trY = trY[train_idx]

    val_idx = np.random.permutation(valX.shape[0])
    valX = valX[val_idx, :]
    valY = valY[val_idx]

    test_idx = np.random.permutation(tsX.shape[0])
    tsX = tsX[test_idx, :]
    tsY = tsY[test_idx]

    return trX, trY, tsX, tsY, valX, valY
