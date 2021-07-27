# numer ディレクトリ内のモジュールをインポートするためのスクリプトファイル。

import os                   # OS に関連するモジュール
import sys                  # システムに関連するモジュール

# 自作モジュールの場所(PATH)を追加
s = os.getcwd()             # このファイルがある場所(カレントディレクトリ)を取得
print(s)
if s not in sys.path:
    sys.path.append(s)
del s

import numer.numermod
import numer.submodule.sub   # サブモジュールをインポート
#import numer                 # ディレクトリ名だけの記述でもインポート可能
#import numer.submodule       # ディレクトリ名だけの記述でもインポート可能
