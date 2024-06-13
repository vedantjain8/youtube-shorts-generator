# import whisper
import stable_whisper
from datetime import timedelta
import globVar
import os


# def transcribeAudio(path):
#     '''
#     This function transcribes the audio file to a subtitle file.

#     Args:
#         path (str): The path to the audio file.
#     '''
#     model = whisper.load_model("small", download_root="./whisper_models/")
#     transcribe = model.transcribe(
#         audio=path, fp16=False)

#     segments = transcribe['segments']

#     for segment in segments:
#         startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
#         endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
#         text = segment['text']
#         segmentId = segment['id']+1
#         segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"

#         with open(os.path.join('output', globVar.folderName, 'output', 'subtitle.srt'), 'a', encoding='utf-8') as srtFile:
#             srtFile.write(segment)


def stableTranscribe(path):
    '''
    This function transcribes the audio file to a subtitle file.

    Args:
        path (str): The path to the audio file.
    '''
    model = stable_whisper.load_model(
        'small', download_root="./whisper_models/")
    transcribe = model.transcribe(
        audio=path, vad=True, word_timestamps=True, fp16=False)
    transcribe.to_srt_vtt(segment_level=False, word_level=True, filepath=os.path.join('output', globVar.folderName, 'output', 'subtitle.srt'))  # SRT word level
    transcribe.to_srt_vtt(segment_level=True, word_level=False, filepath=os.path.join('output', globVar.folderName, 'output', 'YT_subtitle.srt'))  # SRT segment level


# if __name__ == "__main__":
#     stableTranscribe(
#         f"output/6c18f9f4-47f7-4846-979c-f6004b412906/audio/audio.mp3")
