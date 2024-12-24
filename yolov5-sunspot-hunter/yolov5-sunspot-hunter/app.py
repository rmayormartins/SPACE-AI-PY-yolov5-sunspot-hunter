import gradio as gr
import numpy as np
from PIL import Image
import torch
import matplotlib.pyplot as plt

model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')


def detect(img):
    
    img_arr = np.array(img)
    
    results = model(img_arr)

    
    fig, ax = plt.subplots()
    ax.imshow(img_arr)

    
    for *xyxy, conf, cls in results.xyxy[0].cpu().numpy():
        x1, y1, x2, y2 = map(int, xyxy)
        label = model.names[int(cls)]  
        ax.add_patch(plt.Rectangle((x1, y1), x2-x1, y2-y1, fill=False, color='red', linewidth=2))
        ax.text(x1, y1, f'{label} {conf:.2f}', color='white', fontsize=8, bbox={'facecolor': 'red', 'alpha': 0.5})

    plt.axis('off')  

    
    fig.canvas.draw()
    pil_img = Image.fromarray(np.array(fig.canvas.renderer._renderer))
    plt.close(fig)  

    return pil_img


#Gradiooo 
iface = gr.Interface(
    fn=detect,
    inputs=gr.Image(type="pil"),
    outputs=gr.Image(type="pil"),
    title="YOLOv5 Sun Spot Hunter",
    description="Object detector (solar spot/sunspot hunter) trained using YOLOv5 and labeled in Makesense.ai",
    examples=[["example1.jpg"]] 
)


iface.launch(debug=True)
