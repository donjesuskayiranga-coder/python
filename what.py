import re

data = open("image.jpg", "rb").read()

# find all long digit sequences ≥ 50 digits
nums = re.findall(rb"[0-9]{50,}", data)



for i, n in enumerate(nums[:10], 1):
    print(f"[{i}] length={len(n)} digits")
    print(n.decode(errors="ignore"))
    print()