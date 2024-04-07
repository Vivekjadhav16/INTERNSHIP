from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size
    pixels = img.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    encrypted_image_path = image_path.split('.')[0] + '_encrypted.png'
    img.save(encrypted_image_path)
    print("Image encrypted successfully!")

def decrypt_image(encrypted_image_path, key):
    img = Image.open(encrypted_image_path)
    width, height = img.size
    pixels = img.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    decrypted_image_path = encrypted_image_path.split('_encrypted.png')[0] + '_decrypted.png'
    img.save(decrypted_image_path)
    print("Image decrypted successfully!")

def main():
    image_path = input("Enter the path to the image file: ")
    key = int(input("Enter the encryption/decryption key (an integer): "))

    choice = input("Enter 'e' to encrypt or 'd' to decrypt: ").lower()
    if choice == 'e':
        encrypt_image(image_path, key)
    elif choice == 'd':
        decrypt_image(image_path, key)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
