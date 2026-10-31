import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Load audio file
with sr.AudioFile('Recording.wav') as source:
  audio_data = recognizer.record(source)
  print("Transcribing...")

# Google Speech Recognition
try:
  text = recognizer.recognize_google(audio_data)
  print("Transcription:")
  print(text)
except sr.UnknownValueError:
  print("Google Speech Recognition could not understand the audio.")
except sr.RequestError:
  print("Could not request results from Google Speech Recognition service.")
