from pydub import AudioSegment

files = ["", ""]

files[0] = input("Path to the first headphone recording (MP3) > ")
files[1] = input("Path to the second headphone recording (MP3) > ")

f = 0
for filepath in files:
    f += 1

    audio = AudioSegment.from_file(filepath, format="mp3")
    start_time_ms = 0 * 1000
    end_time_ms = 6.5 * 1000

    for i in range(2):
        segment = audio[start_time_ms:end_time_ms]
        segment.export(f"file{f}_segment{i}.wav", format="wav")

        start_time_ms += 6.5 * 2
        end_time_ms += 6.5 * 2

    start_time_ms += 6.5
    end_time_ms += 6.5