# Flash
## Question
We were able to grab an image of a harddrive. Find out what's on it.

[flash_c8429a430278283c0e571baebca3d139.img.zip](https://github.com/asakasa/ctfs/blob/master/CSAW_CTF_2015/data/flash_c8429a430278283c0e571baebca3d139.img.zip)

注：添付ファイルは，ファイルサイズの関係によりzipで圧縮しています．

## Answer
添付されたイメージファイルを何らかの方法でマウントする．
マウントした中身を確認すると適当なファイルが多く存在する．
ファイルの中身は，著作権フリーな小説であったり，ただの数値であったりする．
とりあえず，flagっていう文字列で検索をかけてみると，見つかった(・∀・)

```
$ find . -type f | xargs grep flag
〜中略〜
./.10/.hidden:flag{b3l0w_th3_r4dar}
```

## Flag
***flag{b3l0w_th3_r4dar}***
