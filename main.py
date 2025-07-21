import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration

# Initialize the model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# image captioning function

def generate_caption(image_path):
    raw_image = Image.open(image_path).convert('RGB')
    inputs = processor(raw_image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption


# GUI
app = tk.Tk()
app.title("Ai Image Caption Generator")
app.geometry("600x500")
app.resizable(False, False)


tk.Label(app, text="Upload an Tmage to Get a Caption",font=("Arial",16,"bold")).pack(pady=10)
def upload_image():
    
    file_path = filedialog.askopenfilename(title="Select an Image",filetypes=[("Image Files","*.jpg;*.jpeg;*.png")])
    if file_path:
        
        uploaded_image = Image.open(file_path)
        uploaded_image = uploaded_image.resize((250,250))
        uploaded_image_tk = ImageTk.PhotoImage(uploaded_image)

        
        image_label.config(image=uploaded_image_tk)
        image_label.image = uploaded_image_tk

        caption = generate_caption(file_path)

        caption_label.config(text=f"caption:{caption}")

upload_button = tk.Button(app, text="Upload Image", command=upload_image, bg="lightblue", font=("Arial", 12))
upload_button.pack(pady=20)

image_label = tk.Label(app)
image_label.pack(pady=10)

caption_label = tk.Label(app,text="Caption: ", font="Arial" ,wraplength=500)
caption_label.pack(pady=10)

app.mainloop()