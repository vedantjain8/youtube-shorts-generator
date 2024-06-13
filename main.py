import os
import globVar
from getQuoteListFromAI import getQuoteListFromAI, cleanTextOut
from audio import generateAudio
from pexelsVideoDownload import SearchVideo
from subtitle import stableTranscribe
from generateVideo import generate_video, audioLength
from hashFun import check_hash, write_hash

# https://github.com/vedantjain8/youtube-shorts-generator

def createNewFolder():

    # create output directory
    globVar.folderName = globVar.generateNewFolderName()
    
    os.makedirs("output", exist_ok=True)
    os.makedirs("assets", exist_ok=True)
    os.makedirs("assets/music", exist_ok=True)
    os.makedirs("assets/fonts", exist_ok=True)

    print(f"Folder name: {globVar.folderName}")
    os.makedirs(os.path.join('output', globVar.folderName))
    os.makedirs(os.path.join('output', globVar.folderName, 'video'))
    os.makedirs(os.path.join('output', globVar.folderName, 'audio'))
    os.makedirs(os.path.join('output', globVar.folderName, 'output'))


if __name__ == "__main__":
    # Generate text

    while True:
        topicPreference = input("Enter your prompt: ")

        if (topicPreference == "exit"):
            break
        topic = None if topicPreference == "" else topicPreference

        print(globVar.bcolors.HEADER + globVar.bcolors.BOLD +
              "Generating text..." + globVar.bcolors.ENDC)

        fact, keyword = cleanTextOut(getQuoteListFromAI(
            topic=topic))

        if (check_hash(fact)):
            continue

        print(f"{globVar.bcolors.OKGREEN}{globVar.bcolors.BOLD}Fact: {globVar.bcolors.ENDC}{fact}\n\n{globVar.bcolors.OKGREEN}{globVar.bcolors.BOLD}Keyword:{globVar.bcolors.ENDC} {keyword}")

        response = input("Continue? (y/n): ").lower()
        if response == "n":
            continue
        elif response == "y":
            createNewFolder()

            with open(f"output/{globVar.folderName}/GPToutput.txt", 'w') as f:
                f.write("output: " + fact + "\n" +
                        "keywords: " + ", ".join(keyword))

            # generate audio clip
            print(globVar.bcolors.HEADER + globVar.bcolors.BOLD +
                  "Generating Audio..." + globVar.bcolors.ENDC)
            generateAudio(fact)

            # get audio length
            # pre appended 3 seconds to the audio length
            audio_length = audioLength(globVar.folderName)

            # download video
            print(globVar.bcolors.HEADER + globVar.bcolors.BOLD +
                  "Downloading Video..." + globVar.bcolors.ENDC)
            SearchVideo(keywords=keyword, totalDuration=audio_length)

            # Transcribing Audio
            print(globVar.bcolors.HEADER + globVar.bcolors.BOLD +
                  "Transcribing Audio..." + globVar.bcolors.ENDC)
            stableTranscribe(f"output/{globVar.folderName}/audio/audio.mp3")

            # write hash to file
            write_hash(fact)

            # Generate Video
            print(globVar.bcolors.HEADER + globVar.bcolors.BOLD +
                  "Generating Video..." + globVar.bcolors.ENDC)
            generate_video(folderName=globVar.folderName, threads=2, )

            # generate a appropriate title
            print(globVar.bcolors.HEADER + globVar.bcolors.BOLD +
                  "Generating Title..." + globVar.bcolors.ENDC)
        else:
            break