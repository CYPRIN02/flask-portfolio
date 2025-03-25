# Flask Portfolio Website

A personal portfolio website built with Flask for RASOLOARIVONY ANDRIANANTENAINA PRINCY.

## Features

- Responsive design using Bootstrap 5
- Home page with skills and featured projects
- About page with education and work experience
- Projects page with filtering functionality
- Project detail pages
- Contact form

## Setup Instructions

1. Make sure you have Python installed (Python 3.6 or higher recommended)

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   - Copy the `.env.example` file to `.env` (or create a new `.env` file)
   - Update the values in the `.env` file with your own settings
   - For Airtable integration, you'll need to set your Airtable API key in the `.env` file

4. Run the application:
   ```
   python run.py
   ```

5. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Project Structure

- `app/` - Main application directory
  - `__init__.py` - Flask application initialization
  - `routes.py` - Route definitions
  - `models.py` - Data models
  - `static/` - Static files (CSS, JS, images)
  - `templates/` - HTML templates

## Features

- Responsive design using Bootstrap 5
- Home page with skills and featured projects
- About page with education and work experience
- Projects page with filtering functionality
- Project detail pages
- Contact form with Airtable integration
- Environment variable configuration

## Airtable Integration

The contact form is integrated with Airtable to store form submissions. When a user submits the contact form, the data is sent to an Airtable base where you can manage and respond to inquiries.

To set up the Airtable integration:

1. Create an Airtable account if you don't have one already
2. Get your Airtable API key from your account settings
3. Set the `AIRTABLE_API_KEY` in your `.env` file
4. The base ID and table ID are already configured in the `.env` file

## Customization

### Replacing Placeholder Images

The website currently uses placeholder images for the projects. To replace them with actual images:

1. Navigate to the `app/static/images/` directory
2. Replace the following files with your actual project images:
   - `project1.jpg` - Web Scraping & Product Classification
   - `project2.jpg` - Spam Detection Web Application
   - `project3.jpg` - Emotion Detection in Video
   - `project4.jpg` - Sudoku Game
   - `project5.jpg` - Flight Reservation Website
   - `project6.jpg` - Chess Game in Java

Alternatively, you can run the provided Python script to generate placeholder images:

```
cd app/static/images
python generate_placeholders.py
```

This requires the Pillow library (`pip install pillow`).

### Updating Content

To update the website content, modify the following files:

- `app/models.py` - Update project details, skills, education, and experience
- `app/templates/` - Modify HTML templates for layout changes

## License

This project is licensed under the MIT License.
