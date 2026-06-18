# Python-Image-Watermarker-GUI
# Desktop Image Watermarking Studio

An event-driven desktop graphic utility engineered in Python using Tkinter and the Pillow (PIL) processing suite to overlay semi-transparent text assets over digital photo configurations.

## 🚀 System Architecture & Capabilities
* **Alpha-Composite Matrix Blending:** Utilizes custom RGBA canvas mapping layers to compute transparent text vector positions rather than rewriting raw pixel blocks directly.
* **Fluid Layout Scaling:** Dynamically computes anchor spacing formulas to ensure the watermark automatically metrics itself correctly based on any uploaded image resolution width.
* **Native File System Bindings:** Integrated native OS file dialog search trees (`filedialog`) to handle fluid local directory image uploads and file exports.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Core Libraries:** Tkinter, Pillow (PIL Image, ImageDraw, ImageFont)
