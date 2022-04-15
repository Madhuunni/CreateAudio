from pydub import AudioSegment

start = 20
end = 46
start = start * 1000 #Works in milliseconds
end = end * 1000
newAudio = AudioSegment.from_mp3("/home/madhu/workspace/audio/Narayaneeyam.mp3")
newAudio = newAudio[start:end]
newAudio.export('/home/madhu/workspace/audio/res.mp3', format="mp3")

s1 = AudioSegment.from_mp3("/home/madhu/workspace/audio/one.mp3")
s2 = AudioSegment.from_mp3("/home/madhu/workspace/audio/one.mp3")

combined = s1 + s2
combined.export("/home/madhu/workspace/audio/res.mp3", format="mp3")

s1 = AudioSegment.from_mp3("/home/madhu/workspace/audio/one.mp3")
combined = s1
for i in range(1, 108):
    combined = combined + s1

combined.export("/home/madhu/workspace/audio/res.mp3", format="mp3")

s1 = AudioSegment.from_mp3("/home/madhu/workspace/audio/res.mp3")
s1 = s1.set_frame_rate(43200)
s1.export("/home/madhu/workspace/audio/res1.mp3", format="mp3")
