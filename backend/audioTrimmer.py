import os
from pydub import AudioSegment

start_time_sec = 40

def is_already_processed(filename, output_dir):
    base_name = os.path.splitext(filename)[0]
    print(base_name)
    first_part_name = f"{base_name}_part1.mp3"
    return first_part_name in os.listdir(output_dir)

def find_audio_file(pattern, directory, output_dir):
    for filename in os.listdir(directory):
        if filename.endswith(pattern) and not is_already_processed(filename, output_dir):
            return os.path.join(directory, filename)
    return None

def split_audio(file_path, output_dir):
    audio = AudioSegment.from_file(file_path)
    duration = len(audio)
    part_duration = 30 * 60 * 1000  # 30 minutes in milliseconds
    
    parts = []
    for i in range(start_time_sec * 1000, duration, part_duration):
        part = audio[i:i + part_duration]
        parts.append(part)
        
    base_name = os.path.splitext(os.path.basename(file_path))[0]

    for idx, part in enumerate(parts):
        part_name = f"{base_name}_part{idx+1}.mp3"
        part_path = os.path.join(output_dir, part_name)
        part.export(part_path, format="mp3")
        print(f"Saved {part_path}")

if __name__ == "__main__":
    directory = "./audios"  # Directory containing audio files
    output_dir = "./split_audios"  # Directory to save split audio files
    pattern = "ELL211.mp3"  # Pattern to search for in file names

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    audio_file = find_audio_file(pattern, directory, output_dir)

    if audio_file:
        print(f"Found audio file: {audio_file}")
        split_audio(audio_file, output_dir)
    else:
        print(f"No audio file found ;D")
