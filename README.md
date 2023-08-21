# Text-to-Speech and Hashing Project

This project is designed to demonstrate how to convert text to speech using the Google Speech Recognition API and implement basic hash functions for searching words within the hashed text. The project is implemented using Django, a Python web framework.

## Features

1. **Text-to-Speech Conversion**: The application allows users to upload an audio file containing spoken words. The Google Speech Recognition API is used to convert the spoken words into text.

2. **Hashing and Searching**: The project demonstrates three different hash functions (ASCII, Division, and Multiplication) for hashing words in the text. The hashed words are stored in hash tables, and users can search for the frequency of a specific word using the hash tables.

## Setup and Usage

1. **Installation**:
   - Install Python (3.7 or higher) on your system.
   - Install the required packages using `pip install -r requirements.txt`.

2. **Running the Application**:
   - Navigate to the project directory and run the Django development server using `python manage.py runserver`.
   - Access the application through a web browser at `http://127.0.0.1:8000`.

3. **Text-to-Speech Conversion**:
   - Upload an audio file containing spoken words.
   - The Google Speech Recognition API will convert the audio to text.
   
4. **Hashing and Searching**:
   - The text obtained from the audio is split into words.
   - The words are hashed using three different hash functions: ASCII, Division, and Multiplication.
   - Hashed words are stored in separate hash tables.
   - Users can search for the frequency of a specific word in the hash tables.

## Project Structure

- `audiohash/views.py`: Contains the main logic of the application, including text-to-speech conversion, hashing, and searching functions.
- `audiohash/templates/audiohash/`: Contains the HTML templates for the landing page and search result page.
- `audiohash/urls.py`: Defines the URL routes for the application.
- `requirements.txt`: Lists the required Python packages for the project.

## Hashing Functions

1. **ASCII Hashing**: Words are hashed by summing the ASCII values of their characters.
2. **Division Hashing**: Words are hashed by calculating the remainder of their sum of ASCII values divided by the hash table size.
3. **Multiplication Hashing**: Words are hashed using the multiplication method with a constant

## Notes

- This project is intended for educational purposes and might not be suitable for production use without further refinement and security enhancements.
- The project might require adjustments and improvements to handle larger datasets and potential collision scenarios.

