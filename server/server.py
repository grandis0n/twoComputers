import socket
import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
import threading

counter = 0


def get_local_ip_port():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address, 12345


def start_server(ip, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(1)
    print("Ожидание подключения клиента...")
    client_socket, client_address = server_socket.accept()
    print("Подключено к клиенту:", client_address)

    while True:
        data = client_socket.recv(1024)
        if data == b"change_image":
            change_image()


def change_image():
    global counter
    counter += 1
    counter %= 5
    max_width = 600
    max_height = 300

    image = Image.open(f"img/{counter}.png")

    if image.width > max_width or image.height > max_height:
        image.thumbnail((max_width, max_height))

    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo


def update_ip_port():
    ip, port = get_local_ip_port()
    ip_label.config(text=f"IP: {ip}")
    port_label.config(text=f"Port: {port}")


root = tk.Tk()
root.title("Server")
root.geometry("800x600")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

title_label = Label(frame, text="Серверное приложение", font=("Helvetica", 16))
title_label.pack()

ip_label = Label(frame, text="IP:", font=("Helvetica", 12))
ip_label.pack()

port_label = Label(frame, text="Port:", font=("Helvetica", 12))
port_label.pack()

update_button = Button(frame, text="Обновить IP и Port", command=update_ip_port, font=("Helvetica", 12))
update_button.pack()

image_label = tk.Label(root)
image_label.pack()

ip, port = get_local_ip_port()
server_thread = threading.Thread(target=start_server, args=(ip, port))
server_thread.daemon = True
server_thread.start()

update_ip_port()

root.mainloop()
