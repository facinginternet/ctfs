# Keep Calm And CTF
## Question
My friend sends me pictures before every ctf. He told me this one was special.

Note: this flag doesn't follow the "flag{}" format

![img.jpg](https://github.com/asakasa/ctfs/blob/master/CSAW_CTF_2015/data/img.jpg)

## Answer
この問題は，添付された画像ファイルのなかに隠されたフラグを探すものである．
こういったデータを渡された場合は，まずデータの中にある文字列を検索する．
検索には複数の方法が存在し，例えば，以下のようなものがある．
- **strings** (Unix command)
- **exiftool** (Unix command)
- **bintext** (Windows Application)
- *etc...*

*strings*コマンドは，標準で使えるため便利であるが，*exiftool*を使ったほうが
見易い形で表示してくれることが多い．

```
$ exiftool img.jpg
ExifTool Version Number         : 9.91
File Name                       : img.jpg
Directory                       : .
File Size                       : 95 kB
File Modification Date/Time     : 2015:09:19 12:31:31+09:00
File Access Date/Time           : 2015:09:23 17:05:31+09:00
File Inode Change Date/Time     : 2015:09:19 12:31:31+09:00
File Permissions                : rw-r-----
File Type                       : JPEG
MIME Type                       : image/jpeg
Exif Byte Order                 : Big-endian (Motorola, MM)
Resolution Unit                 : inches
Copyright                       : h1d1ng_in_4lm0st_pla1n_sigh7
XMP Toolkit                     : XMP Core 5.4.0
Rights                          : h1d1ng_in_4lm0st_pla1n_sigh7
Subject                         :
Image Width                     : 600
Image Height                    : 700
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 600x700
Megapixels                      : 0.420
```

結果より，CopyrightおよびRightsセクションに存在する***h1d1ng_in_4lm0st_pla1n_sigh7***がフラグである．
今回のフラグのように，数字をアルファベットに見立てる技法は，CTF業界ひいてはコンピュータ業界で良く使われる．

## Flag
***flag{h1d1ng_in_4lm0st_pla1n_sigh7}***
