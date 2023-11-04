import datetime
import socket
import tkinter as tk
from tkinter import Label, Entry, Button

root = tk.Tk()
root.title("Client")
image_label = tk.Label(root)
image_label.pack()

server_address = None
client_socket = None

status_label = Label(root, text="")
status_label.pack()


def connect_to_server():
    global server_address, client_socket
    server_ip = ip_entry.get()
    server_port_str = port_entry.get()

    try:
        server_port = int(server_port_str)
        server_address = (server_ip, server_port)

        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(server_address)
            connect_status.config(text="Подключение успешно")
        except:
            connect_status.config(text="Не удалось подключиться")
    except ValueError:
        connect_status.config(text="Некорректный ввод")


def set_status(message):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status_label.config(text=f"{message} ({current_time})")


def send_signal():
    if client_socket:
        try:
            client_socket.send(b"change_image")
            set_status("Сигнал отправлен")
        except:
            set_status("Ошибка при отправке сигнала")


ip_label = Label(root, text="IP:")
ip_label.pack()

ip_entry = Entry(root)
ip_entry.pack()

port_label = Label(root, text="Port:")
port_label.pack()

port_entry = Entry(root)
port_entry.pack()

connect_button = Button(root, text="Подключиться", command=connect_to_server)
connect_button.pack()

connect_status = Label(root, text="")
connect_status.pack()

signal_button = Button(root, text="Отправить сигнал", command=send_signal)
signal_button.pack()

root.geometry("800x600")
root.mainloop()
