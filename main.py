# coding:utf-8

import requests

def getUrl(url):
    return requests.get(url)

def getObject():
    return getUrl("http://www.baidu.com")

def main():
    print "This is alice!"


if __name__ == '__main__':
    main()
