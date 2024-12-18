import pyaudio
import numpy as np

class Note:
    def __init__(self, frequency, length, total_length):
        self.frequency = frequency
        self.length = length
        self.p = pyaudio.PyAudio()
        self.total_length = total_length

        self.t = np.linspace(0, self.length, int(44100 * self.length), False)
        self.wave = (0.5 * np.sin(2 * np.pi * self.frequency * self.t)).astype(np.float32)
        self.stream = self.p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=44100,
                        output=True
        )

    def play(self):
        self.stream.write(self.wave.tobytes())