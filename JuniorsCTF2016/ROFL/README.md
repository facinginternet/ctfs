
# ROFL
## trivial admin : [https://scoreboard.ctf.org.ru/task?id=35](https://scoreboard.ctf.org.ru/task?id=35)

問題文に，かなり大量のテキストが埋めこまれていた[PDFファイル](./text.pdf)があるため，
それをダウンロードする．

次に，ダウンロードしたPDFファイルの情報を確かめる．
`exiftool`や`binwalk`等を試してみたが，特に変わったところはなかった．
そこで，PDFファイルに埋めこまれているテキストをみてみることにした．
テキストを流して読んでみると，どうもBase64エンコードされているだろうと推測できる．

とりあえず，中身のテキストを抽出しないことには始まらないため，
`pdftotext`を使ってテキスト化を施す．
抽出されたテキストをもとにBase64デコードをしてみると，
テキストの文字数は減ったものの，またしてもBase64エンコードされているような文字列が得られた．
なので，とりあえず，無限ループ内でBase64をデコードしてみると，最終的にあるバイナリが得られた．
次は，このバイナリが何であるかを把握する必要がある．
`file`コマンドを使うとある文字コードが表示されたため，
`nkf`コマンドを使って表示してみるが，ちゃんとした文字が得られなかった．
そこで，このCTFをホストしている国がロシアであったことを思い出し，
ロシア語の文字コード(KOI8-R)に変換してみたところ，正しい文字列が得られた．

最終的なスクリプトは，以下のようなものになった．

```bash
#!/bin/bash

pdftotext text.pdf text.txt
text=$(cat text.txt)
rm -f text.txt

while true; do
    echo -n $text | base64 -D >/dev/null 2>/dev/null
    if [[ $? != 0 ]]; then
        break
    fi
    text=$(echo -n $text | base64 -D)
    echo $text
done

iconv -f KOI8-R -t utf-8 <(echo -n $text)
```


## FLAG: `ХиЖинА_чУдеС`

