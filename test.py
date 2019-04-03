import midi

pattern = midi.Pattern()

track = midi.Track()

pattern.append(track)

on = midi.NoteOnEvent(tick=0,velocity=50,pitch=midi.G_3)

track.append(on)

off = midi.NoteOffEvent(tick=200,pitch=midi.G_3)

track.append(off)

eot = midi.EndOfTrackEvent(tick=1)
track.append(eot)

midi.write_midifile('example.mid',pattern)