# Created by RitsukiShuto on 2023/06/16.
# 音声ファイルのノイズ除去、無音区間の除去を行う
#
import glob
import os
import sys

import modules.splitWav as splitWav

def readWavFile():
    try:
        # ファイルのパスを取得する
        snd = glob.glob('/sndSource/*.mp3')
        print(snd)

    except:
        print('Error: ファイルの読み込みに失敗しました。')
        sys.exit()

def main():
    # 音声ファイルを読み込む
    # 複数の音声ファイルを読み込む場合はglobを使用する
    snd = readWavFile()

    # 加工する音声ファイルのインスタンスを作成
    angeVoice =  splitWav.splitWav(snd)

    # 無音区間の除去を行う
    angeVoice.removeSilence()

if __name__ == '__main__':
    main()