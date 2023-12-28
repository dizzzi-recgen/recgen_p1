from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(image_path, text_coordinates, output_path):
    # Open the image
    image = Image.open(image_path)

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Define the font and size
    font = ImageFont.truetype("JAi____.TTF", size=20)

    # Add text to the image for each section
    for text, position in text_coordinates.items():
        user_text = input(f"{text}: ")
        draw.text(position, user_text, fill="black", font=font)

    # Save the modified image
    image.save(output_path)

if __name__ == "__main__":
    # Get user input
    image_path = input("Template ID: ")

    # Define text sections and their corresponding coordinates
    text_coordinates = {
        "Item 1": (98, 485),
        "UPC 1": (280, 485),
        "Price1": (505, 485),
	"Item 2": (98, 505),
	"UPC 2": (280, 505),
	"Price 2": (505, 505),
	"Item 3": (98, 525),
	"UPC 3": (280, 525),
	"Price 3": (505, 525),
	"Item 4": (98, 545),
	"UPC 4": (280, 545),
	"Price 4": (505, 545),
	"Item 5": (98, 565),
	"UPC 5": (280, 565),
	"Price 5": (505, 565),
        # Add more sections as needed
    }

    output_path = input("Output: ")

    # Add text to the image
    add_text_to_image(image_path, text_coordinates, output_path)

    print(f"Text added successfully. Modified image saved at {output_path}")
