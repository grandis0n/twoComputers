import socket
import tkinter as tk

from PIL import Image, ImageTk

root = tk.Tk()
root.title("Client")
image_label = tk.Label(root)
image_label.pack()


def change_image():
    image = Image.open("original_image.png")
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo
    print('Changed image')


# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect(("127.0.0.1", 12345))

server_address = ("127.0.0.1", 12345)
retry_interval = 15
client_socket = None


# while True:
#     try:
#         if client_socket is None:
#             client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             client_socket.connect(server_address)
#             print("Подключено")
#
#         data = client_socket.recv(1024)
#         if data == b"change_image":
#             change_image()
#     except ConnectionRefusedError:
#         print("Не удалось подключиться. Повторная попытка через {} секунд...".format(retry_interval))
#         if client_socket is not None:
#             client_socket.close()
#             client_socket = None
#         time.sleep(retry_interval)

def try_connect(client_socket=None):
    try:
        if client_socket is None:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(server_address)
            print("Подключено")

        data = client_socket.recv(1024)
        if data == b"change_image":
            change_image()
    except ConnectionRefusedError:
        print("Не удалось подключиться. Повторная попытка через {} секунд...".format(retry_interval))
        root.after(15000, try_connect)  # 15sec


try_connect(client_socket)
root.mainloop()
