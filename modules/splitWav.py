# Created by RitsukiShuto on 2023/06/16.
# 音声ファイルの無音区間除去を行う
#
from pydub import AudioSegment
from pydub.silence import split_on_silence

class splitWav:
    def __init__(self, snd):
        self.snd = snd

        # ファイルの命名規則
        self.saveDir = '/out/'
        self.outBaseName = 'ANG'

    # 渡された音声ファイルを無音区間で分割する
    def removeSilence(self):        
        org_ms = len(self.snd)

        # 無音区間の検出
        chunks = split_on_silence(self.snd, min_silence_len = 100, silence_thresh = -55, keep_silence = 100)

        removed_sound = AudioSegment.empty()

        for chunk in chunks:
            removed_sound += chunk

        # ファイルの保存
        self.saveWav(removed_sound, org_ms)

    def saveWav(self, snd, org_ms):
        # ファイル名の設定
        outFileName = self.outBaseName + '_' + str(self.snd)

        # ファイルの保存
        snd.export(self.saveDir + outFileName, format = 'mp3')

        # DEBUG
        print('removed: {:.2f} [min]'.format(org_ms/60/1000))
