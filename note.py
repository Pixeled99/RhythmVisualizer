import pyaudio
import numpy as np
import math

def freq_to_note(freq):
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    note_number = 12 * math.log2(freq / 440) + 49
    note_number = round(note_number)

    note = (note_number - 1) % len(notes)
    note = notes[note]

    octave = (note_number + 8) // len(notes)

    return f"{note}{octave}"

class Note:
    def __init__(self, frequency, start, end):
        self.frequency = frequency
        self.start = start
        self.end = end
        self.length = self.end-self.start
        self.total_length = None
        self.p = pyaudio.PyAudio()

        self.t = np.linspace(0, self.length, int(44100 * self.length), False)
        self.wave = (0.5 * np.sin(2 * np.pi * self.frequency * self.t)).astype(np.float32)
        self.stream = self.p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=44100,
                        output=True
        )

    def play(self):
        self.stream.write(self.wave.tobytes())

    def __str__(self):
        return f"{freq_to_note(self.frequency)} starts at {self.start}, ends at {self.end}"