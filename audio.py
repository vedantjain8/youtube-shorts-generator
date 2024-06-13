import random
import globVar
from elevenlabs import save
from elevenlabs.client import ElevenLabs
from os import path


def generateAudio(inputText):
    '''This function generates the audio clip using the ElevenLabs API. 

    Args:
        inputText (str): The text to be converted to speech.
    
    '''
    # DONT USE THIS COMMENTED CODE OR THERE IS A CHANCE OF GETTING YOUR ELEVENLABS API ACCOUNT SUSPENDED
    
    # tokenIndex = 0
    # while len(globVar.elevenapi_key) > tokenIndex:
    #     currentApiKey = globVar.elevenapi_key[tokenIndex]
    #     client = ElevenLabs(api_key=currentApiKey)
    #     tokenLeft = client.user.get_subscription().character_limit - \
    #         client.user.get_subscription().character_count
    #     print(
    #         f"{bcolors.OKGREEN}{bcolors.BOLD}API key in use:{bcolors.ENDC} {currentApiKey} : Token Left: {tokenLeft}")
    #     if (tokenLeft >= len(inputText)):
    #         generateAuidoClip(inputText=inputText, apiKey=currentApiKey)
    #         break
    #     else:
    #         if (tokenIndex == len(globVar.elevenapi_key) - 1):
    #             print(
    #                 f"{bcolors.FAIL}{bcolors.BOLD}All API keys have been exhausted, please try again later{bcolors.ENDC}")
    #             break
    #         tokenIndex += 1
    generateAuidoClip(inputText=inputText, apiKey=globVar.elevenapi_key)



def generateAuidoClip(inputText, apiKey):
    '''
    This function generates the audio clip using the ElevenLabs API. And save it to the audio file.
    
    Args:
        inputText (str): The text to be converted to speech.
        apiKey (str): The API key to be used for the conversion.
    '''
    client = ElevenLabs(
        api_key=apiKey,
    )

    voice = random.choice(globVar.voice_artists)
    print(f"{globVar.bcolors.OKGREEN}{globVar.bcolors.BOLD}Voice artist in use:{globVar.bcolors.ENDC} {voice} ")
    audio = client.generate(
        text=inputText,
        voice=voice,
        model="eleven_multilingual_v2"
    )

    save(audio, path.join('output', globVar.folderName, 'audio', "audio.mp3"))
