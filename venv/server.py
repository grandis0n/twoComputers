import socket
import tkinter as tk

root = tk.Tk()
root.title("Server")
button = tk.Button(root, text="Изменить картинку")


def send_command():
    client_socket.send(b"change_image")


button.config(command=send_command)
button.pack()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 12345))
server_socket.listen(1)
print("Ожидание подключения клиента...")
client_socket, client_address = server_socket.accept()
print("Подключено к клиенту:", client_address)

root.mainloop()