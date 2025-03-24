from PIL import Image, ImageDraw, ImageFont
import os

# Project details
projects = [
    {"id": 1, "title": "Web Scraping & Product Classification", "color": (52, 152, 219)},  # Blue
    {"id": 2, "title": "Spam Detection Web Application", "color": (46, 204, 113)},  # Green
    {"id": 3, "title": "Emotion Detection in Video", "color": (155, 89, 182)},  # Purple
    {"id": 4, "title": "Sudoku Game", "color": (230, 126, 34)},  # Orange
    {"id": 5, "title": "Flight Reservation Website", "color": (231, 76, 60)},  # Red
    {"id": 6, "title": "Chess Game in Java", "color": (52, 73, 94)}  # Dark Blue
]

def create_placeholder_image(project_id, title, color):
    """Create a placeholder image with project title"""
    # Create a new image with a solid color background
    img = Image.new('RGB', (800, 600), color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a default font, or use the default if not available
    try:
        # For Windows
        title_font = ImageFont.truetype("arial.ttf", 40)
        text_font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        # Fallback to default
        title_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
    
    # Add title text
    title_text = title
    title_width = draw.textlength(title_text, font=title_font)
    draw.text(((800 - title_width) / 2, 200), title_text, font=title_font, fill=(255, 255, 255))
    
    # Add placeholder text
    placeholder_text = f"Project {project_id} Placeholder"
    placeholder_width = draw.textlength(placeholder_text, font=text_font)
    draw.text(((800 - placeholder_width) / 2, 300), placeholder_text, font=text_font, fill=(255, 255, 255))
    
    # Add instruction text
    instruction_text = "Please replace with an actual project image"
    instruction_width = draw.textlength(instruction_text, font=text_font)
    draw.text(((800 - instruction_width) / 2, 350), instruction_text, font=text_font, fill=(255, 255, 255))
    
    # Save the image
    filename = f"project{project_id}.jpg"
    img.save(filename)
    print(f"Created {filename}")

def main():
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Change to the current directory
    os.chdir(current_dir)
    
    # Create placeholder images for each project
    for project in projects:
        create_placeholder_image(project["id"], project["title"], project["color"])
    
    print("All placeholder images have been created.")
    print("Run this script from the app/static/images directory to generate the placeholder images.")

if __name__ == "__main__":
    main()
