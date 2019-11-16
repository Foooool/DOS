"""
    节点虚基类
"""


class Node(object):
    """
        节点基类
        实现时，您应该继承这个类并实现必要的方法
    """

    def __init__(self, name, data=None, eta=0.01, batch_size=16):
        """
        初始化，继承时根据需要添加自定义参数
        :param name: 节点名称
        :param data: 节点的私有数据集
        :param eta: 初始学习率
        :param batch_size:  batch size
        """
        self.name = name
        self.data = data
        self.eta = eta
        self.batch_size = batch_size

        self.receive_buffer = []

    def set_data(self, data):
        """
        设置数据
        :param data: 数据
        """
        self.data = data
        print('[+]\t节点{}接受到数据{}'.format(self.name, self.data['x'].shape))

    def step(self):
        """
        进行一次算法迭代
        """
        pass

    def send(self):
        """
        发送参数给邻居节点
        :return: 参数
        """
        pass

    def receive(self, data):
        """
        接受参数
        :param data:  接受邻居发来的参数
        """
        self.receive_buffer.append(data)

    def __str__(self):
        return self.name


class DGDNode(Node):
    """
    DGD算法实现类
    """
