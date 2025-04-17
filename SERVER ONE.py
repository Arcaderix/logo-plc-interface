import snap7
from snap7.util import get_bool, set_bool
from snap7.type import Areas
import socket
from threading import Thread
import time

PLC_IP = '192.168.0.3'
PLC_RACK = 0
PLC_SLOT = 1

client = None
outputs_state = [False] * 4
inputs_state = [False] * 4
server = None

def connect_to_plc():
    global client
    client = snap7.client.Client()
    while True:
        try:
            client.connect(PLC_IP, PLC_RACK, PLC_SLOT)
            print("Conexión exitosa al PLC.")
            break
        except Exception as e:
            print(f"Error conectando al PLC: {e}, reintentando en 5 segundos...")
            time.sleep(5)

def read_inputs():
    global inputs_state
    try:
        data = client.read_area(Areas.PE, 0, 0, 1)
        inputs_state = [get_bool(data, 0, i) for i in range(4)]
    except Exception as e:
        print(f"Error leyendo entradas digitales: {e}")

def write_outputs():
    global outputs_state
    try:
        data = client.read_area(Areas.PA, 0, 0, 1)
        for i, state in enumerate(outputs_state):
            set_bool(data, 0, i, state)
        client.write_area(Areas.PA, 0, 0, data)
    except Exception as e:
        print(f"Error escribiendo salidas digitales: {e}")

def handle_client(conn, addr):
    global outputs_state
    print(f"Cliente {addr} conectado.")
    while True:
        try:
            message = conn.recv(2048).decode("utf8")
            if not message:
                break

            if message.startswith("toggle_output"):
                try:
                    index_str = message.split(":")[1]
                    index = int(index_str)

                    if 0 <= index < len(outputs_state):
                        outputs_state[index] = not outputs_state[index]
                        write_outputs()
                        print(f"Salida {index} cambiada a {outputs_state[index]}")
                    else:
                        print(f"Índice fuera de rango: {index}")
                except ValueError:
                    print(f"Error al convertir el índice a entero: {message.split(':')[1]}")
            else:
                print("Comando desconocido:", message)

        except Exception as e:
            print(f"Error manejando el cliente {addr}: {e}")
            break

    print(f"Cliente {addr} desconectado.")
    conn.close()

def server_thread():
    global server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("0.0.0.0", 2503))
    server.listen(5)

    print("Esperando conexiones de clientes...")
    while True:
        try:
            conn, addr = server.accept()
            Thread(target=handle_client, args=(conn, addr), daemon=True).start()
        except Exception as e:
            print(f"Error aceptando conexión: {e}")
            break

def shutdown_server():
    global server
    if server:
        server.close()
        print("Servidor cerrado correctamente.")

connect_to_plc()

server_thread_instance = Thread(target=server_thread, daemon=True)
server_thread_instance.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Deteniendo servidor...")
    shutdown_server()
