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
        self.files = self.readWavFile()

        # ファイルの命名規則
        self.save_dir = 'out/'

    # 渡された音声ファイルを無音区間で分割する
    def removeSilence(self):
        for file in (self.files):
            print('processing: ' + file + '...')

            # 音声ファイルの読み込み
            basename = os.path.splitext(os.path.basename(file))[0]
            sound = AudioSegment.from_mp3(file)

            # 無音区間の検出
            chunks = split_on_silence(
                                    sound,
                                    min_silence_len = 500,      # ms以上の無音区間を検出
                                    silence_thresh = -40,       # -40dBFS以下の無音区間を検出
                                    keep_silence = 100          # ms以上の無音区間を残す
                                    )

            for i, chunk in enumerate(chunks):
                # ファイルの保存
                self.saveWav(chunk, basename, i)

    def saveWav(self, chunk, basename, i):

        # 400ms以上の音声ファイルのみ保存する
        if len(chunk) > 400:
            # ファイル名の設定
            out_file_name =  basename + '_' + str(i+1) + '.mp3'

            # ファイルの保存
            chunk.export(self.save_dir + out_file_name, format = 'mp3')

            # DEBUG
            print('saved: ' + out_file_name + ' (' + str(len(chunk) / 1000) + 's)')

    def readWavFile(self):
        try:
            # ファイルの読み込み
            return glob.glob(os.path.join("sndSource", "*.mp3"))

        except:
            print('Error: ファイルの読み込みに失敗しました。')
            sys.exit()