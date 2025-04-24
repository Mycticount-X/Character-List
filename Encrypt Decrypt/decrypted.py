import base64

def decrypt_file(input_filename, output_filename):
    try:
        with open(input_filename, "rb") as encrypted_file:
            encoded_data = encrypted_file.read()
            decoded_data = base64.b64decode(encoded_data)

        with open(output_filename, "wb") as decrypted_file:
            decrypted_file.write(decoded_data)

        print(f"File {input_filename} berhasil didekripsi ke {output_filename}")

    except FileNotFoundError:
        print(f"File {input_filename} tidak ditemukan.")
    except base64.binascii.Error:
        print("Data dalam file tidak valid untuk didekripsi.")

# Pemanggilan fungsi
decrypt_file("encrypted.txt", "decrypted.txt")
