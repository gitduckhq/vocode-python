from typing import Optional
from vocode.streaming.models.audio_encoding import AudioEncoding
from vocode.streaming.models.model import BaseModel
from enum import Enum


class InputAudioConfig(BaseModel):
    sampling_rate: int
    audio_encoding: AudioEncoding
    chunk_size: int
    downsampling: Optional[int] = None

class AudioVoice(str, Enum):
    sam = "sam"
    marta = "marta"
    karim = "karim"
    laura = "laura"

class OutputAudioConfig(BaseModel):
    sampling_rate: int
    audio_encoding: AudioEncoding
    voice: Optional[AudioVoice]
