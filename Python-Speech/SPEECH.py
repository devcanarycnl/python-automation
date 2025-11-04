# PyPDF2 is a free and open-source pure-python PDF library
# pyttsx3 is a text-to-speech conversion library in Python

import os
import PyPDF2
import pyttsx3

def text_to_speech_from_pdf(pdf_path):
    print(f"\n=== Converting PDF to Speech ===")
    try:
        # Open the PDF file
        print(f"Opening PDF file: {pdf_path}")
        if not os.path.exists(pdf_path):
            print("Error: PDF file not found!")
            return

        with open(pdf_path, 'rb') as file:
            # Create PDF reader object
            pdf_reader = PyPDF2.PdfReader(file)  # Updated from PdfFileReader
            num_pages = len(pdf_reader.pages)
            print(f"PDF loaded successfully. Total pages: {num_pages}")

            # Initialize the text-to-speech engine
            print("Initializing text-to-speech engine...")
            speaker = pyttsx3.init()
            
            # Extract and read text from each page
            for page_num in range(num_pages):
                print(f"\nProcessing page {page_num + 1}/{num_pages}")
                text = pdf_reader.pages[page_num].extract_text()  # Updated method
                print(f"Extracted text length: {len(text)} characters")
                
                # Read the text out loud
                speaker.say(text)
                speaker.runAndWait()
            
            speaker.stop()
            print("\nFinished reading PDF!")
            
            # Save the last page's audio to file
            print("Saving audio to file...")
            speaker.save_to_file(text, 'audio.mp3')
            speaker.runAndWait()
            print("Audio saved as 'audio.mp3'")

    except Exception as e:
        print(f"Error occurred: {str(e)}")

####CASE 2 READ A STRING ###########
def text_to_speech_from_string(text):
    print(f"\n=== Converting Text to Speech ===")
    try:
        # Create a string
        print(f"Input text: {text}")
        
        # Initialize the Pyttsx3 engine
        print("Initializing text-to-speech engine...")
        engine = pyttsx3.init()
        
        # We can use file extension as mp3 and wav, both will work
        print("Saving audio to file...")
        engine.save_to_file(text, 'speech.mp3')
        
        # Wait until above command is not finished.
        engine.runAndWait()
        print("Audio saved as 'speech.mp3'")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    # Test with a sample string
    sample_text = "Hello! This is a test of the text to speech system."
    text_to_speech_from_string(sample_text)
    
    # To test PDF conversion, uncomment these lines and provide a valid PDF path
    # pdf_path = "path_to_your_pdf.pdf"
    # text_to_speech_from_pdf(pdf_path)


