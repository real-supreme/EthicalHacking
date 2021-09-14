import socket
from IPy import IP


class portscanner:
    def __init__(self, ports: tuple):
        self.port1, self.port2 = ports
        self.banner = []
        self.opens = []

    def scan(self, target):
        converted_ip = self.convert_to_ipv4(target)
        if converted_ip == None:
            print("Something wrong")
        print("\n" + "[- 0 Scanning Target]" + str(target))
        print(str(converted_ip))
        for port in range(int(self.port1), int(self.port2)):
            self.scan_port(converted_ip, port)
        return [self.banner, self.opens, target]

    @staticmethod
    def convert_to_ipv4(ip):
        try:
            IP(ip)
            return ip
        except:
            return socket.gethostbyname(ip)

    @staticmethod
    def get_banner(s):
        return s.recv(1024)

    def scan_port(self, ipaddress, port, time=2.0):
        try:
            sock = socket.socket()
            sock.settimeout(time)
            sock.connect((ipaddress, port))

            try:
                banner = self.get_banner(sock)
                print(
                    "[+] Open Port"
                    + str(port)
                    + " : "
                    + str(banner.decode().strip("\n"))
                )
                print("[+] Open Port" + str(port) + " : " + str(banner))
                self.banner.append(str(banner))
            except:
                print("[+] Open Port" + str(port))
        except:
            print("[-] Port" + str(port) + "Is Closed")


# my_list = ["value1", "value2", "value3"]

# for mine in my_list:
#     print(mine)

if __name__ == "__main__":
    targets = input("[+] Enter Target/s to get Scan: (split multiple target with ,)")
    if "," in targets:
        for ip_add in targets.split(","):
            portscanner().scan(ip_add.strip())
    else:
        portscanner().scan(targets)
