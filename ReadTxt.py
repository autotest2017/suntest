#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ReadAndWrite():
    @classmethod
    def read_file(self):
        hfile=open('data.txt','r')
        for i in hfile.readlines():
            print i.strip().decode('gbk')
        hfile.close()

if __name__=='__main__':
    ReadAndWrite.read_file()