import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
import requests

class GrokApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.conversation_history = []  # 保存对话历史

    def initUI(self):
        # 创建输入框，用户在这里输入查询
        self.text_input = QLineEdit(self)
        # 创建输出文本框，用于显示Grok的响应
        self.text_output = QTextEdit(self)
        # 创建发送按钮
        self.send_button = QPushButton('发送给Grok', self)

        # 创建布局并添加控件
        layout = QVBoxLayout()
        layout.addWidget(self.text_input)
        layout.addWidget(self.send_button)
        layout.addWidget(self.text_output)
        self.setLayout(layout)

        # 连接按钮的点击事件和回车事件到发送方法
        self.send_button.clicked.connect(self.send_to_grok)
        self.text_input.returnPressed.connect(self.send_to_grok)

        # 设置窗口的几何形状和标题
        self.setGeometry(600, 600, 700, 500)
        self.setWindowTitle('Grok')
        self.show()

    def send_to_grok(self):
        # 从输入框中获取用户的查询
        query = self.text_input.text()
        
        # 添加新用户消息到对话历史
        self.conversation_history.append({"role": "user", "content": query})
        
        # 假设的Grok API端点
        api_url = "https://api.x.ai/v1/chat/completions"
        headers = {
            "Authorization": "Bearer xai-PW1vMWbTCgj4OKVmVduBFwTB3dbLWfT6GzQQ9lsHbTEsFstCiJomRN1Vl2kIXHWgEcgrZQy2fTebZ1Nx",  # 请替换为你的实际API密钥
            "Content-Type": "application/json"
        }
        data = {
            "model": "grok-2-1212",  # 使用当前可用的模型名称
            "messages": self.conversation_history
        }
        
        try:
            # 发送POST请求到Grok API
            response = requests.post(api_url, headers=headers, json=data)
            response.raise_for_status()
            # 解析JSON响应
            result = response.json()
            # 从响应中提取内容
            ai_response = result.get('choices', [{}])[0].get('message', {})
            # 添加AI的响应到对话历史
            self.conversation_history.append(ai_response)
            # 在输出框中显示对话
            self.text_output.append(f"User: {query}\nAI: {ai_response.get('content', '')}\n")
        except requests.RequestException as e:
            # 如果请求失败，显示错误信息
            self.text_output.append(f"错误: {e}")

        # 清空输入框以便下一次输入
        self.text_input.clear()

if __name__ == '__main__':
    # 创建应用实例
    app = QApplication(sys.argv)
    # 创建和显示窗口
    ex = GrokApp() # 运行应用主循环
    sys.exit(app.exec_())
