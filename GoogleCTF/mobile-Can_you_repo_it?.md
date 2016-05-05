# Can you repo it?
Category: Mobile  
Point: 5

## Question
Do you think the developer of Ill Intentions knows how to set up public repositories?

## FLAG
`ctf{TheHairCutTookALoadOffMyMind}`

## Answer
まず，この問題とは別の問題で，[illintentions.apk](./data/illintentions.apk)というAPKファイルが与えられている（data/ディレクトリ参照）．

このAPKファイルを`apktool`を使い解凍する．  
中を確認すると，Resourcesのなかのstring.xmlにGitHubのユーザ名が書かれている．
```bash
$ apktool d illintentions.apk
$ cd illintentions/
$ cat res/values/strings.xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="android.permission._msg">Msg permission for this app</string>
    <string name="app_name">SendAnIntentApplication</string>
    <string name="dev_name">Leetdev</string>
    <string name="flag">Qvq lbh guvax vg jbhyq or gung rnfl?</string>
    <string name="git_user">l33tdev42</string>
    <string name="str1">`wTtqnVfxfLtxKB}YWFqqnXaOIck`</string>
    <string name="str2">IIjsWa}iy</string>
    <string name="str3">TRytfrgooq|F{i-JovFBungFk</string>
    <string name="str4">H0l3kwjo1|+kdl^polr</string>
    <string name="test">Test String for debugging</string>
</resources>
$ cat res/values/strings.xml | grep git_user
    <string name="git_user">l33tdev42</string>
```

ここで，このAPKファイルを作ったと思われる製作者のgitのユーザ名`l33tdev42`がわかる．

このユーザ名で，GitHubを検索すると，該当ユーザの[ページ](https://github.com/l33tdev42/)が表示される．
このユーザのリポジトリは一つしかなく，その中身を確認すると怪しいコミットが存在し，
さらに中を確認すると[フラグ](https://github.com/l33tdev42/testApp/commit/5b315cbbfaa2da9502ffae73f283d36d89f92194#diff-39e7d8c00954e920b98e7636f0ac30b2L25)が存在する．

## Author
GitHub: @asakasa
