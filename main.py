import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8888))
server_socket.listen(1)
print("服务端已启动，等待客户端连接...")

conn, addr = server_socket.accept()
print(f"客户端已连接：{addr}")

while True:
    data = conn.recv(1024)
    if not data:
        print("客户端断开连接")
        break
    msg = data.decode("utf-8")
    print("客户端：", msg)
    reply = input("服务器回复：")
    conn.send(reply.encode("utf-8"))

conn.close()
server_socket.close()