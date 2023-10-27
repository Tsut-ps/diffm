import cv2
import sys
import numpy as np
import time
import matplotlib.pyplot as plt

# 引数を取得
args = sys.argv

# 変数の初期化/未定義エラーを防ぐ
mov_A = ""
mov_B = ""
interval = 0

# 引数があるときに動画を指定
if (len(args) > 2):
    # 第1引数で 動画A 指定
    mov_A = args[1]
    # 第2引数で 動画B 指定
    mov_B = args[2]
    # 第3引数でinterval指定
    if (len(args) > 3):
        interval = int(args[3])
    # 引数指定が多すぎるときはエラーを出す
    if (len(args) > 4):
        print("引数が多すぎます")
        exit()

# 動画Aの情報を表示
print("比較動画A: ", end="")
if mov_A == "":
    mov_A = input() # 未指定時に入力
else:
    print(mov_A)

# 動画Bの情報を表示
print("比較動画B: ", end="")
if mov_B == "":
    mov_B = input() # 未指定時に入力
else:
    print(mov_B)

# 描画間隔を表示
print("描画間隔(フレーム): ", end="")
if interval <= 0:
    interval = 30
print(interval)


# 動画の読み込み
video1 = cv2.VideoCapture(mov_A)
video2 = cv2.VideoCapture(mov_B)
brightness = []

# 開始秒数
startTime = time.time()

i = 1
interval_max_brightness = 0
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

    # 最大値を更新
    interval_max_brightness = max(interval_max_brightness, diff_v_mean)

    # 描画間隔ごとに更新
    if (i % interval == 0):
        # グラフをクリアして描画
        plt.cla()
        plt.plot(brightness)
        plt.plot(interval_max_brightness)
        # グラフのラベルを設定
        plt.xlabel("frame")
        plt.ylabel("brightness")
        plt.ylim(0, 255)
        plt.pause(0.0001)
        
        # 画像を表示
        cv2.imshow('diffm', diff)
        cv2.waitKey(1)

        # フレーム番号と区間内の最大値を表示
        print("frame: <", i, "| brightness:", interval_max_brightness)
        interval_max_brightness = 0

    i += 1

# 実行にどれくらいかかったか
print("time: ", (time.time() - startTime), "[sec]")
cv2.waitKey(0)

# メモリ解放
video1.release()
video2.release()
