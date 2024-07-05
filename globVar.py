import uuid


def generateNewFolderName():
    return str(uuid.uuid4())


folderName = str(uuid.uuid4())
# elevenapi_key = 'ELEVENLABS_API_KEY_HERE'

pexels_api_key = "PEXELS_API_KEY_HERE"

voice_artists = ["en-US-BrianNeural", "en-US-AndrewNeural"]
# Select one or more voice artists from the elevenlabs and enter the name as you have save it with on elevenlabs

magickPath = r"assets/magick"


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
