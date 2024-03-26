import base64

ENCODING = 'utf-8'

def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        base64_image = base64.b64encode(img_file.read()).decode(ENCODING)
    return base64_image

def save_base64_to_file(base64_string, output_file):
    with open(output_file, "w") as file:
        file.write(base64_string)

def main():
    image_path = input("Please enter the path of the image you want to convert to base64: ")
    try:
        base64_image = image_to_base64(image_path)
        print("The base64 representation of the image is:\n", base64_image)
        
        output_file_name = input("Enter the output file name to save the base64: ")
        save_base64_to_file(base64_image, output_file_name)
        print(f"The base64 was saved to '{output_file_name}'.")
        
    except FileNotFoundError:
        print("File not found. Make sure to input the correct path to the image.")

if __name__ == "__main__":
    main()
