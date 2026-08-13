import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8888))

while True:
    msg = input("客户端输入：")
    client_socket.send(msg.encode("utf-8"))
    recv_data = client_socket.recv(1024)
    print("服务端回复：", recv_data.decode("utf-8"))
client_socket.close()