from wave import open
from math import floor
from struct import Struct

frame_rate = 11025

def encode(x):
    i = int(16384 * x)
    return Struct("h").pack(i)


def play(sampler,name='song.wav',seconds=2):
    out = open(name,"wb")
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(frame_rate)
    t = 0
    
    while t < seconds * frame_rate:
        sample = sampler(t)
        out.writeframes(encode(sample))
        t = t+1
    out.close()
    

def tri(frequency, amplitude=0.3):
    period = frame_rate // frequency
    def sampler(t):
        saw_wave = t/period - floor(t/period+0.5)
        tri_wave = 2 * abs(2 * saw_wave) -1
        return amplitude * tri_wave
    return sampler
    
c_freq = 261.63