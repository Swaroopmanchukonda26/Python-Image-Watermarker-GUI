import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Image Watermarker")
        self.root.geometry("400x250")
        self.image_path = None

        # --- UI Layout Elements ---
        tk.Label(root, text="Image Watermarking Studio", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Select File Button
        self.select_btn = tk.Button(root, text="Step 1: Choose Image File", command=self.open_file, bg="#9b5de5", fg="white")
        self.select_btn.pack(pady=5)
        
        # Label to show selected filename
        self.file_label = tk.Label(root, text="No file selected", fg="gray")
        self.file_label.pack()

        # Watermark Text Input Field
        tk.Label(root, text="Step 2: Enter Watermark Text:").pack(pady=5)
        self.text_entry = tk.Entry(root, width=30)
        self.text_entry.insert(0, "© Swaroop Manchukonda")
        self.text_entry.pack()

        # Process Button
        self.process_btn = tk.Button(root, text="Step 3: Apply & Save", command=self.apply_watermark, bg="#00f5d4", fg="black")
        self.process_btn.pack(pady=15)

    def open_file(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        if self.image_path:
            filename = self.image_path.split("/")[-1]
            self.file_label.config(text=f"Selected: {filename}", fg="green")

    def apply_watermark(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please select an image file first!")
            return
            
        watermark_text = self.text_entry.get().strip()
        if not watermark_text:
            messagebox.showerror("Error", "Watermark text cannot be empty!")
            return

        try:
            # Open the base photo asset
            base_image = Image.open(self.image_path).convert("RGBA")
            
            # Make a blank slate image for the text layer to handle transparency
            txt_layer = Image.new("RGBA", base_image.size, (255, 255, 255, 0))
            
            # Setup the canvas draw layer tool
            draw = ImageDraw.Draw(txt_layer)
            
            # Dynamically size font based on image dimension width
            font_size = int(base_image.size[0] / 25)
            try:
                font = ImageFont.load_default() # Fallback basic font
            except IOError:
                font = ImageFont.load_default()

            # Place text anchor position near the bottom right quadrant layout corner
            x = base_image.size[0] - (font_size * len(watermark_text) // 2) - 30
            y = base_image.size[1] - font_size - 40

            # Draw white semi-transparent text with some opacity breakdown (Alpha value 150)
            draw.text((x, y), watermark_text, fill=(255, 255, 255, 150), font=font)
            
            # Composite layers matrix arrays together
            watermarked_output = Image.alpha_composite(base_image, txt_layer).convert("RGB")
            
            # Prompt user for destination file saving address
            save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG Image", "*.jpg")])
            if save_path:
                watermarked_output.save(save_path)
                messagebox.showinfo("Success", "Watermarked file successfully exported and saved!")
                
        except Exception as e:
            messagebox.showerror("System Error", f"Could not map image: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
