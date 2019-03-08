# coding:utf-8

import requests

def getUrl(url):
    return requests.get(url)

def main():
    print "This is alice!"


if __name__ == '__main__':
    main()
