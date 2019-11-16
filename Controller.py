"""
    主控制器
"""


class Controller(object):
    """
        主控制器
    """

    def __init__(self, graph=None, node_list=None, data=None, convergence_threshold=0.01):
        """
        初始化
        :param graph: 网络图 nx.Graph
        :param node_list: 节点列表
        :param data: 总数据，字典格式，键为'x'和'y'，值为 ndarray 格式 {'x': x, 'y': y}
        :param convergence_threshold: 收敛性阈值，浮点数
        """
        self.graph = graph
        self.node_list = node_list
        self.data = data
        self.convergence_threshold = convergence_threshold

    def distribute_data(self):
        """
        将数据分发到各个节点上
        这里随机平均分配，可以根据需要调整
        """
        num_node = len(self.node_list)
        data_per_node = self.data['x'].shape[0] // num_node

        for ni in range(num_node):
            node_data = {'x': self.data['x'][ni * data_per_node:(ni + 1) * data_per_node],
                         'y': self.data['y'][ni * data_per_node:(ni + 1) * data_per_node]}
            self.node_list[ni].set_data(node_data)
