from tkinter import *
from tkinter import filedialog, messagebox
import os

root = Tk()
# root.geometry("300x200")

root.geometry("400x300")
root.title("Image Encryption Tool")
root.config(bg="#f0f0f0")

# Get the current working directory (where the script is located)
current_directory = os.path.dirname(os.path.abspath(__file__))

# Global label to display file path
file_path_label = Label(root, text="", bg="#f0f0f0", fg="#007ACC", font=("Arial", 10))
file_path_label.place(x=120, y=100)

# Function to encrypt the image
def encrypt_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png")]
    )
    if file_path:
       file_path_label.config(text=f"File: {os.path.basename(file_path)}")  # Display selected file name
    key = entry1.get(1.0, END).strip()
    try:
            key = int(key)
    except ValueError:
            messagebox.showerror("Invalid Key", "Please enter a valid integer key.")
            return
    try:
            with open(file_path, "rb") as file:
                image = bytearray(file.read())

            # Pixel manipulation: XOR and addition
            for index, value in enumerate(image):
                image[index] = value ^ key  # XOR with key
                image[index] = (image[index] + 5) % 256  # Add 5 to each pixel value

            # Save the encrypted file in the same directory with "_encrypted" suffix
            new_file_path = os.path.join(current_directory, "encrypted_image.png")
            with open(new_file_path, "wb") as file:
                file.write(image)

            messagebox.showinfo("Success", f"Image encrypted successfully! Saved as {new_file_path}")

    except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


def decrypt_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png")]
    )
    if file_path:
       file_path_label.config(text=f"File: {os.path.basename(file_path)}")  # Display selected file name
    key = entry1.get(1.0, END).strip()
    try:
            key = int(key)
    except ValueError:
            messagebox.showerror("Invalid Key", "Please enter a valid integer key.")
            return

    try:
            with open(file_path, "rb") as file:
                image = bytearray(file.read())

            # Reverse pixel manipulation: Subtract 5 and XOR with key
            for index, value in enumerate(image):
                image[index] = (value - 5) % 256  # Subtract 5 from each pixel value
                image[index] = image[index] ^ key  # XOR with key

            # Save the decrypted file in the same directory with "_decrypted" suffix
            new_file_path = os.path.join(current_directory, "decrypted_image.png")
            with open(new_file_path, "wb") as file:
                file.write(image)

            messagebox.showinfo("Success", f"Image decrypted successfully! Saved as {new_file_path}")

    except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Styling buttons and layout
b1 = Button(root, text="Encrypt Image", command=encrypt_image, bg="#4CAF50", fg="white", font=("Arial", 12), width=12)
b1.place(x=50, y=10)

b2 = Button(root, text="Decrypt Image", command=decrypt_image, bg="#f44336", fg="white", font=("Arial", 12), width=12)
b2.place(x=200, y=10)


entry1 = Text(root, height=1, width=10, font=("Arial", 12),)
entry1.place(x=120, y=70)

label1 = Label(root, text="Enter Key:", bg="#f0f0f0", font=("Arial", 10))
label1.place(x=50, y=70)

root.mainloop()