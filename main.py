"""
程序主入口
"""

from argparse import ArgumentParser

import matplotlib.pyplot as plt
import networkx as nx

from Controller import Controller
from Node import Node
from datasets import mnist


def main():
    # 解析命令行参数
    arg_parser = ArgumentParser('Distributed Optimization Simulator',
                                usage='一个分布式优化模拟器')
    arg_parser.add_argument('--direct', action='store_true', default=False,
                            help='如果加上该选项，则创建有向图')
    arg_parser.add_argument('--graphfile', default='', help='网络定义文件')
    arg_parser.add_argument('--nodenum', default=0, help='节点个数')
    args = arg_parser.parse_args()

    # 构建网络
    g = nx.DiGraph() if args.direct else nx.Graph()

    if args.graphfile:
        # 从文件导入网络结构
        with open(args.graphfile) as f:
            pass
    else:
        # 节点
        node_num = args.nodenum
        while node_num <= 0:
            node_num = int(input('请输入节点数：'))
        node_list = [Node('Node{}'.format(i + 1)) for i in range(node_num)]
        g.add_nodes_from([str(i) for i in list(range(1, node_num + 1))])

        # 边
        print('请输入网络的边，空格或换行符分割的数字对，如1,2 3,4')
        edge_list = []
        x = input('>')
        while x != '':
            edge_list.extend([t.split(',') for t in x.split()])
            x = input('>')
        g.add_edges_from(edge_list)

    # 日志
    print('网络生成成功')
    print('节点：', list(g.nodes))
    print('边：', list(g.edges))

    # 绘图
    plt.figure()
    nx.draw(g, with_labels=True, pos=nx.spring_layout(g))
    plt.show()

    # 数据
    x, y, _, _, _, _ = mnist(num_train=10000)

    # 创建控制器
    controller = Controller(g, node_list, {'x': x, 'y': y})

    # 分发数据
    controller.distribute_data()


if __name__ == '__main__':
    main()
