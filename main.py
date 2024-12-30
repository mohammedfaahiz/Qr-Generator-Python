
import pyqrcode
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox

def generate_qr_code():
    data = data_entry.get()
    if not data:
        messagebox.showerror("Input Error", "Please enter data to encode in the QR code.")
        return

    save_path = filedialog.asksaveasfilename(
        title="Save QR Code",
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")],
    )

    if save_path:
        try:
            qr_code = pyqrcode.create(data)
            qr_code.png(save_path, scale=6)
            messagebox.showinfo("Success", f"QR code successfully saved at {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Canceled", "Save operation canceled.")


root = Tk()
root.title("QR Code Generator")
root.geometry("400x200")


Label(root, text="Enter data for QR Code:", font=("Arial", 12)).pack(pady=10)
data_entry = Entry(root, width=40, font=("Arial", 12))
data_entry.pack(pady=5)

Button(root, text="Generate QR Code", command=generate_qr_code, font=("Arial", 12)).pack(pady=20")


root.mainloop()
