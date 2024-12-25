# 导入必要的库
from selenium import webdriver  # 控制浏览器行为
from selenium.webdriver.common.by import By  # 用于定位页面元素
import time  # 控制等待时间
import pyautogui  # 模拟键盘操作
import traceback  # 捕获和显示错误

# 初始化 Chrome 浏览器驱动
driver = webdriver.Chrome()

# 定义滚动和保存的等待时间
scroll_wait_time = 4  # 每次滚动后等待6秒
save_wait_time = 1    # 保存 PDF 文件后等待3秒

# 记录加载失败的页面号，便于后续手动处理
failed_pages = []

# 设置第一页与后续页面的 URL 格式
first_page_url = "https://www.177pica.com/html/2013/11/11163.html"  # 第一个页面的特殊 URL
page_url_template = "https://www.177pica.com/html/2013/11/11163.html/{}/"  # 后续页面 URL 的模板，{} 会被替换为页码

# 遍历每一页进行下载
for page_num in range(1, 26):  # 假设需要下载1到21页
    try:
        # 根据页面号选择合适的 URL
        if page_num == 1:
            url = first_page_url  # 第一个页面使用特殊的 URL
        else:
            url = page_url_template.format(page_num)  # 其他页面使用通用模板

        # 访问页面
        driver.get(url)

        # 滚动到页面底部以加载所有内容
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_wait_time)  # 等待加载内容

        # 滚动到页面中部以确保所有图片加载
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
        time.sleep(3)  # 等待中部内容加载

        # 打开打印窗口
        pyautogui.hotkey("command", "p")  # Mac 上打开打印窗口
        time.sleep(2)  # 等待打印窗口打开

        # 按下回车进入文件名和保存路径设置界面
        pyautogui.press("enter")
        time.sleep(1.5)  # 等待文件名输入框加载

        # 输入文件名（不带路径）
        filename = f"page_{page_num}"  # 仅文件名
        pyautogui.write(filename)
        
        # 按下回车确认保存
        pyautogui.press("enter")
        time.sleep(1.5)        
        print(f"第 {page_num} 页已成功保存为 PDF 文件。")

    except Exception as e:
        # 捕获异常并记录错误信息
        print(f"第 {page_num} 页保存失败。错误信息：{str(e)}")
        failed_pages.append(page_num)
        traceback.print_exc()

# 关闭浏览器
driver.quit()

# 输出保存失败的页面号
if failed_pages:
    print("以下页面保存失败，请稍后手动处理：", failed_pages)
else:
    print("所有页面均已成功保存。")
