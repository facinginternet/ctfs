# EasyPie

Category: Reversing

Point: 100



## Question

Nothing much to say here. Take a look at the file given below and let us know if you can make sense out of it. 

[disasm](./disasm)



## Answer

問題のファイルをテキストエディタで開くと，`LOAD_CONST`や`BUILD_LIST`などと書いてあり，これらの文字列で検索するとPythonのdisモジュールで出力されたCPythonバイトコードの逆アセンブル結果であることがわかる．

[ドキュメント](http://docs.python.jp/2/library/dis.html)を参考に解読していくと，以下のような処理をするコードであることがわかる．

```
res = [0, -15, 6, -2, -12, 17, -17, 26, -4, -68, 44, 20, -6, -61, 59, -56, 44, 5, 5, -69, 61, -61, 0, 15, 58, -11, 10, -57, 49, -5, 13, -57, 0, 4, 70]
start = 'x'
flag = ''

for i in res:
	start = chr(ord(start) + i)
	flag += start

print(flag)
```

これを実行することでflagが得られる．

## Flag

`xiomara{w3_sm0k3_di$a$$3mbl3d_l337}`

