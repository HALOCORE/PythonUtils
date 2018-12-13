"""
实用函数
"""
import os
import random
import csv


def get_abs_filename(filename, debug=False):
    """
    以当前utility.py所在目录为根据，获取绝对路径
    """
    my_path = os.path.abspath(os.path.join(os.path.dirname(__file__), filename))
    if debug:
        print("# 获取绝对路径: ", str(my_path))
    return my_path


def get_lines_from_file(filename, debug=True):
    """
    从文件读取得到行数组
    """
    filename = get_abs_filename(filename)
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    if debug:
        print("# get_lines_from_file: 文件名 %s, 行数 %d. 读取完成。" % (filename, len(lines)))
    file.close()
    return lines


def get_file_content(filename: str, debug=True):
    """读取全部文件内容"""
    filename = get_abs_filename(filename)
    file = open(filename, 'r')
    content = file.read()
    if debug:
        print("# get_file_content: 文件名 %s, 内容长度 %d. 读取完成。" % (filename, len(content)))
    file.close()
    return content


def write_lines_to_file(filename, data, debug=True):
    """
    将数据列表写入文件
    """
    filename = get_abs_filename(filename)
    filepath = get_path_in_filename(filename)
    ensure_path(filepath)
    file = open(filename, 'w')
    write_data = [str(x) + "\n" for x in data]
    file.writelines(write_data)
    file.flush()
    file.close()
    if debug:
        print("# write_lines_to_file: 文件名 %s,  行数 %d. 写入完成。" % (filename, len(write_data)))


def append_lines_to_file(filename, data, debug=True):
    """
    将行数据附加到文件后面
    """
    filename = get_abs_filename(filename)
    filepath = get_path_in_filename(filename)
    ensure_path(filepath)
    file = open(filename, 'a')
    write_data = [str(x) + "\n" for x in data]
    file.writelines(write_data)
    file.flush()
    file.close()
    if debug:
        print("# append_lines_to_file: 文件名 %s,  添加行数 %d. 写入完成。" % (filename, len(write_data)))


def write_csv_lines_to_file(filename, data, debug=True):
    """
    将数据列表写入文件
    """
    filename = get_abs_filename(filename)
    filepath = get_path_in_filename(filename)
    ensure_path(filepath)
    file = open(filename, 'w')
    write_data = [', '.join([str(t) for t in x]) + "\n" for x in data]
    file.writelines(write_data)
    file.flush()
    file.close()
    if debug:
        print("# write_csv_lines_to_file: 文件名 %s,  行数 %d. 写入完成。" % (filename, len(write_data)))


def append_a_csv_line_to_file(filename, data_list, debug=True):
    """
    将一个数据列表转为csv行添加到文件
    """
    str_list = [str(x) for x in data_list]
    str_line = ', '.join(str_list)
    append_lines_to_file(filename, [str_line], debug)




def get_path_in_filename(filename):
    """
    从filename中分离出路径部分
    """
    if filename.find('\\') > 0:
        path_split = filename.split('\\')
    else:
        path_split = filename.split('/')
    path_split.pop()
    return '/'.join(path_split)


def ensure_path(path):
    """
    确保一个路径存在
    """
    if not os.path.exists(path):
        print("# ensure_path: 自动创建路径 " + path)
        os.makedirs(path)


def check_sorted(input_list):
    """
    检查列表是否升序排序
    """
    last_elem = input_list[0]
    for elem in input_list:
        if elem < last_elem:
            return False
        last_elem = elem
    return True


def check_consistent(input_list1, input_list2):
    """
    检查两个列表是否一致
    """
    if len(input_list1) != len(input_list2):
        return False
    set1 = set(input_list1)
    set2 = set(input_list2)
    inter = set1.intersection(set2)
    if len(input_list1) + len(input_list2) > 0 and len(inter) == 0:
        return False
    dict1 = {keyx:0 for keyx in inter}
    dict2 = {keyx:0 for keyx in inter}
    for keyx in input_list1:
        dict1[keyx] += 1
    for keyx in input_list2:
        dict2[keyx] += 1
    for key in inter:
        if dict1[key] != dict2[key]:
            return False
    return True


def write_csv(filename, head, rows):
    """
    写入CSV文件
    """
    filename = get_abs_filename(filename)
    out = open(filename, 'w', newline='')
    writer = csv.writer(out, dialect='excel')
    writer.writerow(head)
    writer.writerows(rows)
    out.close()
    print("# write_csv: 已写入" + filename)


def read_csv(filename):
    """
    读取csv文件，返回head和rows
    """
    filename = get_abs_filename(filename)
    txt = open(filename, 'r')
    reader = csv.reader(txt, dialect='excel')
    head = next(reader)
    rows = [row for row in reader]
    txt.close()
    print("# write_csv: 已写入" + filename)
    return (head, rows)


def dict_to_rows(my_dict):
    """
    输入字典dict对象，返回列表对象
    """
    rows = [[key] + my_dict[key] for key in my_dict]
    return rows


def rows_to_dict(my_rows, data_type=str):
    """
    输入列表，返回字典对象
    """
    rows = {row[0]: [data_type(t) for t in row[1:]] for row in my_rows}
    return rows



def random_integers(low=1, high=10, count=100):
    """
    产生随机整数
    """
    # 产生随机数list
    result = list()
    for _ in range(0, count):
        result.append(random.randint(low, high))
    return result


def random_digitletter_charcodes(count=100, test_only=False):
    """
    产生随机的数字或者大小写字母的 ascii 码
    """
    # 26 + 26 + 10 = 62
    if test_only:
        # return random_integers(ord('a'), ord('a') + 25, count)
        return random_integers(ord('0'), ord('0') + 5, count)
    
    rand_ints = random_integers(1, 62, count)
    result = list()
    error_flag = False
    for rand_int in rand_ints:
        if rand_int <= 26:
            result.append(rand_int - 1 + ord('A'))
        elif rand_int <= 52:
            result.append(rand_int - 27 + ord('a'))
        elif rand_int <= 62:
            result.append(rand_int - 53 + ord('0'))
        else:
            error_flag = True
    if error_flag:
        print("# ERROR: random_digitletter_charcodes.")
    return result


def convert_ints_to_str(int_list):
    """
    将整数列表转字符串
    A=65 Z=90
    """
    result = ""
    for intx in int_list:
        result += "%c" % (intx)
    return result


def convert_str_to_ints(my_str):
    """
    将字符串转化为整形数组
    """
    result = [ord(x) for x in my_str]
    return result


def list_minus_base(data: list):
    """将一个列表都减去第一个元素"""
    base = data[0]
    return [x - base for x in data]
