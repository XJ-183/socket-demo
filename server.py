import socket

# UDP套接字 SOCK_DGRAM
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("127.0.0.1", 8888))
print("UDP服务端启动，端口8888，等待消息...")

while True:
    # recvfrom：接收数据，同时拿到发送方地址(IP,端口)
    data, client_addr = server_socket.recvfrom(1024)
    msg = data.decode("utf-8")
    print(f"收到来自{client_addr}：{msg}")

    reply = input("服务端回复：")
    server_socket.sendto(reply.encode("utf-8"), client_addr)