# Assignment 4
Bryan Lizama Montecino

## Course Override Request Web Application

This is a simple web application built using Flask that allows students to submit course override requests to a university. The application provides a user-friendly form for students to enter their information and the course details for which they are requesting an override.

## Features

- User-friendly web form for submitting course override requests.
- Basic form data validation to ensure key fields are not empty.
- Styling using Bootstrap for a clean and responsive design.
- Error handling for internal server errors and unknown routes.

## Getting Started

These instructions will help you set up and run the application locally for testing and development.

### Prerequisites

- Python 3.x
- virtualenv (optional but recommended)

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/course-override-app.git
   cd course-override-app

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt

# Usage
1. Start Flask application with:
   ```bash
   python app.py
2. Open your web browser and navigate to http://127.0.0.1:5000/ to access the application.
3. Fill out the course override request form and submit it. You will receive a success message upon submission.

# Customization
You can customize the application further by modifying the app.py file and the HTML templates in the templates directory. 
- You can also adjust the styling by editing the styles.css file in the static directory.
