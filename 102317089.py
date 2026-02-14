import sys
import os
import zipfile
from yt_dlp import YoutubeDL
from moviepy import AudioFileClip, concatenate_audioclips
import static_ffmpeg

static_ffmpeg.add_paths()

def main():
    if len(sys.argv) != 5:
        print("Usage: python 102317089.py <SingerName> <NoOfVideos> <AudioDuration> <OutputFileName>")
        sys.exit(1)

    singer = sys.argv[1]
    try:
        n = int(sys.argv[2])
        y = int(sys.argv[3])
    except ValueError:
        print("Error: N and Y must be integers.")
        sys.exit(1)

    output_mp3 = sys.argv[4]
    output_zip = output_mp3.replace(".mp3", ".zip")

    if n <= 10 or y <= 20:
        print("Error: N > 10 and Y > 20 required.")
        sys.exit(1)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}],
        'outtmpl': 'video_%(id)s.%(ext)s',
        'quiet': True
    }

    print(f"Downloading {n} videos for {singer}...")
    search_query = f"ytsearch{n}:{singer}"
    with YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([search_query])
        except Exception as e:
            print(f"Download Error: {e}")

    clips = []
    mp3_files = [f for f in os.listdir() if f.endswith(".mp3") and f.startswith("video_")]

    print("Processing audio segments...")
    for file in mp3_files[:n]:
        try:
            # FIX: Using subclipped instead of with_section
            audio = AudioFileClip(file).subclipped(0, y) 
            clips.append(audio)
        except Exception as e:
            # Try subclip if subclipped fails (older versions)
            try:
                audio = AudioFileClip(file).subclip(0, y)
                clips.append(audio)
            except:
                print(f"Error processing {file}: {e}")

    if clips:
        final_audio = concatenate_audioclips(clips)
        final_audio.write_audiofile(output_mp3, logger=None)
        
        for clip in clips: clip.close()
        for file in mp3_files: os.remove(file)

        with zipfile.ZipFile(output_zip, 'w') as zipf:
            zipf.write(output_mp3)
        
        print(f"Success: {output_mp3} and {output_zip} created.")
    else:
        print("No audio clips were processed.")

if __name__ == "__main__":
    main()