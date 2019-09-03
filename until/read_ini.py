# coding = utf-8
import configparser


class ReadIni(object):
    # 创建一个函数，用来获取local_element配置文件中的配置信息，判断文件是否存在，节点是否有
    def __init__(self, file_name=None, node=None):
        # 如果这个路径为空选择此路径的配置文件
        if file_name is None:
            file_name = "/Users/joseph/PycharmProjects/project/config/local_element.ini"
        # 如果没有选择配置文件内的节点，选择此节点
        if node is None:
            self.node = "RegisterElement"
        else:
            self.node = node
        self.cf = self.load_ini(file_name)

    # 加载文件 - 引入实例化的配置文件，读取文件信息
    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    # 获取value值
    def get_value(self, key):
        data = self.cf.get(self.node, key)
        return data


if __name__ == '__main__':
    red_init = ReadIni()
    print(red_init.get_value("user_name"))
