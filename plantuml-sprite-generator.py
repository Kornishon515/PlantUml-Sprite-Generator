from PIL import Image
import numpy as np

def image_to_hex4bits(input_image_path, width, height, output_txt_path):
    img = Image.open(input_image_path).convert("RGBA") 
    
    print(f"Original size : {img.width}x{img.height}")
    img = img.resize((width, height))
    
    img_array = np.array(img)
    
    r, g, b, a = img_array[:,:,0], img_array[:,:,1], img_array[:,:,2], img_array[:,:,3]
    gray = (0.299 * r + 0.587 * g + 0.114 * b).astype(np.uint8)
    gray[a < 255] = 255
    img_array_4bits = 15 - gray // 16
    
    with open(output_txt_path, 'w') as f:
        for row in img_array_4bits:
            row_hex = ''.join(f"{pixel:X}" for pixel in row) 
            f.write(row_hex + '\n')
    
    print(f"Saved as : {output_txt_path}")

# Exemple d'utilisation
if __name__ == "__main__":
    image_name = "input.png"
    image_to_hex4bits(image_name, 128, 128, f"{image_name[:-4]}_hex.txt") # This is ugly but I don't care 
