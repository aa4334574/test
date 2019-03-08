# import os
# import os.path
# rootdir = "D:/"                                   # 指明被遍历的文件夹
#
# for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
#     for dirname in  dirnames:                       #输出文件夹信息
#         print ("parent is:" + parent)
#         print  ("dirname is" + dirname)
#
#     for filename in filenames:                        #输出文件信息
#         print ("parent is:" + parent)
#         print ("filename is:" + filename)
#         print ("the full name of the file is:" + os.path.join(parent,filename)) #输出文件路径信息




# import os
# path = u'D:\可知新资源'
# for dirpath,dirname,filenames in os.walk(path):
#     print (dirname)
#     for filename in filenames:
#         # print (filename)
#         print (os.path.join(dirpath,filenames))
#     # print(filenames)

# -*- conding :utf-8 -*-
import pymssql as py
# server = '124.193.177.45,50680'
# user = 'develop'
# password = 'db(*)2016'
#
# help(py)
# conn = py.connect(host = server,database = 'red_solution',user = user,password = password)
# print (conn)
# cur = conn.coursor()

# import os
'''
记录i/o写入
'''
# path = 'D:\\'
# a = []
# for d in  os.walk(path):
#     for i in d:
#         with open('D:\\text.txt','a') as f:
#     # print(f.read())
#     # print(type(f.read()))
#     # for readline in f.readlines():
#     #     print (readline)
#     # print(f.readlines())
#     # print(type(f.readline()))
#             print(''.join(tuple(i)))
#             f.write(''.join(tuple(i))+'/n')
#             if not f:
#                 print('写入完成')
import pytest
import pytest_html
class Test_class:
    def setup_model(self):
        print('1')
    def turndown_model(self):
        print('2')
    def test_one(self):
        x = 'this'
        assert 'h'in x
    def test_two(self):
        x = 'that'
        assert  'a' in x
    def test_three(self):
        x = 'that'
        assert  'th' in x