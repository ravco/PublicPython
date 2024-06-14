import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import svgwrite

def image_to_svg(image_path, svg_path, scale=1):
    image = Image.open(image_path)
    image = image.convert("RGBA")
    width, height = image.size

    dwg = svgwrite.Drawing(svg_path, profile='tiny', size=(width * scale, height * scale))

    for y in range(height):
        for x in range(width):
            r, g, b, a = image.getpixel((x, y))
            if a > 0:
                color = svgwrite.rgb(r, g, b, '%')
                dwg.add(dwg.rect(insert=(x * scale, y * scale), size=(scale, scale), fill=color))

    dwg.save()

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)

def save_svg():
    file_path = filedialog.asksaveasfilename(defaultextension=".svg", filetypes=[("SVG files", "*.svg")])
    if file_path:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, file_path)

def convert():
    input_path = input_entry.get()
    output_path = output_entry.get()
    if not input_path or not output_path:
        messagebox.showerror("Error", "Please select both input image and output SVG paths.")
        return
    
    try:
        image_to_svg(input_path, output_path)
        messagebox.showinfo("Success", "Image converted to SVG successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Set up the GUI
root = tk.Tk()
root.title("Image to SVG Converter")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

input_label = tk.Label(frame, text="Input Image:")
input_label.grid(row=0, column=0, pady=5)

input_entry = tk.Entry(frame, width=50)
input_entry.grid(row=0, column=1, pady=5)

input_button = tk.Button(frame, text="Browse...", command=select_image)
input_button.grid(row=0, column=2, padx=5, pady=5)

output_label = tk.Label(frame, text="Output SVG:")
output_label.grid(row=1, column=0, pady=5)

output_entry = tk.Entry(frame, width=50)
output_entry.grid(row=1, column=1, pady=5)

output_button = tk.Button(frame, text="Browse...", command=save_svg)
output_button.grid(row=1, column=2, padx=5, pady=5)

convert_button = tk.Button(frame, text="Convert", command=convert)
convert_button.grid(row=2, column=0, columnspan=3, pady=10)

root.mainloop()
