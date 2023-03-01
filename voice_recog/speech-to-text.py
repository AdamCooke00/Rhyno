import os
import pyaudio
import wave
import pygame

def test_audio(speech_file):
    pygame.mixer.init()
    pygame.mixer.music.load(speech_file)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

def transcribe_file(speech_file):
    """Transcribe the given audio file asynchronously."""
    from google.cloud import speech
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = #INSERT YOUR GOOGLE CLOUD CREDENTIALS HERE

    client = speech.SpeechClient()

    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    """
     Note that transcription is limited to a 60 seconds audio file.
     Use a GCS file for audio longer than 1 minute.
    """
    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="en-US",
    )


    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=90)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print("Transcript: {}".format(result.alternatives[0].transcript))
        print("Confidence: {}".format(result.alternatives[0].confidence))

    device, command = result.alternatives[0].transcript.split()[0], result.alternatives[0].transcript.split()[1]
    brightness = 50

    if device == "light":
        device = "light-" + command
        command = result.alternatives[0].transcript.split()[2]
    if command == "brightness":
        command = "ON"
        brightness = result.alternatives[0].transcript.split()[3]

    return (device, command, brightness)


def record_audio(file_name = "output.wav"):
    # set the parameters for the audio recording
    CHUNK = 1024 # number of frames per buffer
    FORMAT = pyaudio.paInt16 # sample format
    CHANNELS = 1 # mono
    RATE = 44100 # sample rate (Hz)
    RECORD_SECONDS = 3 # duration of recording

    audio = pyaudio.PyAudio() # create an instance of PyAudio
    # open the microphone stream
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    # start recording
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    # stop recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # write the audio data to a WAV file
    
    with wave.open(file_name, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b"".join(frames))



record_audio()
device, command, brightness = transcribe_file("output.wav")

command = command.upper()
if device == "light-one":
    cmdStr = "mosquitto_pub -t \'zigbee2mqtt/light1/set\' -m \'{ \"state\": \"%s\",\"brightness\":%s}\'" % (command, brightness)
elif device == "light-two" or device == "light-to":
    cmdStr = "mosquitto_pub -t \'zigbee2mqtt/light2/set\' -m \'{ \"state\": \"%s\",\"brightness\":%s}\'" % (command, brightness)
elif device == "plug":
    cmdStr = "mosquitto_pub -t \'zigbee2mqtt/plug1/set\' -m \'{ \"state\": \"%s\",\"brightness\":%s}\'" % (command, brightness)


# os.system(cmdStr)
# print(cmdStr)
print(device, command, brightness)
# test_audio("output.wav")
