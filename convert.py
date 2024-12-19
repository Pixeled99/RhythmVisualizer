import mido
from mido.messages.messages import Message
from note import Note

def midi_to_frequency(note : int):
    return 440.0 * (2 ** ((note - 69) / 12.0))

def convert(path : str, track : int) -> list[Note]:
    midi_file = mido.MidiFile(path)

    track = midi_file.tracks[track]
    notes : [Note] = []
    current_notes = {}
    time = 0
    offset = False

    for msg in track:
        msg : Message
        time += msg.time
        if hasattr(msg, "velocity"):
            if msg.type == "note_off" or msg.velocity == 0:
                notes.append(Note(midi_to_frequency(msg.note), current_notes[msg.note]/1000, time/1000))
                del current_notes[msg.note]
            elif msg.type == "note_on":
                if not offset:
                    offset = True
                    time = 0
                current_notes[msg.note] = time

    return notes