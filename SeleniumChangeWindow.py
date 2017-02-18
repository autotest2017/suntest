from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys(u"samren博客园")
driver.find_element_by_id("su").click()
driver.find_element_by_partial_link_text(u"GitHub命令精简教程").click()
print(driver.window_handles)

#[u'{131ae35e-0fd5-4e7a-9bdd-c62255657bf7}', u'{3af733e1-5c76-45f4-afc2-378d62425b6a}']
print(driver.current_window_handle)


driver.find_element_by_partial_link_text(u"GitHub命令精简教程").click()
print(driver.window_handles)
print(driver.current_window_handle)


driver.switch_to.window(driver.window_handles[1])

print(driver.current_window_handle)


driver.find_element_by_link_text(u"管理").click()