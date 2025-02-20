#server_b.py
import socket
import ssl
from win10toast import ToastNotifier

HOST = "127.0.0.1"
PORT = 7001  # Must match Stunnel config
EXPECTED_PASSWORD = "secretpassword"
toaster = ToastNotifier()

CERT_PATH = "C:/Users/ASUS/stunnel_project/stunnel.pem"
KEY_PATH = "C:/Users/ASUS/stunnel_project/stunnel.key"

def receive_order():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=CERT_PATH, keyfile=KEY_PATH)

    # Create a raw socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen(5)
        print("📡 Server B: Waiting for secure orders...")

        while True:
            conn, addr = sock.accept()
            print(f"🔒 Secure connection established with {addr}")

            with context.wrap_socket(conn, server_side=True) as secure_conn:
                # Receive order data
                order_data = secure_conn.recv(1024).decode()

                # Receive authentication password
                password = secure_conn.recv(1024).decode()

                # Authenticate client
                if password != EXPECTED_PASSWORD:
                    print("❌ Authentication failed. Closing connection.")
                    secure_conn.sendall("Authentication failed.".encode())
                    continue
                
                print(f"📦 Order Received: {order_data}")

                # Send a confirmation message
                confirmation = f"Confirmation for {order_data}"
                secure_conn.sendall(confirmation.encode())
                print(f"✅ Sent Confirmation: {confirmation}")

                # Show Windows Notification
                toaster.show_toast("Order Confirmation", confirmation, duration=5)

if __name__ == "__main__":
    receive_order()
