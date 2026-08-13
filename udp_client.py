import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ("127.0.0.1", 8888)

while True:
    msg = input("客户端输入：")
    client_socket.sendto(msg.encode("utf-8"), server_addr)
    recv_data, addr = client_socket.recvfrom(1024)
    print("服务端回复：", recv_data.decode("utf-8"))
client_socket.close()