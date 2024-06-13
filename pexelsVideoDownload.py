import requests
import globVar
from os import path
import uuid


def SearchVideo(keywords: list, totalDuration=60.00):
    '''
    This function searches for videos on Pexels based on the keywords provided.

    Args:
        keywords (list): The list of keywords to search for.
        totalDuration (float): The total duration of the video. Default is 60.00.
    '''
    totalDuration = totalDuration
    videoIndex = 0
    videoOrderNumber = 0
    while totalDuration > 0:
        videoIndex += 1
        for keyword in keywords:
            videoOrderNumber += 1
            print(
                f"{globVar.bcolors.OKBLUE} {globVar.bcolors.BOLD}Searching for keyword: {keyword}{globVar.bcolors.ENDC}")
            r = requests.get(f"https://api.pexels.com/videos/search?query={keyword}&per_page=1&page={videoIndex}",
                             headers={"Authorization": globVar.pexels_api_key})
            jsondata = r.json()
            if (totalDuration <= 0):
                break
            try:
                video = jsondata['videos'][0]

                for i in (video['video_files']):
                    if i['quality'] == 'hd':
                        if i['width'] >= 1920:
                            if i['height'] >= 1080:
                                nestedVideo_link = i['link']
                                nestedVideoId = i['id']
                                videoDuration = video['duration']
                                if videoDuration <= 15:
                                    totalDuration -= videoDuration
                                else:
                                    totalDuration -= 15
                                print(totalDuration)
                                writeVideoToFile(
                                    nestedVideo_link=nestedVideo_link, video_id=nestedVideoId, videoOrderNumber=videoOrderNumber)
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
            except Exception as e:
                print(
                    f"{globVar.bcolors.FAIL}{globVar.bcolors.BOLD}Error for keyword [{keyword}]: {e}{globVar.bcolors.ENDC}")


def writeVideoToFile(nestedVideo_link, video_id, videoOrderNumber):
    '''
    This function download and writes the video to a file.

    Args:
        nestedVideo_link (str): The link to the video.
        video_id (str): The id of the video.
        videoOrderNumber (int): The order number of the video.
    '''
    r = requests.get(nestedVideo_link)
    filePath = path.join('output', globVar.folderName,
                         'video', f"{videoOrderNumber}-{str(video_id)}-{str(uuid.uuid4())}.mp4")
    print(f"{globVar.bcolors.OKBLUE} {globVar.bcolors.BOLD}Writing to video file: {filePath}{globVar.bcolors.ENDC}")
    with open(filePath, 'wb') as file:
        file.write(r.content)


# if __name__ == "__main__":
#     SearchVideo(['astronaut'])
