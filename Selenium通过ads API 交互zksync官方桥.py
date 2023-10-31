import requests,time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import sys


ads_id = "j6xwg0d"
open_url = "http://local.adspower.net:50325/api/v1/browser/start?user_id=" + ads_id
close_url = "http://local.adspower.net:50325/api/v1/browser/stop?user_id=" + ads_id

resp = requests.get(open_url).json()

if resp["code"] != 0:
    print(resp["msg"])
    print("please check ads_id")
    sys.exit()

chrome_driver = resp["data"]["webdriver"]
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
print(driver.title)


# driver.get("https://bridge.zksync.io/")
#
#
# # 获取当前窗口句柄
# target_handle = driver.current_window_handle
#
# # 获取所有窗口句柄
# all_handles = driver.window_handles
#
# # 关闭其他标签页
# for handle in all_handles:
#     if handle != target_handle:
#         driver.switch_to.window(handle)
#         driver.close()
#
# # 切换回原来的标签页
# driver.switch_to.window(target_handle)
#
# # 打开新的标签，用于钱包popup页面
# EXTENSION_ID = 'hjlpapoplhliikalllichlbflmghmaob'
# driver.execute_script("window.open('');")
# driver.switch_to.window(driver.window_handles[1])
# driver.get('chrome-extension://{}/popup.html'.format(EXTENSION_ID))
#
# time.sleep(3)
#
# # 指定matamask的标签页
# metamask_handle = driver.current_window_handle
# print('指定matamask的标签页')
# print(metamask_handle)
#
# # 切换回协议的标签页
# driver.switch_to.window(target_handle)
# print('切换回协议的标签页')
# print(target_handle)
#
# # 点击“连接MetaMask”按钮
# download_button = driver.find_elements(By.XPATH, '//button[@class="login-btn"]')
# download_button[0].click()
# time.sleep(1)
# print('点击“连接MetaMask”按钮')
#
# # 切回matamask的标签页并刷新
# driver.switch_to.window(metamask_handle)
# driver.refresh()
# #如果不sleep，可能导致下一步选择器拿不到元素；
# time.sleep(2)
#
# # 点击“下一步”按钮
# next_button = driver.find_elements(By.XPATH, '//button[@class="button btn--rounded btn-primary"]')
# print('点击“下一步:',next_button)
# next_button[0].click()
# time.sleep(1)
#
# # 点击“连接”按钮
# link_button = driver.find_elements(By.XPATH, '//button[@class="button btn--rounded btn-primary page-container__footer-button"]')
# link_button[0].click()
# time.sleep(1)
#
#
# # 切换回协议的标签页
# driver.switch_to.window(target_handle)
# print('切换回协议的标签页')
# print(target_handle)
# time.sleep(8)
#
# # 在协议输入eth的金额
# input_amount = driver.find_elements(By.XPATH, '//input[@class="balance-input z-10"]')
# print('输入框:',input_amount)
# input_amount[0].send_keys("0.01")
# time.sleep(10)
# print('输入了eth金额')
#
# # 点击deposit
# deposit_button = driver.find_elements(By.XPATH, '//button[@class="button contained primary lg mt-10 w-full"]')
# deposit_button[0].click()
# time.sleep(1)
# print('点击deposit')
#
# # 切回matamask的标签页并刷新
# driver.switch_to.window(metamask_handle)
# #如果不sleep，refresh就无法取到小狐狸的process；
# time.sleep(5)
# driver.refresh()
# #如果不sleep，可能导致下一步选择器拿不到元素；
# time.sleep(3)
#
#
# # 点击确认按钮，find和click必须同一行，否则会刷新报错。
# driver.find_elements(By.XPATH, '//button[@class="button btn--rounded btn-primary page-container__footer-button"]')[0].click()
#
#
# # 切换回协议的标签页
# driver.switch_to.window(target_handle)
# print('切换回协议的标签页')
# print(target_handle)
# time.sleep(10)
#
# #driver.quit()
# #requests.get(close_url)