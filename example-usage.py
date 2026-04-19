import requests

def encrypt(text):
    url = "https://i7xo164.live.codepad.app/encrypt"

    data = {
        "text": text
    }

    response = requests.post(url, json=data)

    # Debugging help:
    # print(f"Status Code: {response.status_code}")
    # print(f"Response Text: {response.text}")
    # print(f"Response Headers: {response.headers}")

    data = response.json()

    if "encrypted" in data:
        stripped = data["encrypted"]
        return stripped
    else:
        print("Error from API:", data)

def decrypt(text):
    url = "https://i7xo164.live.codepad.app/decrypt"

    data = {
        "text": text
    }

    response = requests.post(url, json=data)

    # More debugging help:
    # print(f"Status Code: {response.status_code}")
    # print(f"Response Text: {response.text}")
    # print(f"Response Headers: {response.headers}")

    data = response.json()

    if "decrypted" in data:
        stripped = data["decrypted"]
        return stripped
    else:
        print("Error from API:", data)
    

encrypted = encrypt("I made a goated api... I think 🤔")

decrypted = decrypt(encrypted)

print(f"This is the encrypted text:\n\n{encrypted}\n\n\n")
print(f"This is the decrypted text:\n\n{decrypted}\n\n\n")
