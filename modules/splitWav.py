# Created by RitsukiShuto on 2023/06/16.
# 音声ファイルの無音区間除去を行う
#
import glob
from pydub import AudioSegment
from pydub.silence import split_on_silence
from pathlib import Path
import sys
import os

class SplitWav:
    def __init__(self):
        self.files = read_wav_file()

        # ファイルの命名規則
        self.save_dir = 'out\\'
        self.out_base_name = 'ANG'

    # 渡された音声ファイルを無音区間で分割する
    def remove_silence(self):
        print(self.files)

        for file in (self.files):
            # 音声ファイルの読み込み
            sound = AudioSegment.from_mp3(file)
            org_ms = len(sound)

            # 無音区間の検出
            chunks = split_on_silence(sound, min_silence_len = 100, silence_thresh = -55, keep_silence = 100)
            removed_sound = AudioSegment.empty()

            for chunk in chunks:
                removed_sound += chunk

            # ファイルの保存
            self.save_wav(removed_sound, org_ms)

    def save_wav(self, snd, org_ms):
        # ファイル名の設定
        out_file_name = self.out_base_name + '_' + str(snd)

        # ファイルの保存
        snd.export(self.save_dir + out_file_name, format = 'mp3')

        # DEBUG
        print('removed: {:.2f} [min]'.format(org_ms/60/1000))

def read_wav_file():
    try:
        return glob.glob(os.path.join("sndSource", "*.mp3"))

    except:
        print('Error: ファイルの読み込みに失敗しました。')
        sys.exit()