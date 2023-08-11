from typing import Optional
from vocode.streaming.models.audio_encoding import AudioEncoding
from vocode.streaming.models.model import BaseModel
from enum import Enum


class InputAudioConfig(BaseModel):
    sampling_rate: int
    audio_encoding: AudioEncoding
    chunk_size: int
    downsampling: Optional[int] = None
    language_code: Optional[str] = None

class OutputAudioConfig(BaseModel):
    sampling_rate: int
    audio_encoding: AudioEncoding
    voice: Optional[str]
    provider: Optional[str]
