from Crypto.Cipher import AES

# Data provided by the challenge
state = [0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1]
taps = [63, 61, 60, 58]
ciphertext_hex = "8f0e6d0f5b0dc1db201948b9e0cebd8f06069ee9ff30c87bd50b31d6fd72c4c438338e7e04fbddef0c6260a4eb758417"

def solve():
    curr_state = state[:]
    key_bits = []

    # 1. Generate 128 bits from the LFSR
    for _ in range(128):
        # Feedback is the XOR of the bits at the tap positions
        feedback = 0
        for t in taps:
            feedback ^= curr_state[t]
        
        # The output bit is the one being shifted out (leftmost)
        output_bit = curr_state.pop(0)
        key_bits.append(output_bit)
        
        # Append the new feedback bit to the end
        curr_state.append(feedback)

    # 2. Convert the 128 bits into 16 bytes
    bit_string = "".join(map(str, key_bits))
    key_bytes = int(bit_string, 2).to_bytes(16, byteorder='big')

    # 3. Decrypt the flag using AES-ECB
    ciphertext = bytes.fromhex(ciphertext_hex)
    cipher = AES.new(key_bytes, AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)

    print("Decrypted Message:", decrypted)

if __name__ == "__main__":
    solve()
