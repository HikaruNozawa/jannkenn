# jannkenn
動作内容・ルール
じゃんけんを行います
1 は 3 に強く 2 は 1 に強く 3 は 1 に強いとした
数字を入力すると勝ち・引き分け・負けの結果を表示します
1 から 3 以外の数字を入力するとコマンドが間違っていると表示します


動作手順
Tera Term を 3 つ起動し raspberry pi 3 と SSH 通信します
そのうちの 1 つは roscore を実行します
もう 2 つをプログラムのある scripts まで移動します
片方で rosrun mypkg count.py を実行し，もう片方で　rosrun mypkg twice.py を実行します
count.py 側で数字を入力すると twice.py 側が対応した結果を表示します
