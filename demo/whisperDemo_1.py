import whisper

# Load the Whisper model
model = whisper.load_model("base")

# Transcribe an audio file
result = model.transcribe("new_speech.mp3", language = "en")


# Print the transcription
print(result['text'])
