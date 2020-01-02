# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import subprocess
from mycroft.util import play_wav, is_speaking
from mycroft.tts import TTS, TTSValidator


class SpdSayPico(TTS):
    def __init__(self, lang, config):
        super(SpdSayPico, self).__init__(lang, config, SpdSayValidator(self))

    def execute(self, sentence, ident=None, listen=False):
        self.begin_audio()
        subprocess.call(['/usr/bin/pico2wave','-l=fr-FR', '-w=/tmp/tmp_say.wav', '"'+sentence+'"'])
        subprocess.call(["aplay", "/tmp/tmp_say.wav"])
        self.end_audio(listen)


class SpdSayValidator(TTSValidator):
    def __init__(self, tts):
        super(SpdSayValidator, self).__init__(tts)

    def validate_lang(self):
        # TODO
        pass

    def validate_connection(self):
        try:
            subprocess.call(['spd-say', '--version'])
        except Exception:
            raise Exception(
                'SpdSay is not installed. Run: sudo apt-get install '
                'speech-dispatcher')

    def get_tts_class(self):
        return SpdSayPico
