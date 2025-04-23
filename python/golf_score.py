import sys
result_list = []
sum_list = [-4, -3, -2, -1, 0, 1]
t = []
w = []
r = []
# cat case_1.txt | python golf_score.py実行したら、イーグル,バーディ,コンドル,2ボギー,3ボギー,バーディ,ボギー,ホールインワン,ボギー,2ボギー,アルバトロス,ボギー,3ボギー,バーディ,ボギー,ボギー,バーディ,ボギーが返ってくる

# cat case_1.txt(ファイルの内容を出力する) |

# python golf_score.py(標準出力を受け取る)実行する

# 標準出力を受け取る(4,4,5,3,5,4,4,3,4,4,5,4,4,3,4,4,3,5,2,3,1,5,8,3,5,1,5,6,2,5,7,2,5,5,2,6)
for i in range(2):
    input_line = str(input())
    
    # print(input_line)
# 一行目と二行目を別々の変数に格納する(一行目：4,4,5,3,5,4,4,3,4,4,5,4,4,3,4,4,3,5, 2行目:2,3,1,5,8,3,5,1,5,6,2,5,7,2,5,5,2,6)
    s = input_line.split(',')
    for z in s:
        t.append(z)
        w.append(z)
x = t[:18]
y = w[18:]
    
# 一行目と二行目をint型のリストに変換する(x =[4,4,5,3,5,4,4,3,4,4,5,4,4,3,4,4,3,5],y = [2,3,1,5,8,3,5,1,5,6,2,5,7,2,5,5,2,6])
x = [int(v) for v in x]
y = [int(l) for l in y]

# for文で繰り返し処理する
# y[0]-x[0]を計算する(-2)
r =[c - b for b,c in zip(x,y)]
# 上の結果を文字に変換する('イーグル')
for d, f in zip(r,y):
    if f == 1:
        result_list.append('ホールインワン')
    elif d >= 2:
        result_list.append(f'{d}ボギー')
    elif d == -4:
        result_list.append('コンドル')
    elif d == -3:
        result_list.append('アルバトロス')
    elif d == -2:
        result_list.append('イーグル')
    elif d ==-1:
        result_list.append('バーディ')
    elif d == 0:
        result_list.append('パー')
    else:
        result_list.append('ボギー')
print(result_list)
   
# イーグル,バーディ,コンドル,2ボギー,3ボギー,バーディ,ボギー,ホールインワン,ボギー,2ボギー,アルバトロス,ボギー,3ボギー,バーディ,ボギー,ボギー,バーディ,ボギーが返ってくる

