from PIL import Image
import os


def convert_to_webp(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(
                output_folder, os.path.splitext(filename)[0] + '.webp')

            try:
                img = Image.open(input_path)
                img.save(output_path, 'webp')
                print(f"Image converted and saved: {output_path}")
            except Exception as e:
                print(f"Error converting image {filename}: {e}")


if __name__ == "__main__":
    input_folder = r"C:\Users\User\Desktop\NEW"
    output_folder = r"C:\Users\User\Desktop\output_images_webp"

    convert_to_webp(input_folder, output_folder)
