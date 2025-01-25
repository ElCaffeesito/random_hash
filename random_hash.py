import hashlib
import random

for _ in range(1000):
    hash_value = hashlib.sha256(str(random.random()).encode()).hexdigest()
    if hash_value.startswith("00"):
        print(f"Valid hash found: {hash_value}")
        break
else:
    print("No valid hash found.")
