import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def remove_white_background(image_path, output_path, tolerance=200):
    image = Image.open(image_path).convert("RGBA")
    data = image.getdata()

    new_data = []
    for item in data:
        if item[0] > tolerance and item[1] > tolerance and item[2] > tolerance:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    image.putdata(new_data)
    image.save(output_path, "PNG")

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)

def save_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, file_path)

def convert():
    input_path = input_entry.get()
    output_path = output_entry.get()
    tolerance = tolerance_slider.get()
    if not input_path or not output_path:
        messagebox.showerror("Error", "Please select both input image and output image paths.")
        return
    
    try:
        remove_white_background(input_path, output_path, tolerance)
        messagebox.showinfo("Success", "Image processed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Set up the GUI
root = tk.Tk()
root.title("Remove White Background")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

input_label = tk.Label(frame, text="Input Image:")
input_label.grid(row=0, column=0, pady=5)

input_entry = tk.Entry(frame, width=50)
input_entry.grid(row=0, column=1, pady=5)

input_button = tk.Button(frame, text="Browse...", command=select_image)
input_button.grid(row=0, column=2, padx=5, pady=5)

output_label = tk.Label(frame, text="Output Image:")
output_label.grid(row=1, column=0, pady=5)

output_entry = tk.Entry(frame, width=50)
output_entry.grid(row=1, column=1, pady=5)

output_button = tk.Button(frame, text="Browse...", command=save_image)
output_button.grid(row=1, column=2, padx=5, pady=5)

tolerance_label = tk.Label(frame, text="Tolerance:")
tolerance_label.grid(row=2, column=0, pady=5)

tolerance_slider = tk.Scale(frame, from_=0, to=255, orient=tk.HORIZONTAL)
tolerance_slider.set(200)
tolerance_slider.grid(row=2, column=1, columnspan=2, pady=5)

convert_button = tk.Button(frame, text="Convert", command=convert)
convert_button.grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()
