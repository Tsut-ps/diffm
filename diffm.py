import cv2
import numpy as np
import time
import matplotlib.pyplot as plt

fps = 30

print("比較動画A: ", end="")
mov_A = input()
print("比較動画B: ", end="")
mov_B = input()

# 動画の読み込み
video1 = cv2.VideoCapture(mov_A)
video2 = cv2.VideoCapture(mov_B)
brightness = []

# 開始秒数
startTime = time.time()

i = 1
while (True):
    # 動画の1フレームを取得
    ret1, frame1 = video1.read()
    ret2, frame2 = video2.read()

    # どちらかのフレームが取得できない場合はループを抜ける
    if not ret1 or not ret2:
        break

    # フレームの差分で画像を作成
    diff = cv2.absdiff(frame1, frame2)
    # BGR(RGB)からHSVに変換
    diff_hsv = cv2.cvtColor(diff, cv2.COLOR_BGR2HSV)
    # HSVのV(明度)だけ抽出
    diff_v = diff_hsv[:, :, 2]
    # 平均値を計算
    diff_v_mean = np.mean(diff_v)
    
    # 配列に追加
    brightness.append(diff_v_mean)
    
    # 30フレームごとにグラフ描画
    if (i % fps == 0):
        plt.cla()
        plt.ylim(0, 255)
        plt.plot(brightness)
        plt.pause(0.0001)
        cv2.imshow('diffm', diff)
        cv2.waitKey(1)
    
    i += 1

# 実行にどれくらいかかったか
print("time: ", (time.time() - startTime), "[sec]")
cv2.waitKey(0)

# メモリ解放
video1.release()
video2.release()
