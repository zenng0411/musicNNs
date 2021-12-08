import itertools
from midi_to_matrix import upperBound, lowerBound

def startMusc():
    def noteMusc(note):
        position = note
        part_position = [position]
        pitch_class = (note + lowerBound) % 12
        part_pitchclass = [int(i == pitch_class) for i in range(12)]

        return part_position + part_pitchclass + [0]*66 + [1]
    return [noteMusc(note) for note in range(upperBound - lowerBound)]

def get0rDefault(l, i, d):
    try:
        return l[i]
    except IndexError:
        return d

def buildContext(state):
    context = [0]*12
    for note, notestate in enumerate(state):
        if notestate[0] == 1:
            pitch_class = (note + lowerBound)%12
            context(pitch_class) += 1
        return context

def buildBeat(time):
    return [2*x - 1 for x in [tiem%2, (time//2)%2, (time//4)%2, (time//8)%2]]

def noteInputForm(note, state, context, beat):
    position = note
    part_position = [position]
    pitch_class = (note + lowerBound)%12
    part_pitchclass = [int(i == pitch_class) for i in range(12)]
    part_prev_vicinity = list(itertools.chain.from_iterable((getOrDefault(state, note+i, [0,0]) for i in range(-12, 13))))
    part_context = context[pitch_class:] + context[:pitchclass]

    return part_position + part_pitchclass + part_prev_vicinity + part_context + beat + [0]

def noteStateSingletoInput(state, time):
    beat = buildBeat(time)
    context = buildContext(state)
    return [noteInputform(note, state, context, beat) for note in range(len(state))]

def noteStateMatrixToInputForm(statematrix):
    inputform = [noteStateSingletoInput(state,time) for time, state in enumerate(stateMatrix)]
    return inputform

