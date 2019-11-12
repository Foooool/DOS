"""
    主控制器
"""


class Controller(object):
    """
        主控制器
    """

    def __init__(self, graph=None, data=None, convergence_threshold=0.01):
        """
        初始化
        :param graph: 网络图
        :param data: 总数据
        :param convergence_threshold: 收敛性阈值
        """
        self.graph = graph
        self.data = data
        self.convergence_threshold = convergence_threshold