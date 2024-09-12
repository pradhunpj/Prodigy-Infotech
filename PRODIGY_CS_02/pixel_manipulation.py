# Image Encryptor Tool

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


def open_image():  #code to open image file
    global photo, file_path, image
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp;*.tiff;*.webp;*.heif")])
    if file_path:
        try:
            # Open and resize the image
            image = Image.open(file_path)
            image.thumbnail((200,200), Image.Resampling.LANCZOS)
            
            # Convert image to PhotoImage
            photo = ImageTk.PhotoImage(image)
            
            # Update the label with the image
            img_display.config(image=photo)
            img_display.image = photo  # Keep a reference to avoid garbage collection
            


        except Exception as e:
            # Handle errors by updating the display and path label
            img_display.config(text=f"Cannot Display Image \n(Possibly Encrypted)",font=("Times New Roman", 11), image=None)
            img_display.image = None # Update path_label with the file path


def encrypt():  #code to Encrypt image
    if file_path and key_entry.get():
        try:
            key = int(key_entry.get())

            with open(file_path, "rb") as file:
                encrypt_image = bytearray(file.read())

            # XOR encryption with the key
            for index, value in enumerate(encrypt_image):
                encrypt_image[index] = value ^ key

            # Add a marker at the end of the file to validate the key during decryption
            marker = key.to_bytes(4, byteorder='big')  # Use 4 bytes to store the key
            encrypt_image.extend(marker)

            with open(file_path, "wb") as file:
                file.write(encrypt_image)

            status_label.config(text="Image encrypted successfully :)", font=("Times New Roman", 15), fg="green")
            img_display.config(image="")  # Clear the displayed image
            key_entry.delete(0, END)  # Clear the key entry field

        except ValueError:
            status_label.config(text="Invalid Key: Enter an integer", font=("Times New Roman", 15), fg="red")
        except Exception as e:
            status_label.config(text=f"Encryption Failed: {e}", font=("Times New Roman", 15), fg="red")
            print(f"Encryption Error: {e}")


def decrypt():  #code to Decrypt image
    if file_path and key_entry.get():
        try:
            key = int(key_entry.get())

            with open(file_path, "rb") as file:
                decrypt_image = bytearray(file.read())

            # Read the marker (last 4 bytes) and check if it matches the key
            marker = decrypt_image[-4:]
            original_key = int.from_bytes(marker, byteorder='big')

            if original_key != key:
                status_label.config(text="Incorrect key. Cannot decrypt!", font=("Times New Roman", 15), fg="red")
                img_display.config(image="")  # Clear the displayed image
                key_entry.delete(0, END)  # Clear the key entry field
                
                return

            # If the key is correct, remove the marker
            decrypt_image = decrypt_image[:-4]

            # XOR decryption with the key
            for index, value in enumerate(decrypt_image):
                decrypt_image[index] = value ^ key

            with open(file_path, "wb") as file:
                file.write(decrypt_image)

            status_label.config(text="Image decrypted successfully!", font=("Times New Roman", 15),fg="green")
            key_entry.delete(0, END)

        except ValueError:
            status_label.config(text="Invalid Key: Enter an integer", font=("Times New Roman", 15),fg="red")
        except Exception as e:
            status_label.config(text=f"Decryption failed: {e}", fg="red")
            print(f"Decryption Error: {e}")


root = Tk()
root.title("Encryption Tool For Image")
root.geometry("500x500")
root.config(bg="black")
head_lable = Label(root,text="Welcome to ImageCrypt",font=("Times New Roman", 30 ,"bold"),bg="black",fg="white")
head_lable.pack()
status_label = Label(root, text="",bg="black",fg="white")
status_label.pack(pady=10)

img_display = Label(root, text="No Image Selected",bg="black",fg="white")
img_display.pack(pady=40)



key_label = Label(root, text="Enter the key",font=("Times New Roman", 15 ),bg="black",fg="white")
key_label.pack(pady=5)

key_entry = Entry(root, font=("Times New Roman", 15 ))
key_entry.pack(pady=5)


button_frame = Frame(root, bg="black")
button_frame.pack(pady=10)
open_button = Button(button_frame, text="Browse Image",font=("Times New Roman", 15 ,"bold"),bg="black",fg="white", command=open_image)
open_button.grid(row=0,column=0,padx=10)

encrypt_button = Button(button_frame,font=("Times New Roman", 15 ,"bold"),bg="black",fg="white", text="Encrypt Image",command=encrypt)
encrypt_button.grid(row=0, column=1, padx=10)  # Place Encrypt on row 0, column 0

decrypt_button = Button(button_frame,font=("Times New Roman", 15 ,"bold"),bg="black",fg="white", text="Decrypt Image",command=decrypt)
decrypt_button.grid(row=0, column=2, padx=10) 



root.mainloop()
