# Offensive 200
## Q
Category: Analysis-offensive  
Points: 200

Click button to get the flag!

### 概要
Androidアプリケーション（[VirusClicker.apk](https://github.com/asakasa/ctfs/blob/master/TMCTF2015/data/VirusClicker.apk)）があたえられる．
Androidアプリケーションを実行すると，
「画面を10000000回タップするとフラグが出てくる」と思われるアプリケーションで
あることがわかる．

## A
画面を10000000回も人力でタップしていられないので，APKファイルをデコンパイルする．
```Bash
$ unzip VirusClicker.apk -d VirusClicker # APKファイルはただの圧縮ファイルなので，解凍可能
...
$ cd VirusClicker/
$ d2j-dex2jar classes.dex
dex2jar classes.dex -> ./classes-dex2jar.jar
$ unzip classes-dex2jar.jar -d src # jarファイルも解凍可能
...
```

ここまでで，まずアプリケーションのクラスファイルの抽出までが完了した．  
この後，クラスファイルからリバーシングを行うが，いくつかの方法が存在するため，好きな方法で良い．
下に例を挙げる．

- jad コマンドを利用して，クラスファイルからJavaファイルを抽出する
- JD-GUI（JD-GUIの場合，jarファイルの状態からリバーシング可能）
- JD-IntelliJ

ここでは，JD-IntelliJ を利用する．このプラグインを利用すると，
classファイルから自動でJavaファイルに変換してくれるため，中身のコードを確認することが出来る．

ソースコードのディレクトリ構造を確認すると，CongraturationsActivityといった如何にも怪しいファイルが存在する．
中身を確認すると，このアクティビティを起点にフラグが表示されるような構成になっていることがわかる．
```Java
b a = null;
// 中略
setContentView(a); // クラスbのインスタンスaを表示する
```

そこで次は，クラスbを確認すると，フラグの表示に関する記述があった．
```Java
private void a(Canvas paramCanvas, Paint paramPaint)
{
  // 略
  String str2 = "TMCTF{" + f + "}";
  // 略
}
```

これより，クラスbのメンバ変数fが最終的なフラグの値であることが判明する．
そのため，fがどのようにして組み立てられているのかを調べるのも良い（実際にコードを読み解きながら調べた人もいる）が，
今回のアプリケーションは，1000万回タップすればフラグがゲット出来るようだったので，
コードのなかにある1000万回という記述の部分を書き換え，再度，アプリケーションの形にビルドし直す．

まずコード中の10000000という部分を調べる．何となく16進の可能性もあると考えていたため，合わせて0x989680でも検索をする．
```Bash
$ find src-java/com/ -type f | xargs grep -iE "10000000|989680"
src-java/com//tm/ctf/clicker/activity/c.java:        String s1 = Integer.toString(0x989680);
src-java/com//tm/ctf/clicker/activity/c.java:        if(0x989680 <= g)
src-java/com//tm/ctf/clicker/activity/CongraturationsActivity.java:        if(0x989680 != com.tm.ctf.clicker.a.a.c())
```
結果より，それぞれのソースの0x989680の部分を0xAに書き換える必要があるが，
javaソースをそのまま書き換えてビルドし直すことは，恐らく不可能か現実的ではない
（ライブラリ等依存関係を解決したりと手間がかかる）．
そのため，アプリケーションのバイトコードを書き換える（詳しくは後述）．

先に結論をいうと，上記の1000万回の部分を10回に書き換えたうえで，アプリケーションを起動し試した結果，
正常にフラグが出現しなかった．そのため，もう一度コードを確認すると，
どうやらタップ回数にチェックポイント的な要素が存在することが判明した．
```Java
// in クラスc
if ((3769 == g) || (10007 == g) || (59239 == g) || (100003 == g) || (495221 == g) || (1000003 == g) || (9999999 == g))
{
  paramMotionEvent = new Intent("com.tm.ctf.clicker.SCORE");
  paramMotionEvent.putExtra("SCORE", g);
  a.sendBroadcast(paramMotionEvent);
}
// in クラスScoreBroadcastReceiver
if (10007 == i) {
  paramContext = "x";
} else if (59239 == i) {
  paramContext = "p";
} else if (100003 == i) {
  paramContext = "Y";
} else if (495221 == i) {
  paramContext = "2";
} else if (1000003 == i) {
  paramContext = "t";
} else if (9999999 == i) {
  paramContext = "z";
}
```
これにより，タップ回数が以上に挙げた数値（10007, 59239, 100003, 495221, 1000003, 9999999）になった場合に，
フラグの文字列を操作するような処理であったことが判明した．そのため，先ほどの1000万回と同じく，これらの数値を書き換えた．

書き換えに際し上述したJavaのソースコードの書き換えは現実的でないため，アプリケーションのバイトコードを書き換える
（Javaソースコードを書き換えた場合はAndroidアプリケーションとしてコンパイルしビルドする必要があるが，
バイトコードを書き換えた場合はコンパイルの必要がなくビルドのみ行えばよい）．
バイトコードはsmaliと呼ばれる形式で記述されている．
今回の場合は，数値を書き換えればいいため，非常に簡単（数値はそのままコード内に記述されている）である．
```Bash
$ apktool d VirusClicker.apk
$ # 各バイトコード内の関連する数値を編集する
$ diff c.smali
356c356
<     const v2, 0xA
---
>     const v2, 0x989680
781c781
<     const/16 v0, 0x1
---
>     const/16 v0, 0xeb9
787c787
<     const/16 v0, 0x2
---
>     const/16 v0, 0x2717
793c793
<     const v0, 0x3
---
>     const v0, 0xe767
799c799
<     const v0, 0x4
---
>     const v0, 0x186a3
805c805
<     const v0, 0x5
---
>     const v0, 0x78e75
811c811
<     const v0, 0x6
---
>     const v0, 0xf4243
817c817
<     const v0, 0x7
---
>     const v0, 0x98967f
841c841
<     const v0, 0xA
---
>     const v0, 0x989680

$ diff CongraturationsActivity.smali
144c144
<     const v0, 0xA
---
>     const v0, 0x989680

$ diff ScoreBroadcastReceiver.smali
29c29
<     const/16 v2, 0x1
---
>     const/16 v2, 0xeb9
42c42
<     const/16 v2, 0x2
---
>     const/16 v2, 0x2717
51c51
<     const v2, 0x3
---
>     const v2, 0xe767
60c60
<     const v2, 0x4
---
>     const v2, 0x186a3
69c69
<     const v2, 0x5
---
>     const v2, 0x78e75
78c78
<     const v2, 0x6
---
>     const v2, 0xf4243
87c87
<     const v2, 0x7
---
>     const v2, 0x98967f

```

各数値を適当な値に書き換えた後，アプリケーションのビルドを行う．
そして，アプリケーションをインストールするために，アプリケーションに対して署名を行う．
```Bash
$ apktool b VirusClicker -o VirusClicker.apk
$ adb install VirusClicker.apk
```
これらの手順が終了したら，アプリケーションをシステムにインストールし，
実際にアプリケーションを起動し0xA回タップすると，フラグがゲット出来た．

![flag](https://github.com/asakasa/ctfs/blob/master/TMCTF2015/img/off200-flag.png)

## FLAG
***TMCTF{Congrats_10MClicks}***
