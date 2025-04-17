import tkinter as tk
from tkinter import messagebox
import socket
from threading import Thread
import time

SERVER_PORT = 2503
BUFSIZ = 1024

client_socket = None
connected = False

def toggle_output(index):
    global client_socket, connected
    if not connected:
        log_message("No está conectado al servidor.")
        return
    try:
        message = f"toggle_output:{index}"
        client_socket.send(message.encode())
        log_message(f"Comando enviado: {message}")
    except Exception as e:
        log_message(f"Error al enviar el comando: {e}")

def connect_to_server():
    global client_socket, connected

    if connected:
        log_message("Ya está conectado.")
        return

    server_ip = ip_entry.get().strip()
    if not server_ip:
        messagebox.showwarning("IP inválida", "Por favor ingresa una IP válida.")
        return

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, SERVER_PORT))
        connected = True
        update_connection_status(True)
        log_message(f"Conexión exitosa al servidor {server_ip}.")
    except Exception as e:
        connected = False
        update_connection_status(False)
        log_message(f"Error conectando al servidor: {e}")
        messagebox.showerror("Error de Conexión", f"No se pudo conectar al servidor: {e}")

def disconnect_from_server():
    global client_socket, connected
    try:
        if client_socket:
            client_socket.close()
        connected = False
        update_connection_status(False)
        log_message("Desconectado del servidor.")
    except Exception as e:
        log_message(f"Error al desconectar: {e}")

def update_connection_status(is_connected):
    if is_connected:
        server_status_led.config(bg='green')
        plc_status_led.config(bg='green')
        connection_button.config(text="Desconectar", command=disconnect_from_server)
    else:
        server_status_led.config(bg='red')
        plc_status_led.config(bg='red')
        connection_button.config(text="Conectar", command=lambda: Thread(target=connect_to_server).start())

def log_message(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    console.config(state=tk.NORMAL)
    console.insert(tk.END, f"{timestamp} - {message}\n")
    console.yview(tk.END)
    console.config(state=tk.DISABLED)

def refresh_status():
    if connected:
        log_message("Estado del servidor: Conectado.")
        plc_status_led.config(bg='green')
    else:
        log_message("Estado del servidor: No conectado.")
        plc_status_led.config(bg='red')
    root.after(10000, refresh_status)

# GUI
root = tk.Tk()
root.title("Control PLC Siemens LOGO!")
root.geometry("600x500")
root.configure(bg="#1e1e1e")

# Estado
status_frame = tk.Frame(root, bg="#2d2d2d")
status_frame.grid(row=0, column=0, pady=20, sticky="ew")

server_status_label = tk.Label(status_frame, text="Estado Servidor:", font=("Arial", 14), fg="white", bg="#2d2d2d")
server_status_label.grid(row=0, column=0, padx=10)
server_status_led = tk.Canvas(status_frame, width=20, height=20, bg='red', bd=0, highlightthickness=0)
server_status_led.grid(row=0, column=1)

plc_status_label = tk.Label(status_frame, text="Estado PLC:", font=("Arial", 14), fg="white", bg="#2d2d2d")
plc_status_label.grid(row=1, column=0, padx=10)
plc_status_led = tk.Canvas(status_frame, width=20, height=20, bg='red', bd=0, highlightthickness=0)
plc_status_led.grid(row=1, column=1)

# IP
ip_label = tk.Label(root, text="Ingrese IP del Servidor:", font=("Arial", 12), fg="white", bg="#1e1e1e")
ip_label.grid(row=1, column=0, padx=10, pady=10)
ip_entry = tk.Entry(root, font=("Arial", 12))
ip_entry.grid(row=1, column=1, padx=10, pady=10)

# Botón conexión
connection_button = tk.Button(root, text="Conectar", command=lambda: Thread(target=connect_to_server).start(),
                              font=("Arial", 14), bg="#4CAF50", fg="white", relief="solid", bd=2)
connection_button.grid(row=2, column=0, pady=20)

# Salidas
output_frame = tk.Frame(root, bg="#2d2d2d")
output_frame.grid(row=3, column=0, columnspan=2, pady=20, sticky="ew")

for i in range(4):
    btn = tk.Button(output_frame, text=f"Salida {i+1}", command=lambda i=i: toggle_output(i),
                    font=("Arial", 12), bg="#FF5722", fg="white", relief="solid", bd=2)
    btn.grid(row=0, column=i, padx=10, pady=10)

# Consola
console_frame = tk.Frame(root, bg="#1e1e1e")
console_frame.grid(row=4, column=0, columnspan=2, pady=20, sticky="ew")

console_label = tk.Label(console_frame, text="Consola:", font=("Arial", 14), fg="white", bg="#1e1e1e")
console_label.grid(row=0, column=0)

console = tk.Text(console_frame, height=10, width=70, bg='black', fg='orange', font=("Arial", 12), wrap=tk.WORD)
console.grid(row=1, column=0)
console.config(state=tk.DISABLED)

refresh_status()
root.mainloop()
