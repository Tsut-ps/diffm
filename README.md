![image](https://github.com/Tsut-ps/diffm/assets/73014392/28bff96e-4cbd-484f-9f8a-cba82f9f0a9d)# diffm
動画差分を表示 & グラフ化してくれるやつ。
リアルタイム計算。
30フレームごとに描画するようになっている。

![image](https://github.com/Tsut-ps/diffm/assets/73014392/fa76e2a9-0a8b-4a21-bc30-4b56b245f2d5)

## どうして作ったの？
- AviUtlで差分比較するのが面倒だった
- グラフ化して定量的に差分比較したかった

## ToDo
演算がちょっと重めなので、軽量化したい。

## もっと詳しく
[PythonとOpenCVで画像を比較して保存する](https://scrapbox.io/Tsut-ps/Python%E3%81%A8OpenCV%E3%81%A7%E7%94%BB%E5%83%8F%E3%82%92%E6%AF%94%E8%BC%83%E3%81%97%E3%81%A6%E4%BF%9D%E5%AD%98%E3%81%99%E3%82%8B)

## 確認動作環境
- Windows 11
- VSCode 1.83.1
- Python 3.11.6

# 必要なライブラリ
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

# 入力
```
比較動画A: <ここにパスを入力> 
比較動画B: <ここにパスを入力>
```

# 注意事項
環境によっては動作しない可能性あり。