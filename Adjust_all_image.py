import os
from PIL import Image

def uniform_image_size(input_folder, output_folder, width, height, dpi=300):
     if not os.path.exists(output_folder):
          os.makedirs(output_folder)

     for image_filename in os.listdir(input_folder):
        image_path = os.path.join(input_folder, image_filename)
        if os.path.isfile(image_path) and image_filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                with Image.open(image_path) as img:
                    img = img.convert("RGBA") if img.mode == 'RGBA' else img
                    img = Image.open(image_path)
                    img_width, img_height = img.size
                    aspect_ratio = img_width / img_height
                    target_aspect_ratio = width / height

                    if aspect_ratio > target_aspect_ratio:
                        new_width = width
                        new_height = int(width / aspect_ratio)

                    else:
                        new_height = height
                        new_width = int(height * aspect_ratio)
                    img_resized = img.resize((new_width, new_height), Image.LANCZOS)

                    new_image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
                    left = (width - new_width) // 2
                    top = (height - new_height) // 2
                    new_image.paste(img_resized, (left, top))


                    output_path = os.path.join(output_folder, image_filename)
                    new_image.save(output_path, dpi=(dpi, dpi))
                    print(f"Imagen procesada y guardada en: {output_path}")

            except Exception as e:
                print(f"Error al procesar la imagen {image_filename}: {e}")

input_folder = r"C:\Users\Lenovo\Documents\Amy_prueba6\img2"
output_folder = r"C:\Users\Lenovo\Documents\Amy_prueba6\resized_uniform"

width = 1750
height = 1750

uniform_image_size(input_folder, output_folder, width, height)