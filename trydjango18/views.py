from django.shortcuts import render
import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
from trydjango18.recorder import Recorder


def about(request):
	return render(request, "about.html", {})


def record(request):
    recorder = Recorder('speech.wav')
    recorder.record_to_file()
    print("Recording started...")
    return render(request, "about.html", {})


def submit(request):
    info=request.POST['info']
    print("Submit worked")
    speech_to_text = SpeechToTextV1(
		username='2c7c1607-84f2-4cc1-88df-7adcd4adb3f9',
		password='QDGAcW5N7JLS',
		x_watson_learning_opt_out=False)

    print(json.dumps(speech_to_text.models(), indent=2))

    print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))

    text = transcribe_audio('../speech.wav')
    print(text)
    return render(request, "about.html", {"text":text})

    # with open(join(dirname(__file__),'../speech.wav'),'rb') as audio_file:print(json.dumps(speech_to_text.recognize(audio_file,content_type='audio/wav',timestamps=True,word_confidence=True), indent=2))


def transcribe_audio(path_to_audio_file):
    speech_to_text = SpeechToTextV1(
		username='2c7c1607-84f2-4cc1-88df-7adcd4adb3f9',
		password='QDGAcW5N7JLS',
		x_watson_learning_opt_out=False)
    with open(join(dirname(__file__), path_to_audio_file), "rb") as audio_file: return speech_to_text.recognize(audio_file, content_type="audio/wav",word_confidence=True)