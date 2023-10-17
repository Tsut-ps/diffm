# diffm
動画差分を表示 & グラフ化してくれるやつ。  
リアルタイム計算。  
30フレームごとに描画するようになっている（書き換えれば調整可能）。  

![image](https://github.com/Tsut-ps/diffm/assets/73014392/9d305d27-b9a9-46fd-a404-c967f4a8ddfd)

## どうして作ったの？
- AviUtlで差分比較するのが面倒だった
- グラフ化して定量的に差分比較したかった
- ライブラリを使ってみたかった（あまり使ったことがないので）

## もっと詳しく（経緯）
[PythonとOpenCVで画像を比較して保存する](https://scrapbox.io/Tsut-ps/Python%E3%81%A8OpenCV%E3%81%A7%E7%94%BB%E5%83%8F%E3%82%92%E6%AF%94%E8%BC%83%E3%81%97%E3%81%A6%E4%BF%9D%E5%AD%98%E3%81%99%E3%82%8B)

### ToDo
演算がちょっと重めなので、軽量化したい。

## 確認動作環境
- Windows 11
- VSCode 1.83.1
- Python 3.11.6 (Microsoft Store)

## 必要なライブラリ
- OpenCV  
  ```
  pip install opencv-python
  ```
- NumPy
  ```
  pip install numpy
  ```
- Matplotlib
  ```
  pip install matplotlib
  ```

## 実行
1. どこか好きなところに diffm.py を保存
1. 実行できるもので開く
1. パスを入力
   ```
   比較動画A: <ここに1つ目の動画のパスを入力>
   比較動画B: <ここに2つ目の動画のパスを入力>
   ```

## 終了
「diffm」ウィンドウをバツで閉じると、他のウィンドウも閉じる。
