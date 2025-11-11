from pydub import AudioSegment

files = ["", ""]

files[0] = input("Path to the first headphone recording (MP3) > ")
files[1] = input("Path to the second headphone recording (MP3) > ")

f = 0

# TIMESTAMPS ARE CODED FOR WALK IN THE PARK BY TRACKTRIBE, I MAY ADD CUSTOMIZABLE SEGMENTS LATER. :3
start_time_ms = 0
end_time_ms = 6500

print("Cutting sounds...")
for filepath in files:
    print(f"Cutting {filepath}...")
    f += 1

    audio = AudioSegment.from_file(filepath, format="mp3")

    for i in range(2):
        print(f"Start time (MS): {start_time_ms} | End time (MS): {end_time_ms}")
        segment = audio[start_time_ms:end_time_ms]
        segment.export(f"file{f}_segment{i}.wav", format="wav")

        start_time_ms += 6500 * 2
        end_time_ms += 6500 * 2
        
    #start_time_ms += 6500
    #end_time_ms += 6500
    start_time_ms = 6500
    end_time_ms = 13000
    print(f"ADDED || Start time (MS): {start_time_ms} | End time (MS): {end_time_ms}")

print("Combining cut files...")
sample1 = AudioSegment.from_file("file1_segment0.wav", format="wav")
sample2 = AudioSegment.from_file("file2_segment0.wav", format="wav")
sample3 = AudioSegment.from_file("file1_segment1.wav", format="wav")
sample4 = AudioSegment.from_file("file2_segment1.wav", format="wav")

finalAudio = sample1 + sample2 + sample3 + sample4
finalAudio.export("Final_Sample.mp3", format="mp3")