
    
# In this project, we'll go through a simple app that records audio from the microphone and transcribes it into text using Google's Speech API.

####### Instructions #######

# Include a new option for users to select the speech recognition API they want to use. In addition to Google Speech Recognition, consider other APIs available in the provided libraries.

# Improve the error handling in the transcribe_speech() function to provide more meaningful error messages to the user.

# Add a feature to allow the user to save the transcribed text to a file.

# Add a feature to allow the user to choose the language they are speaking in, and configure the speech recognition API to use that language.

# Add a feature to allow the user to pause and resume the speech recognition process.

##############


# Step 1: Import Required Libraries
import streamlit as st
import speech_recognition as sr


# Step 2: Define the Speech Recognition Function
def transcribe_speech():
    # Initialize recognizer class
    r = sr.Recognizer()
    
    # Use the microphone as the audio source
    with sr.Microphone() as source:
        st.info("Speak now...")
        audio_text = r.listen(source)
        st.info("Transcribing...")

        try:
            # Using Google Speech Recognition
            text = r.recognize_google(audio_text)
            return text
        except:
            return "Sorry, I did not get that."

## Explanation:
#  - "sr.Recognizer()": Initializes the recognizer object.
#  - "sr.Microphone()": Captures real-time audio from the microphone.
#  - "r.listen()": Listens to the speech and stores it as an audio object.
#  - "r.recognize_google()": Uses Google's speech recognition engine to convert audio into text.

## Working with Audio Files
# If you want to transcribe pre-recorded audio files instead of using the microphone, PyAudio is not needed. Here's how you can modify the transcribe_speech() function:

def transcribe_audio_file(file_path):
    # Initialize recognizer class
    r = sr.Recognizer()

    # Use the pre-recorded audio file as the source
    with sr.AudioFile(file_path) as source:
        audio_text = r.record(source)  # Read the audio file
        st.info("Transcribing...")

        try:
            # Using Google Speech Recognition
            text = r.recognize_google(audio_text)
            return text
        except:
            return "Sorry, I did not get that."
            
## Explanation:
# sr.AudioFile(): Opens the audio file as a source.
# r.record(): Reads the audio from the file, instead of capturing it live.


# Step 3: Create the Main Function
def main():
    st.title("Speech Recognition App")
    st.write("Click on the button to transcribe audio file:")
    
    if st.button("Start Transcription"):
        file_path = r"C:\Users\pc\Desktop\B-older\Data and Stuff\GMC\ML GMC\harvard.wav"
        text = transcribe_audio_file(file_path)
        #text = transcribe_speech() 
        st.write("Transcription: ", text)

  
## Explanation:
#  - "st.button()": Creates an interactive button in the Streamlit interface.
#  - "transcribe_audio_file()": When the button is clicked, the function is called to transcribe the audio file into text.



# Step 4: Run the App:

if __name__ == "__main__":
    main()

# This ensures the app runs when executed.
    