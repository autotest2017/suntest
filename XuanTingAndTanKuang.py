#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


wd = webdriver.Firefox()
wd.get("http://www.baidu.com")
link = wd.find_element_by_link_text(u"设置")
tmp = ActionChains(wd).move_to_element(link)
tmp.perform()

ActionChains(wd).double_click(link).perform()
ActionChains(wd).click(link).perform()
wd.find_element_by_link_text(u"搜索设置").click()
wd.find_element_by_class_name("prefpanelgo").click()

#wd.switch_to_alert().accept()
wd.switch_to.alert.accept()