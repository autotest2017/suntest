#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
#按住ctrl，然后点击unittest就可以看到这个模块的定义


class ClassExample(unittest.TestCase):
    #按住ctrl，然后点击TestCase就可以看到这个类的定义
    # 定义了一个ClassExample类，继承unittest.TestCase这个类，这样在这个类里面就能使用unittest.TestCase里的方法了

    def test_add_sum1(self):
        #每一个测试用例都要用test_开头
        self.assertEqual(2,1+1)
        self.assertEqual(3,2+1)      #断言，如果这里失败了，这个用例就结束了，后面不用再执行
        self.assertTrue(True,'这里应该是True')
        print ('sum1')

    def test_add_sum(self):
        self.assertEqual(1,1)
        print ('sum')


class UTExample2(unittest.TestCase):
    def test_min(self):
        self.assertEqual(2-1,1)
        print('min')

if __name__ == "__main__":
    unittest.main()