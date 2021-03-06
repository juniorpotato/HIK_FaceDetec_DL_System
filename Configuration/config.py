# coding=utf-8
import configparser
import os

# rootdir = os.getcwd()  # 获取配置文件的绝对路径
# rootconf = os.path.join(rootdir, 'config.ini')  # 连接路径和相应文件
# print(rootconf)
# 自己在这里犯了一个错误，config.ini应该放在总工程目录下

config = configparser.ConfigParser()
config.read('/home/douxiao/Desktop/HIK_FaceDetec_DL_System/config.ini')  # 读取配置文件中的配置信息

user = config.get("accountConf", "user")
password = config.get("accountConf", "password")
host = config.get("ipConf", "host")
port = config.get("ipConf", "port")


def get_rtsp():
    # 海康威视摄像头的RSTP地址
    # 海康威视摄像头采用的是RTSP协议 RTSP 实时串流协议(Real time stream protocol,RTSP)
    # 是一种网络应用协议，专为娱乐和通信系统使用，以控制流媒体服务器。
    rtsp = "rtsp://%s:%s@%s/Streaming/Channels/1" % (user, password, host)
    print(rtsp)
    return rtsp


def get_ip():
    return host

def get_port():
    return port


if __name__ == "__main__":
    get_rtsp()
    get_ip()
    get_port()