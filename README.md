# Jikken5

attentions.py はコピペした。encoderとdecoder、MultiHeadAttention、FFN クラスがある。

commons.py　はコピペした。ニューラルネットワークの初期化、パディング、シーケンス生成、およびその他の関連ユーティリティ関数がある。

inference.ipymb はよくわかんないけど一応ファイルだけ作った。多分自分たちで作る必要あり

losses.py　はコピペした。生成モデル（Generator）および識別モデル（Discriminator）の損失関数を計算するための関数がある。

models.py 音声合成モデル（SynthesizerTrn）を実装している。コピペしちゃったけど編集する必要あり。

modules.py はコピペした。pytorchをつかったフロータイプの生成モデル。

transform.pyはコピペした。PyTorchを使用して確率的な逆変換を実行するためのコード？どこで使われているかはまだ確認していない。

utils data_utils はコピペ


train.py は参考に自分たちで書く必要あり
configにtraining_filesとかはいってるからそれを編集する必要あり

mel_processing.pyは人によってコードが違うから考える必要あり。