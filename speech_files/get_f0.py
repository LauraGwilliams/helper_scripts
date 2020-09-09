# leg5@nyu.edu
# get average f0 for a wav file

# modules
import parselmouth
import numpy as np

# define function
def get_mean_f0(file):
    '''
    file:   filepath of .wav file of interest
    '''

    # load file into parselmouth
    snd = parselmouth.Sound(file)

    # extract pitch / f0
    pitch = snd.to_pitch()
    pitch_values = pitch.selected_array['frequency']
    pitch_values[pitch_values==0] = np.nan  # for easy ignoring

    return np.nanmean(pitch_values)

# useage
file = 'path_to_speech_file.wav'
avg_f0 = get_mean_f0(file)
