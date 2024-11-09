import json
import requests
import Debug
class ollama():
    def __init__(self,ip:str = "localhost",port:str = "11434"):
        self.debug = Debug.Debug(fname="api.log")
        self.ip = ip
        self.port = port
        self.url = f"http://{self.ip}:{self.port}"
    def have_ollama(self):
        url = f"{self.url}"
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    def get_model_list(self) -> list:
        url = f"{self.url}/api/tags"
        response = requests.get(url)
        data = json.loads(response.text)
        return_data = []
        for i in data["models"]:
            return_data.append(i["name"])
        return return_data
    def install_model(self,model_name:str) -> bool:
        url = f"{self.url}/api/pull"
        post = {"model":model_name,"stream":True}
        data = requests.post(url=url,json=post,stream=True)
        for i in data.iter_lines():
            j = json.loads(i)
            self.debug.info(j)
            if j["status"] == "success":
                return True
        return False
    def have_model(self,model_name:str) -> bool:
        url = f"https://ollama.com/library/{model_name}"
        response = requests.get(url)
        if '<main class="mx-auto flex max-w-4xl flex-1 flex-col-reverse items-center justify-center p-32 md:flex-row md:items-start md:justify-between">' in response.text:
            return True
        else:
            return False
    def ollama_have_model(self,model_name:str) -> bool:
        url = f"{self.url}/api/tags"
        response = requests.get(url)
        data = json.loads(response.text)
        return_data = []
        for i in data["models"]:
            if i["name"] == model_name:
                return False
        return True
    def uninstall_model(self,model_name:str) -> bool:
        url = f"{self.url}/api/delete"
        post = {"model":model_name,"stream":True}
        data = requests.delete(url=url,json=post,stream=True)
        if data.status_code == 200:
            return True
        else:
            return False
    def chat(self,model_name:str,message:str,historical_dialogs):
        messages = []
        for i in historical_dialogs:
            temp = {"role": "user","content": i[0]}
            messages.append(temp)
            temp = {"role": "assistant","content": i[1]}
            messages.append(temp)
        temp = {"role": "user","content": message}
        messages.append(temp)
        url = f"{self.url}/api/chat"
        post = {"model":model_name,"messages":messages,"stream":True}
        self.debug.info(post)
        data = requests.post(url=url,json=post,stream=True)
        for i in data.iter_lines():
            j = json.loads(i)
            self.debug.info(i)
            if "error" in j:
                yield j["error"]
                break
            if not(j["done"]):
                yield j["message"]["content"]
    def generate(self,model_name:str,prompt:str):
        url = f"{self.url}/api/generate"
        post = {"model":model_name,"prompt":prompt,"stream":True}
        data = requests.post(url=url,json=post,stream=True)
        temp = ""
        for i in data.iter_lines():
            j = json.loads(i)
            if "error" in j:
                yield j["error"]
                break
            self.debug.info(j)
            temp += j["response"]
            yield temp
