from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    # Load image and convert to numpy array
    image = Image.open(image_path)
    pixels = np.array(image, dtype=np.uint8)  # Ensure the array uses uint8 type

    # Convert key to uint8
    key = np.uint8(key)

    # Apply encryption using XOR with key
    encrypted_pixels = pixels ^ key  # XOR operation with key

    # Convert back to image and save
    encrypted_image = Image.fromarray(encrypted_pixels)
    encrypted_image.save("encrypted_image.png")
    print("Image encrypted and saved as encrypted_image.png")

def decrypt_image(encrypted_image_path, key):
    # Load encrypted image and convert to numpy array
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_pixels = np.array(encrypted_image, dtype=np.uint8)

    # Convert key to uint8
    key = np.uint8(key)

    # Apply decryption (same XOR with key)
    decrypted_pixels = encrypted_pixels ^ key  # XOR to revert encryption

    # Convert back to image and save
    decrypted_image = Image.fromarray(decrypted_pixels)
    decrypted_image.save("decrypted_image.png")
    print("Image decrypted and saved as decrypted_image.png")

# Main program
image_path = input("Enter the path of the image you want to encrypt: ")
key = int(input("Enter an integer key (1-255) for encryption: "))

choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()

if choice == "encrypt":
    encrypt_image(image_path, key)
elif choice == "decrypt":
    encrypted_image_path = input("Enter the path of the encrypted image: ")
    decrypt_image(encrypted_image_path, key)
else:
    print("Invalid choice. Please type 'encrypt' or 'decrypt'.")
