
# Clone Attack
## trivial forensic : [https://scoreboard.ctf.org.ru/task?id=10](https://scoreboard.ctf.org.ru/task?id=10)

問題文にある画像をクリックして，[`dipper.7z`](./dipper.7z)ファイルを取得する．
ダウンロードしたファイルを解凍する．

`$ 7z x -odipper-imgs dipper.7z`

ディレクトリを移動して中身を確認すると，1001枚のJPEGファイルが存在している．
恐らく，このなかの1000枚がダミーで1枚が本物だろうと推測出来る．

まず，画像の情報を表示する．

```bash
$ exiftool 0BU2eQPmDAW4Omwb.jpg
ExifTool Version Number         : 10.20
File Name                       : 0BU2eQPmDAW4Omwb.jpg
Directory                       : .
File Size                       : 26 kB
File Modification Date/Time     : 2016:11:03 12:56:07+09:00
File Access Date/Time           : 2016:11:26 10:53:26+09:00
File Inode Change Date/Time     : 2016:11:26 05:28:17+09:00
File Permissions                : rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Current IPTC Digest             : 62413cf66d23ca631c3d4cb94abc3b89
Coded Character Set             : UTF8
Envelope Record Version         : 4
Object Name                     : Ксерокопия  номер  895
Application Record Version      : 4
Comment                         : Flag is MD5sum of this file. Its TRUE
Image Width                     : 193
Image Height                    : 400
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:4:4 (1 1)
Image Size                      : 193x400
Megapixels                      : 0.077
```

この情報のなかで興味深いセクションは，恐らく，`Object Name`と`Comment`だろう．
`Comment`は，本物の画像のMD5ハッシュ値がフラグだと示している．
試しにもう一枚の画像を確認してみると，`Comment`は同じだったが，
`Object Name`の末尾の数値が違っていた．

そこで，全ての画像ファイルから`Object Name`の値を取得してソートをしてみた．

```bash
$ find . -type f -name \*.jpg | xargs exiftool | grep 'Object Name' | sort -t' ' -k5,5 | tail
Object Name                     : Ксерокопия  номер  991
Object Name                     : Ксерокопия  номер  992
Object Name                     : Ксерокопия  номер  993
Object Name                     : Ксерокопия  номер  994
Object Name                     : Ксерокопия  номер  995
Object Name                     : Ксерокопия  номер  996
Object Name                     : Ксерокопия  номер  997
Object Name                     : Ксерокопия  номер  998
Object Name                     : Ксерокопия  номер  999
Object Name                     : Оригинальный Диппер
```

結果から，一枚の画像のみ値が違うことがわかった．
あとは，この画像の情報を取得する．

```bash
$ find . -type f -name \*.jpg | xargs exiftool | grep " Оригинальный Диппер" -C 20
Megapixels                      : 0.077
======== ./dipper/atvF2wf1tfB2IkuV.jpg
ExifTool Version Number         : 10.20
File Name                       : atvF2wf1tfB2IkuV.jpg
Directory                       : .
File Size                       : 26 kB
File Modification Date/Time     : 2016:11:03 12:56:08+09:00
File Access Date/Time           : 2016:11:26 05:53:49+09:00
File Inode Change Date/Time     : 2016:11:26 05:28:17+09:00
File Permissions                : rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Current IPTC Digest             : d576396322e6a76e8ebf29b2b1d2b7b1
Coded Character Set             : UTF8
Envelope Record Version         : 4
Object Name                     : Оригинальный Диппер
Application Record Version      : 4
Comment                         : Flag is MD5sum of this file. Its TRUE
Image Width                     : 193
Image Height                    : 400
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:4:4 (1 1)
Image Size                      : 193x400
Megapixels                      : 0.077
======== ./dipper/AW4rBJdiR1x5J4lJ.jpg
ExifTool Version Number         : 10.20
File Name                       : AW4rBJdiR1x5J4lJ.jpg
Directory                       : ./dipper
File Size                       : 26 kB
File Modification Date/Time     : 2016:11:03 12:56:08+09:00
File Access Date/Time           : 2016:11:26 05:53:49+09:00
File Inode Change Date/Time     : 2016:11:26 05:28:17+09:00
File Permissions                : rw-r--r--
File Type                       : JPEG
```

結果より，そのファイル名が何であるかがわかった．
あとは，このファイルのMD5ハッシュ値を調べて，サブミットすればよい．

```bash
$ md5sum atvF2wf1tfB2IkuV.jpg
cd4d19b8471cecbc8ea7544de59db368  atvF2wf1tfB2IkuV.jpg
```

## FLAG: `cd4d19b8471cecbc8ea7544de59db368`

