# Created by RitsukiShuto on 2023/06/16.
# 音声ファイルのノイズ除去、無音区間の除去を行う
#
import glob
import sys

import modules.splitWav as splitWav

def main():
    # 音声ファイルを読み込む
    # 複数の音声ファイルを読み込む場合はglobを使用する
    angeVoice = splitWav.splitWav()

    # 無音区間の除去を行う
    angeVoice.removeSilence()

if __name__ == '__main__':
    main()