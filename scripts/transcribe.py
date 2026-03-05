import whisper
import os

AUDIO_FOLDER = "../dataset/onboarding"
OUTPUT_FOLDER = "../dataset/onboarding_transcripts"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

model = whisper.load_model("base")

for file in os.listdir(AUDIO_FOLDER):

    if file.endswith(".mp3") or file.endswith(".wav"):

        audio_path = os.path.join(AUDIO_FOLDER, file)

        print("Transcribing:", file)

        result = model.transcribe(audio_path)

        transcript = result["text"]

        output_file = file.replace(".mp3", ".txt").replace(".wav", ".txt")

        with open(os.path.join(OUTPUT_FOLDER, output_file), "w", encoding="utf-8") as f:
            f.write(transcript)

        print("Saved transcript:", output_file)