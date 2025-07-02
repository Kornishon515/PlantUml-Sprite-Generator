import argparse
from PIL import Image
import numpy as np
import os

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert image to hex 4-bit grayscale.")
    parser.add_argument('--path', type=str, default="input.png", help="Path to input image")
    parser.add_argument('--width', type=int, default=128, help="Output image width")
    parser.add_argument('--height', type=int, default=128, help="Output image height")
    parser.add_argument('--output', type=str, help="Path to output text file")

    args = parser.parse_args()

    image_name = args.path
    output_name = args.output if args.output else f"{os.path.splitext(image_name)[0]}_hex.txt"

    image_to_hex4bits(image_name, args.width, args.height, output_name)
