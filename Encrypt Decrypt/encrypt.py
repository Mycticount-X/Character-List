import base64

def encrypt_file(input_filename, output_filename):
    try:
        with open(input_filename, "rb") as file:
            data = file.read()
            encoded_data = base64.b64encode(data)
        
        with open(output_filename, "wb") as encrypted_file:
            encrypted_file.write(encoded_data)

        print(f"File {input_filename} berhasil dienkripsi ke {output_filename}")

    except FileNotFoundError:
        print(f"File {input_filename} tidak ditemukan.")

if __name__ == "__main__":
    encrypt_file("file.txt", "encrypted.txt")
