import socket
import hashlib
import unicodedata
import time

# ----- CONFIG -----
HOST = "verbal-sleep.picoctf.net"
PORT = 51950  # replace with your current instance port
CHEESE_FILE = "cheese.txt"

# ----- Normalize text -----
def normalize(text):
    text = text.strip().lower()
    text = unicodedata.normalize("NFD", text)
    return "".join(c for c in text if unicodedata.category(c) != "Mn")

# ----- Read cheeses -----
with open(CHEESE_FILE, "r", encoding="utf-8") as f:
    cheeses = [line.strip() for line in f if line.strip()]

# ----- Connect & guess -----
def guess_cheese():
    while True:
        
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                print(f"[+] Connecting to {HOST}:{PORT}...")
                s.connect((HOST, PORT))
                
                # Receive initial message
                data = s.recv(4096)
                print(data.decode())

                for cheese in cheeses:
                    for variant in (cheese, normalize(cheese)):
                        s.sendall(b"g\n")  # tell server we want to guess
                        time.sleep(0.5)  # safe delay
                        print(f"[+] Trying: {variant}")
                        s.sendall(variant.encode() + b"\n")
                        time.sleep(0.5)

                        response = s.recv(4096).decode()
                        print(response)
                        if "correct" in response.lower() or "you guessed" in response.lower():
                            print(f"[!!!] FOUND CHEESE: {variant}")
                            return
        except ConnectionAbortedError:
            print("[!] Connection aborted. Retrying in 2 seconds...")
            time.sleep(2)
        except ConnectionResetError:
            print("[!] Connection reset by server. Retrying in 2 seconds...")
            time.sleep(2)
        except KeyboardInterrupt:
            print("[!] Exiting...")
            return

if __name__ == "__main__":
    guess_cheese()