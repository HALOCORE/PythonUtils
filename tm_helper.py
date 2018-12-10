"""计时辅助模块"""
from . import utility
import matplotlib.pyplot as plt

def get_average_time_from_timetxt(filename):
    """
    从time.txt读取得到平均时间
    """
    lines = utility.get_lines_from_file(filename)
    datas = [[float(x.strip()) for x in line.split(",")] for line in lines]
    avers = [sum(one)/len(one) for one in zip(*datas)]
    return avers


def get_time_in_theory(func, scales, real_max_time):
    """
    计算理论用时.
    func是一个传入函数，参数为规模scale，返回值与时间成正比;
    scales是规模列表，每一项作为func的输入;
    real_max_time 给出最大规模的真实时间，好按比例计算理论时间。
    返回：理论时间列表，与scales对应。
    (假定：scales的最后一个是最大的)
    """
    theo_times = [func(scale) for scale in scales]
    ratio = real_max_time / theo_times[-1]
    theo_times = [t*ratio for t in theo_times]
    return theo_times


def plot_time_graph(scales, real_times, theo_times, m_title, 
                    m_xlabel="scale", m_ylabel="time (s)"):
    """
    绘制时间比较图像
    """
    plt.plot(scales, real_times)
    plt.plot(scales, theo_times)
    plt.legend(["real", "theory"], loc="upper left")
    plt.title(m_title)
    plt.xlabel(m_xlabel)
    plt.ylabel(m_ylabel)
    plt.ylim(ymin=0)
    plt.show()
