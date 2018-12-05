"""
graphiz图代码生成器
"""

class GzDigraphWriter:
    """
    graphviz代码生成
    """
    def __init__(self, name):
        self.name = name
        self.__code_list = list()
        self.__code_list.append("digraph " + name + "{")
        self.__code_list.append("ordering = in;")

    def add_edge(self, name1, name2):
        """在digraph上添加边"""
        self.__code_list.append(name1 + " -> " + name2 + ";")

    def set_node(self, name, color="black"):
        """在digraph中设置节点颜色"""
        code = name + " [color=" + color + "];"
        self.__code_list.append(code)

    def get_codes(self):
        """获取代码"""
        return self.__code_list + ["}"]
