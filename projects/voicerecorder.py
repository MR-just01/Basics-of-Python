import sounddevice
import scipy

from scipy.io.wavfile import write

def voicerec(seconds , file):
    print("Recording Started...")
    recording = sounddevice.rec((seconds * 44100) , samplerate = 44100 , channel = 2)
    sounddevice.wait()
    write(file , 44100,recording)
    print("recording is finish")

voicerec(10 , "test.wav")