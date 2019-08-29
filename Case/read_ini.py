# coding = utf-8
import configparser

class ReadIni(object):
    def __init__(self, file_name=None, node=None):
        if file_name == None:
            self.file_name = "/Users/joseph/PycharmProjects/project/config/local_element.ini"
        if node == None:
            self.node = "RegisterElement"
        else:
            self.node = node
        self.cf = self.load_ini(self.file_name)

# 加载文件
    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

# 获取value值
    def get_value(self,key):
        date = self.cf.get(self.node, key)
        return date

if __name__ == '__main__':
    red_init = ReadIni()
    print(red_init.get_value("user_name"))


