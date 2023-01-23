
#Import necessary libraries
import pandas as pd
import numpy as np
import cv2
import random
from pedalboard import Chorus, Reverb, Gain, LadderFilter,Phaser, Delay, PitchShift, Distortion
from pedalboard.io import AudioFile
from PIL import Image
from scipy.io import wavfile
import librosa
import glob