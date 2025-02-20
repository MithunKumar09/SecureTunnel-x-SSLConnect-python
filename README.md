# SecureTunnelX-SSLGuard-python 🚀🔒
## A Secure SSL Tunnel for Encrypted Communication
*SecureTunnelX-SSLGuard is a Python-based SSL tunneling system that provides secure, encrypted communication between two servers using Stunnel and Python's SSL module. This project ensures end-to-end encryption for sensitive data transmissions, preventing eavesdropping and unauthorized access.*

### 🔹 Features
- **✅ SSL Encryption:** Protects data in transit using SSL/TLS.
- **✅ Stunnel Integration:** Secure tunneling between Server A & Server B.
- **✅ Authentication:** Uses a shared secret password for secure communication.
- **✅ Windows Notifications:** Provides real-time order confirmation alerts.
- **✅ Error Handling:** Handles SSL certificate verification and authentication errors.

### 🔹 How It Works
- Server A (Client Mode) sends an encrypted order request to Server B via Stunnel.
- Server B (Server Mode) decrypts the request, verifies authentication, and confirms the order.
- The confirmation is sent back to Server A, and a Windows notification appears.

### 🔹 Setup Instructions
- **1️⃣ Install Dependencies**
- *pip install pyopenssl win10toast*

- **2️⃣ Generate SSL Certificates (If Not Generated)**
- *openssl req -new -x509 -days 365 -nodes -out stunnel.pem -keyout stunnel.key*

- **3️⃣ Start Stunnel**
#### Modify stunnel.conf as per your system.
- Run:
- *stunnel stunnel.conf* [stunnel C:\Users\..\stunnel_project\stunnel.conf]
- **Check Connection:** Get-Process | Where-Object { $_.ProcessName -like "stunnel*" }
- **Confirm B Server Connection:** Get-Process | Where-Object { $_.ProcessName -like "python*" }
- **Stop Stunnel:** Stop-Process -Name "stunnel" -Force
- **Stop Server B:** Stop-Process -Id 44328 -Force

- **4️⃣ Run Servers**
#### Start Server B (Order Receiver)
- *python server_b.py*

#### Start Server A (Order Sender)
- *python server_a.py*

### 🔹 Configuration
- **Stunnel Certificate & Key Path:** Modify CERT_PATH and KEY_PATH in server_a.py & server_b.py.
- **Port Configuration:** Ensure ports 5001, 6001, and 7001 match in stunnel.conf.

### 🔹 Future Enhancements
- 🚀 Multi-client support for handling multiple secure connections.
- 🔒 Database logging for transaction history.
- 📡 Cloud deployment for enterprise-level security.

### 📜 License
- This project is licensed under MIT License – feel free to use and contribute!
- contact: mithunkumaar098@gmail.com

### 🔥 Developed with Security in Mind! 🚀
- Give this repo a ⭐ if you like it! 😃
