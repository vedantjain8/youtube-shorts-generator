import os
from random import choice
from moviepy.video.fx.all import crop
from moviepy.config import change_settings
from moviepy.editor import TextClip, VideoFileClip, CompositeVideoClip, AudioFileClip, concatenate_videoclips, CompositeAudioClip
from moviepy.video.tools.subtitles import SubtitlesClip
import globVar


def audioLength(folderName: str):
    '''
    This function returns the length of the audio file in seconds with a end buffer of 3 seoconds
    '''
    return (AudioFileClip(f'output/{folderName}/audio/audio.mp3').duration + 3.00)


def generate_video(folderName, threads: int, subtitles_position="center,center", text_color="white") -> str:
    """
    This function creates the final video, with subtitles and audio.

    Args:
        folderName (str): The name of the folder where the video files are stored.
        threads (int): The number of threads to use for rendering the video.
        subtitles_position (str): The position of the subtitles on the video. Default is "center,center".
        text_color (str): The color of the subtitles. Default is "white".

    Returns:
        str: The path to the final video.
    """
    change_settings(
        # {"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})
        {"IMAGEMAGICK_BINARY": globVar.magickPath})

    # Split the subtitles position into horizontal and vertical
    horizontal_subtitles_position, vertical_subtitles_position = subtitles_position.split(
        ",")

    # Load the audio and video
    audio = AudioFileClip(
        os.path.join('output', folderName, 'audio', 'audio.mp3'))
    duration = audio.duration + 3.00

    combinedClip = []
    files = sorted(os.listdir(os.path.join('output', folderName, 'video')))
    for file in files:
        if file.endswith(".mp4"):
            videoClip = VideoFileClip(
                os.path.join('output', folderName, 'video', file))
            combinedClip.append(videoClip.subclip(
                0, min(15.00, videoClip.duration)))
    clip = concatenate_videoclips(combinedClip)

    # bg music calculation
    bg_music = AudioFileClip(
        os.path.join('assets', 'music', choice(os.listdir(f"assets/music/"))))
    available_bg_music = min(60, duration)
    start_time = choice(range(int(bg_music.duration - available_bg_music)))

    bg_music = bg_music.volumex(0.2)
    bg_music = bg_music.subclip(start_time, start_time + available_bg_music)

    # crop the video
    w, h = clip.size

    # Calculate the width and height of the cropped region based on the aspect ratio 9:16
    crop_width = h * 9 / 16
    crop_height = h

    # Calculate the coordinates for the crop region
    x1 = (w - crop_width) / 2
    x2 = x1 + crop_width
    y1 = 0
    y2 = crop_height

    # limit the video to the length of the audio clip
    # clip = clip.subclip((0, 0), (0, ceil(audio.duration)))
    cropped_video = crop(clip, x1=x1, y1=y1, x2=x2, y2=y2)

    # Set the fps to 24
    cropped_video = cropped_video.set_fps(24)

    # Limit the length of the video
    # cropped_video = cropped_video.subclip(0, output_duration)

    # Define a function to generate TextClip for each subtitle
    def subtitle_generator(txt):

        return TextClip(txt, font=os.path.join('assets', 'fonts', choice(os.listdir(f"assets/fonts/"))), fontsize=45, color=text_color, method='caption', align='center',
                        bg_color="transparent")
        # stroke_color="black", stroke_width=10,

    # Load and parse the subtitles
    subtitles = SubtitlesClip(
        os.path.join('output', folderName, 'output', 'subtitle.srt'), subtitle_generator)

    # Composite the video with subtitles
    result = CompositeVideoClip([
        # Use cropped video with limited duration
        cropped_video.set_duration(duration),
        subtitles.set_pos((horizontal_subtitles_position,
                          vertical_subtitles_position))
    ])

    # Add the audio
    finalAudio = CompositeAudioClip([audio, bg_music])
    result = result.set_audio(finalAudio)

    # Write the final video
    result.write_videofile(
        os.path.join('output', folderName, 'output', 'play.mp4'), threads=threads or 2, codec="libx264")

    return os.path.join('output', folderName, 'output', 'play.mp4')

# if __name__ == "__main__":
    # generate_video(folderName='4bcf1c99-e17d-4075-ae19-b1fdcefad578', threads=2,
    #            subtitles_position="center,center", text_color="white")
