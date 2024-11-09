import os
import time as t
from colorama import Fore,Back,Style,init
init(autoreset=True)
class Debug():
    def __init__(self,print = True,date = True,time_stamp = False,write = True,fname = "main.log",server = False) -> None:
        self.print = print
        self.date = date
        self.time_stamp = time_stamp
        self.write = write
        self.fname = fname
        self.server = server
    def debug(self,txt,ip = "") -> None:
        txt = str(txt)
        if self.server:
            if self.date:
                if self.time_stamp:
                    time = round(t.time())
                else:
                    time = t.strftime('%Y-%m-%d %H:%M:%S', t.localtime())
                ptxt = "[" + Fore.RED + str(time) + Style.RESET_ALL + "] [" + Fore.BLUE + "DEBUG" + Style.RESET_ALL + "][" + Fore.BLUE + ip + Style.RESET_ALL +  "] " + txt
                ftxt = "[" + str(time) + "] [" + "DEBUG" + "][" + ip + "] " + txt + "\n"
            else:
                ptxt = "[" + Fore.BLUE + "DEBUG" + Style.RESET_ALL + "][" + Fore.BLUE + ip + Style.RESET_ALL +  "] " + txt
                ftxt = "[" + "DEBUG" + "][" + ip + "] " + txt + "\n"
            if self.print:
                print(ptxt)
            if self.write:
                if os.path.exists(self.fname):
                    with open(self.fname, 'r') as f:
                        ftxt = f.read() + ftxt
                with open(self.fname, 'w') as f:
                    f.write(ftxt)
                    f.close()
        else:
            if self.date:
                if self.time_stamp:
                    time = round(t.time())
                else:
                    time = t.strftime('%Y-%m-%d %H:%M:%S', t.localtime())
                ptxt = "[" + Fore.RED + str(time) + Style.RESET_ALL + "] [" + Fore.BLUE + "DEBUG" + Style.RESET_ALL + "] " + txt
                ftxt = "[" + str(time) + "] [" + "DEBUG" + "] " + txt + "\n"
            else:
                ptxt = "[" + Fore.BLUE + "DEBUG" + Style.RESET_ALL + "] " + txt
                ftxt = "[" + "DEBUG" + "] " + txt + "\n"
            if self.print:
                print(ptxt)
            if self.write:
                if os.path.exists(self.fname):
                    with open(self.fname, 'r') as f:
                        ftxt = f.read() + ftxt
                with open(self.fname, 'w') as f:
                    f.write(ftxt)
                    f.close()
    def info(self,txt,ip = "") -> None:
        txt = str(txt)
        if self.server:
            if self.date:
                if self.time_stamp:
                    time = round(t.time())
                else:
                    time = t.strftime('%Y-%m-%d %H:%M:%S', t.localtime())
                ptxt = "[" + Fore.RED + str(time) + Style.RESET_ALL + "] [" + Fore.GREEN + "INFO" + Style.RESET_ALL + "] [" + Fore.BLUE + ip + Style.RESET_ALL +  "] " + txt
                ftxt = "[" + str(time) + "] [" + "INFO" + "] [" + ip + "] " + txt + "\n"
            else:
                ptxt = "[" + Fore.GREEN + "INFO" + Style.RESET_ALL + "] [" + Fore.BLUE + ip + Style.RESET_ALL +  "] " + txt
                ftxt = "[" + "INFO" + "] [" + ip + "] " + txt + "\n"
            if self.print:
                print(ptxt)
            if self.write:
                if os.path.exists(self.fname):
                    with open(self.fname, 'r') as f:
                        ftxt = f.read() + ftxt
                with open(self.fname, 'w') as f:
                    f.write(ftxt)
                    f.close()
        else:
            if self.date:
                if self.time_stamp:
                    time = round(t.time())
                else:
                    time = t.strftime('%Y-%m-%d %H:%M:%S', t.localtime())
                ptxt = "[" + Fore.RED + str(time) + Style.RESET_ALL + "] [" + Fore.GREEN + "INFO" + Style.RESET_ALL + "] " + txt
                ftxt = "[" + str(time) + "] [" + "INFO" + "] " + txt + "\n"
            else:
                ptxt = "[" + Fore.GREEN + "INFO" + Style.RESET_ALL + "]  " + txt
                ftxt = "[" + "INFO" + "]  " + txt + "\n"
            if self.print:
                print(ptxt)
            if self.write:
                if os.path.exists(self.fname):
                    with open(self.fname, 'r') as f:
                        ftxt = f.read() + ftxt
                with open(self.fname, 'w') as f:
                    f.write(ftxt)
                    f.close()
    def warn(self,txt,ip = "") -> None:
        txt = str(txt)
        if self.server:
            if self.date:
                if self.time_stamp:
                    time = round(t.time())
                else:
                    time = t.strftime('%Y-%m-%d %H:%M:%S', t.localtime())
                ptxt = "[" + Fore.RED + str(time) + Style.RESET_ALL + "] [" + Fore.YELLOW + "WARN" + Style.RESET_ALL + "] [" + Fore.BLUE + ip + Style.RESET_ALL +  "] " + txt
                ftxt = "[" + str(time) + "] [" + "WARN" + "] [" + ip + "] " + txt + "\n"
            else:
                ptxt = "[" + Fore.YELLOW + "WARN" + Style.RESET_ALL + "] [" + Fore.BLUE + ip + Style.RESET_ALL +  "] " + txt
                ftxt = "[" + "WARN" + "] [" + ip + "] " + txt + "\n"
            if self.print:
                print(ptxt)
            if self.write:
                if os.path.exists(self.fname):
                    with open(self.fname, 'r') as f:
                        ftxt = f.read() + ftxt
                with open(self.fname, 'w') as f:
                    f.write(ftxt)
                    f.close()
        else:
            if self.date:
                if self.time_stamp:
                    time = round(t.time())
                else:
                    time = t.strftime('%Y-%m-%d %H:%M:%S', t.localtime())
                ptxt = "[" + Fore.RED + str(time) + Style.RESET_ALL + "] [" + Fore.YELLOW + "WARN" + Style.RESET_ALL + "] " + txt
                ftxt = "[" + str(time) + "] [" + "WARN" + "] " + txt + "\n"
            else:
                ptxt = "[" + Fore.YELLOW + "WARN" + Style.RESET_ALL + "]  " + txt
                ftxt = "[" + "WARN" + "]  " + txt + "\n"
            if self.print:
                print(ptxt)
            if self.write:
                if os.path.exists(self.fname):
                    with open(self.fname, 'r') as f:
                        ftxt = f.read() + ftxt
                with open(self.fname, 'w') as f:
                    f.write(ftxt)
                    f.close()
    def error(self,txt,ip = "") -> None:
        txt = str(txt)
        if self.server:
            if self.date:
                if self.time_stamp:
                    time = round(t.time())
                else:
                    time = t.strftime('%Y-%m-%d %H:%M:%S', t.localtime())
                ptxt = "[" + Fore.RED + str(time) + Style.RESET_ALL + "] [" + Fore.RED + "ERROR" + Style.RESET_ALL + "][" + Fore.BLUE + ip + Style.RESET_ALL +  "] " + txt
                ftxt = "[" + str(time) + "] [" + "ERROR" + "][" + ip + "] " + txt + "\n"
            else:
                ptxt = "[" + Fore.RED + "ERROR" + Style.RESET_ALL + "][" + Fore.BLUE + ip + Style.RESET_ALL +  "] " + txt
                ftxt = "[" + "ERROR" + "][" + ip + "] " + txt + "\n"
            if self.print:
                print(ptxt)
            if self.write:
                if os.path.exists(self.fname):
                    with open(self.fname, 'r') as f:
                        ftxt = f.read() + ftxt
                with open(self.fname, 'w') as f:
                    f.write(ftxt)
                    f.close()
        else:
            if self.date:
                if self.time_stamp:
                    time = round(t.time())
                else:
                    time = t.strftime('%Y-%m-%d %H:%M:%S', t.localtime())
                ptxt = "[" + Fore.RED + str(time) + Style.RESET_ALL + "] [" + Fore.RED + "ERROR" + Style.RESET_ALL + "] " + txt
                ftxt = "[" + str(time) + "] [" + "ERROR" + "] " + txt + "\n"
            else:
                ptxt = "[" + Fore.RED + "ERROR" + Style.RESET_ALL + "] " + txt
                ftxt = "[" + "ERROR" + "] " + txt + "\n"
            if self.print:
                print(ptxt)
            if self.write:
                if os.path.exists(self.fname):
                    with open(self.fname, 'r') as f:
                        ftxt = f.read() + ftxt
                with open(self.fname, 'w') as f:
                    f.write(ftxt)
                    f.close()
