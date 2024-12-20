import json
import sys
import time
import Debug
debug = Debug.Debug("main.log")
print(
"""
 /$$$$$$$$                       /$$            /$$$$$$  /$$$$$$       /$$$$$$$                      /$$                    
| $$_____/                      | $$           /$$__  $$|_  $$_/      | $$__  $$                    | $$                    
| $$        /$$$$$$   /$$$$$$$ /$$$$$$        | $$  \ $$  | $$        | $$  \ $$  /$$$$$$   /$$$$$$ | $$  /$$$$$$  /$$   /$$
| $$$$$    |____  $$ /$$_____/|_  $$_/        | $$$$$$$$  | $$        | $$  | $$ /$$__  $$ /$$__  $$| $$ /$$__  $$| $$  | $$
| $$__/     /$$$$$$$|  $$$$$$   | $$          | $$__  $$  | $$        | $$  | $$| $$$$$$$$| $$  \ $$| $$| $$  \ $$| $$  | $$
| $$       /$$__  $$ \____  $$  | $$ /$$      | $$  | $$  | $$        | $$  | $$| $$_____/| $$  | $$| $$| $$  | $$| $$  | $$
| $$      |  $$$$$$$ /$$$$$$$/  |  $$$$/      | $$  | $$ /$$$$$$      | $$$$$$$/|  $$$$$$$| $$$$$$$/| $$|  $$$$$$/|  $$$$$$$
|__/       \_______/|_______/    \___/        |__/  |__/|______/      |_______/  \_______/| $$____/ |__/ \______/  \____  $$
                                                                                          | $$                     /$$  | $$
                                                                                          | $$                    |  $$$$$$/
                                                                                          |__/                     \______/ 

FAID v1.0 快速部署AI""")
debug.info("正在加载gradio...")
import gradio as gr
import ollama
import os
debug.info("程序启动")
model = None
try:
    with open("config.json", "r", encoding='utf-8') as file:
        config = json.load(file.read())
except:
    with open("config.json", "w", encoding='utf-8') as file:
        config = {"theme":"Base","ip":"127.0.0.1", "port":"11434"}
        file.write(str(config))
chat = ollama.ollama(ip=config["ip"],port=config["port"])
debug.info(f"加载配置文件{config}")
debug.info("检查环境...")
if not chat.have_ollama():
    debug.error("我们未检测到ollama服务，请检查是否正常启动或安装")
    debug.info("准备尝试启动哦ollama")
    if os.system("ollama"):
            print("请在打开的网站手动下载\n如果下载速度过慢请安装steam++，开启github网络加速后在https://github.com/ollama/ollama/releases 下载Latest版本")
            os.system("start https://ollama.com/download")
            print("程序正在等待ollama启动，如果正常启动将会自动进行下一步")
            while True:
                if chat.have_ollama():
                    break
                time.sleep(1)
    else:
        print("正常启动将会自动进行下一步")
        while True:
            if chat.have_ollama():
                break
debug.info("环境检查完毕")
THEMES = ["Base", "Default", "Origin", "Citrus", "Monochrome", "Soft", "Glass", "Ocean"]
debug.info("正在加载主题...")
def theme():
    global config
    if config["theme"] == "Base":
        return gr.themes.Base()
    elif config["theme"] == "Default":
        return gr.themes.Default()
    elif config["theme"] == "Origin":
        return gr.themes.Origin()
    elif config["theme"] == "Citrus":
        return gr.themes.Citrus()
    elif config["theme"] == "Monochrome":
        return gr.themes.Monochrome()
    elif config["theme"] == "Soft":
        return gr.themes.Soft()
    elif config["theme"] == "Glass":
        return gr.themes.Glass()
    elif config["theme"] == "Ocean":
        return gr.themes.Ocean()
    else:
        t = gr.Theme.from_hub(config["theme"])
        return t
def apply_theme(theme):
    global config
    with open("config.json", "w", encoding='utf-8') as file:
        config["theme"] = theme
        file.write(str(config))
def set_model_func(set_model_dropdown):
    global model
    model = set_model_dropdown
    gr.Info(f"已切换为{model}")
    return None
def install_model_func(install_model_dropdown):
    if chat.have_model(install_model_dropdown): 
        gr.Warning("没有此模型")
    else:
        if chat.have_model(install_model_dropdown): 
            gr.Warning("已有此模型")
        else:
            gr.Info(f"开始安装{install_model_dropdown},请耐心等待...")
            if chat.install_model(install_model_dropdown):
                gr.Info(f"安装成功")
            else: 
                gr.Error("安装失败")
def uninstall_model_func(install_model_dropdown):
    if chat.ollama_have_model(install_model_dropdown): 
        gr.Warning("没有此模型")
    else:
        gr.Info(f"开始卸载{install_model_dropdown},请耐心等待...")
        if chat.uninstall_model(install_model_dropdown):
            gr.Info(f"卸载成功")
        else: 
            gr.Error("卸载失败")
def respond(message, chat_history):
    global model
    if model == None: 
        gr.Warning("请先选择模型")
    else:
        data = chat.chat(model_name=model, message=message, historical_dialogs=chat_history)
        temp = ""
        for i in data:
            temp += i
            yield temp
def respond_img(message, chat_history,img):
    print(111)
    global model
    if model == None: 
        gr.Warning("请先选择模型")
    else:
        data = chat.chat_img(model_name=model, message=message, historical_dialogs=chat_history,imgpath=[img])
        temp = ""
        for i in data:
            temp += i
            yield temp
def make_text_func(prompt):
    global model
    if model == None: 
        gr.Warning("请先选择模型")
        yield "未选择模型"
    else:
        data = chat.generate(model_name=model,prompt=prompt)
        for i in data: 
            yield i
def set_ip_port_func(ip,port):
    global config
    config["ip"] = ip
    config["port"] = port
    with open("config.json", "w", encoding='utf-8') as file:
        file.write(str(config))
def Restart_func():
    os.execl(sys.executable,sys.executable,*sys.argv)
with gr.Blocks(theme = theme()) as Main_tab:
    gr.HTML(
    """
    <p>安装或选择一个模型，开始吧！</p>
    """)
with gr.Blocks() as Chat_tab:
    Chat_interface = gr.ChatInterface(respond,fill_height = True)
with gr.Blocks() as Chat_img_tab:
    Chat_interface = gr.ChatInterface(respond_img,fill_height = True,additional_inputs=[gr.Image(type="filepath",label="图片")])
with gr.Blocks() as Make_text_tab:
    gr.Markdown("# 文本生成")
    prompt = gr.Textbox(label="输入文本")
    generate_button = gr.Button("生成")
    make_text = gr.Markdown("")
    generate_button.click(make_text_func, inputs=[prompt], outputs=[make_text])
with gr.Blocks() as Tools_tab:
    gr.Markdown("# 工具箱")
    gr.Markdown("## 安装")
    install_model_name = gr.Textbox(label="模型名")
    install_model_button = gr.Button("安装模型")
    install_model_button.click(install_model_func, inputs=[install_model_name])
    gr.Markdown("## 卸载")
    uninstall_model_name = gr.Textbox(label="模型名")
    uninstall_model_button = gr.Button("卸载模型")
    uninstall_model_button.click(uninstall_model_func, inputs=[uninstall_model_name])
with gr.Blocks() as Set_tab:
    with gr.Tab("模型"):
        set_model_dropdown = gr.Dropdown(chat.get_model_list(), value=chat.get_model_list()[0], label="模型选择")
        set_model_button = gr.Button("设置模型")
        set_model_button.click(set_model_func, inputs=[set_model_dropdown])
        refresh_model_button = gr.Button("刷新模型")
        refresh_model_button.click(chat.get_model_list, outputs=[set_model_dropdown])
    with gr.Tab("主题"):
        theme_dropdown = gr.Dropdown(THEMES, label="选择主题")
        apply_theme_button = gr.Button("应用主题(重启生效)")
        apply_theme_button.click(apply_theme, inputs=[theme_dropdown])
        Restart = gr.Button("重启")
        Restart.click(Restart_func)
    with gr.Tab("本程序"):
        set_ip = gr.Textbox(label="IP地址")
        set_port = gr.Textbox(label="端口")
        set_ip_port_button = gr.Button("设置(应用于本程序，重启生效)")
        set_ip_port_button.click(chat.get_model_list,inputs=[set_ip,set_port])
    gr.Markdown(
"""
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
[彩蛋](https://sr.mihoyo.com/)""")
app = gr.TabbedInterface([Main_tab, Chat_tab, Chat_img_tab, Make_text_tab, Tools_tab, Set_tab], 
                         ["主页", "对话", "带图片对话", "文本生成", "工具箱", "设置"], title="AI",theme = theme())
debug.info("启动成功 请访问http://127.0.0.1:7860/")
app.launch(debug=True)
