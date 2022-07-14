import gtts

from playsound import playsound

with open("text-files/text.txt", "r") as file:

    for line in file:

        text = gtts.gTTS(line, lang="pt-br")

        text.save("audio-files/textspeech.mp3")

        playsound("audio-files/textspeech.mp3")