# mangle table use to mask
import subprocess

IPTABLES_MARK_H= "iptables -t mangle -A PREROUTING -p tcp -m multiport -d xxx --dport xxx -j MARK --set-mark 0x65536"

#  redirect to point port
IPTABLES_FORWARD_H="iptables -t nat -A PREROUTING -p tcp -m mark --mark 0x65536 -j REDIRECT --to-ports xxxxx"


def parse_port():
    return '10000:20000'


def mark_port():
    ports=parse_port()
    cmd=["iptables","-t","mangle","-A","PREROUTING","-p","tcp","-m","multiport","-d","192.168.52.129",'--dport',f"{ports}","-j","MARK","--set-mark","0x65536"]
    subprocess.run(cmd,check=True)


def delete_mark_port():
    ports=parse_port()
    delete_mark_cmd=["iptables","-t","mangle","-D","PREROUTING","-p","tcp","-m","multiport","-d","192.168.52.129",'--dport',f"{ports}","-j","MARK","--set-mark","0x65536"]
    subprocess.run(delete_mark_cmd,check=True)

def redirect_port():
    port = 10001
    redirect_cmd=["iptables", "-t", "nat", "-A","PREROUTING", "-p","tcp", "-m","mark", "--mark","0x65536", "-j","REDIRECT","--to-ports",f"{port}"]
    subprocess.run(redirect_cmd,check=True)

def delete_redirect_port():
    port=10001
    delete_redirect_cmd = ["iptables", "-t", "nat", "-D", "PREROUTING", "-p", "tcp", "-m", "mark", "--mark", "0x65536", "-j",
                    "REDIRECT", "--to-ports", f"{port}"]
    subprocess.run(delete_redirect_cmd,check=True)


import json
import socket

def start_syslog_server(host='0.0.0.0', port=514):
    # 创建 TCP 套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)  # 监听队列大小为 5

    print(f"Syslog server started on {host}:{port}")

    try:
        while True:
            conn, addr = sock.accept()
            print(f"Connection established from {addr}")
            with conn:
                while True:
                    data = conn.recv(4096)
                    if not data:
                        break
                    log_message = data.decode('utf-8')
                    # 提取 JSON 数据部分
                    print(log_message)

    except KeyboardInterrupt:
        print("Syslog server shutting down.")
    finally:
        sock.close()

if __name__ == "__main__":
    # start_syslog_server(port=1001)
    start_syslog_server(port=10001)
    # delete_redirect_port()
    # delete_mark_port()
    # mark_port()
    # redirect_port()


# iptables -t nat -L -v -n
# iptables -t mangle -L -v -n
# mangle table use to mask
import subprocess

IPTABLES_MARK_H= "iptables -t mangle -A PREROUTING -p tcp -m multiport -d xxx --dport xxx -j MARK --set-mark 0x65536"

#  redirect to point port
IPTABLES_FORWARD_H="iptables -t nat -A PREROUTING -p tcp -m mark --mark 0x65536 -j REDIRECT --to-ports xxxxx"


def parse_port():
    return '10000:20000'


def mark_port():
    ports=parse_port()
    cmd=["iptables","-t","mangle","-A","PREROUTING","-p","tcp","-m","multiport","-d","192.168.52.129",'--dport',f"{ports}","-j","MARK","--set-mark","0x65536"]
    subprocess.run(cmd,check=True)


def delete_mark_port():
    ports=parse_port()
    delete_mark_cmd=["iptables","-t","mangle","-D","PREROUTING","-p","tcp","-m","multiport","-d","192.168.52.129",'--dport',f"{ports}","-j","MARK","--set-mark","0x65536"]
    subprocess.run(delete_mark_cmd,check=True)

def redirect_port():
    port = 10001
    redirect_cmd=["iptables", "-t", "nat", "-A","PREROUTING", "-p","tcp", "-m","mark", "--mark","0x65536", "-j","REDIRECT","--to-ports",f"{port}"]
    subprocess.run(redirect_cmd,check=True)

def delete_redirect_port():
    port=10001
    delete_redirect_cmd = ["iptables", "-t", "nat", "-D", "PREROUTING", "-p", "tcp", "-m", "mark", "--mark", "0x65536", "-j",
                    "REDIRECT", "--to-ports", f"{port}"]
    subprocess.run(delete_redirect_cmd,check=True)


import json
import socket

def start_syslog_server(host='0.0.0.0', port=514):
    # 创建 TCP 套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)  # 监听队列大小为 5

    print(f"Syslog server started on {host}:{port}")

    try:
        while True:
            conn, addr = sock.accept()
            print(f"Connection established from {addr}")
            with conn:
                while True:
                    data = conn.recv(4096)
                    if not data:
                        break
                    log_message = data.decode('utf-8')
                    # 提取 JSON 数据部分
                    print(log_message)

    except KeyboardInterrupt:
        print("Syslog server shutting down.")
    finally:
        sock.close()

if __name__ == "__main__":
    # start_syslog_server(port=1001)
    start_syslog_server(port=10001)
    # delete_redirect_port()
    # delete_mark_port()
    # mark_port()
    # redirect_port()


# iptables -t nat -L -v -n
# iptables -t mangle -L -v -n
# 1415 92667 DOCKER     all  --  *      *       0.0.0.0/0            0.0.0.0/0            ADDRTYPE match dst-type LOCAL
#    0     0 REDIRECT   tcp  --  *      *       0.0.0.0/0            0.0.0.0/0            mark match 0x65536 redir ports 10001

