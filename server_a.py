#server_a.py
import socket
import ssl
import time

HOST = "127.0.0.1"
PORT = 5001  # Must match Stunnel config
PASSWORD = "secretpassword"

CERT_PATH = "C:/Users/ASUS/stunnel_project/stunnel.pem"

def send_order():
    try:
        # Create a raw socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Wrap socket with SSL
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        context.load_verify_locations(CERT_PATH)
        secure_sock = context.wrap_socket(sock, server_hostname=HOST)

        # Connect to Stunnel-secured server
        secure_sock.connect((HOST, PORT))
        print("🔒 Secure connection established with Server B")

        # Send order data
        order_data = "Order#123: 2 Burgers, 1 Coke"
        secure_sock.sendall(order_data.encode())
        time.sleep(0.5)

        # Send authentication password
        secure_sock.sendall(PASSWORD.encode())
        print(f"📤 Sent Order: {order_data}")

        # Receive confirmation
        response = secure_sock.recv(1024).decode()
        print(f"📩 Received Confirmation: {response}")

        secure_sock.close()

    except ssl.SSLError as e:
        print(f"SSL Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    send_order()
