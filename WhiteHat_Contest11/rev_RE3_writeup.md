# RE3

Category: Reverse Engineering   
Points: 100

## Question

```
http://material.wargame.whitehat.vn/contests/11/digital_fortrees.exe

flag = SHA1(FirstRoom:SecondRoom:ThridRoom)
```

## Answer

まずは普通に ```digital_fortrees.exe``` を実行してみる．

```
> digital_fortrees.exe
...
Welcome to DIGITAL FORTRESS
Be carefull with your choice:
1: Draw infinity map
2: Go through all room on your map
What's your choice:
```

Windowsなら問題なく実行可能．  
※ ただし，1を選ぶと大量の空フォルダが実行フォルダ内に生成されるので注意.

stringsコマンドで文字列を探ってみると，**pythondll** などpython関係と思われる単語が多数見つかる．  
このファイルは **py2exe** というモジュールによってPythonスクリプトをPE形式に変換して作ったものらしい．

**unpy2exe** と **uncompyle2** を使えばPE形式からpythonスクリプトを復元することができる．

```python
#Embedded file name: digital_fortrees.py
import urllib2

def main():
    print "                                       /\\\n                                      /`:\\\n                                     /`'`:\\\n                                    /`'`'`:\\\n                                   /`'`'`'`:\\\n                                  /`'`'`'`'`:\\\n                                   |`'`'`'`:|\n     _ _  _  _  _                  |] ,-.  :|_  _  _  _\n    ||| || || || |                 |  |_| ||| || || || |\n    |`' `' `' `'.|                 | _'=' |`' `' `' `'.|\n    :          .:;                 |'-'   :          .:;\n     \\-..____..:/  _  _  _  _  _  _| _  _'-\\-..____..:/\n      :--------:_,' || || || || || || || `.::--------:\n      |]     .:|:.  `' `'_`' `' `' `' `'    | '-'  .:|\n      |  ,-. .[|:._     '-' ____     ___    |   ,-.'-|\n      |  | | .:|'--'_     ,'____`.  '---'   |   | |.:|\n      |  |_| .:|:.'--' ()/,| |`|`.\\()   __  |   |_|.:|\n      |  '=' .:|:.     |::_|_|_|\\|::   '--' |  _'='.:|\n      | __   .:|:.     ;||-,-,-,-,|;        | '--' .:|\n      |'--'  .:|:. _  ; ||       |:|        |      .:|\n      |      .:|:.'-':  ||       |;|     _  |]     _:|\n      |      '-|:.   ;  ||       :||    '-' |     '--|\n      |  _   .:|].  ;   ||       ;||]       |   _  .:|\n      | '-'  .:|:. :   [||      ;|||        |  '-' .:|\n  ,', ;._____.::-- ;---->'-,--,:-'<'--------;._____.::.`.\n ((  (          )_;___,' ,' ,  ; //________(          ) ))\n  `. _`--------' : -,' ' , ' '; //-       _ `--------' ,'\n       __  .--'  ;,' ,'  ,  ': //    -.._    __  _.-  -\n   `-   --    _ ;',' ,'  ,' ,;/_  -.       ---    _,\n       _,.   /-:,_,_,_,_,_,_(/:-\\   ,     ,.    _\n     -'   `-'--'-'-'-'-'-'-'-''--'-' `-'`'  `'`' `-\n"
    print 'Welcome to DIGITAL FORTRESS'
    while 1:
        print 'Be carefull with your choice: '
        print '1: Draw infinity map'
        print '2: Go through all room on your map'
        choice = '-1'
        while not choice.isdigit():
            choice = raw_input("What's your choice: ")
            if choice not in ('1', '2'):
                choice = '-1'

        choice = int(choice)
        if choice == 1:
            exec (urllib2.urlopen('http://material.wargame.whitehat.vn/contests/11/drawmap.py').read(), globals())
        elif choice == 2:
            exec (urllib2.urlopen('http://material.wargame.whitehat.vn/contests/11/letgo.py').read(), globals())


if __name__ == '__main__':
    main()
```

復元したスクリプトの中を見ると， ```drawmap.py``` と ```letgo.py``` というpythonスクリプトをダウンロードして実行している．  


```python
# drawmap.py
import os
import errno
import math

def draw():
    current = 2
    check_map("2")
    print 'Press Ctrl + C to stop draw map'

    while 1:
        try:
            current = find_next_prime(current)
            check_map(str(current))
        except KeyboardInterrupt:
            break

def check_map(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno !=errno.EEXIST:
            raise

def find_next_prime(current):
    flag = False
    for p in range(current+1, current*2):
        for i in range(2, int(math.sqrt(p)) + 1):
            if p % i == 0:
                flag = True
                break
        if flag == False:
            return p
        else:
            flag = False

draw()
```



```python
# letgo.py
import os

def gothrough():
    key = 1
    roomtogo = [r for r in os.listdir(os.curdir)if os.path.isdir(r)]
    for room in roomtogo:
        key *= int(room)
        os.system("start cmd /k echo Room number " + room + ": get key part")
    if (key == 1000012277050240711531267079):
        os.system("start cmd /k echo Congrats! Where did you get these key parts?")
    else:
        os.system("start cmd /k echo Nothing here! wrong key parts")

gothrough()
```

```drawmap.py``` は**素数をフォルダ名にした**空フォルダを無限に生成するプログラム．  
```letgo.py``` は実行フォルダにある全てのフォルダ名（素数）を読み込み
，それらの積が ***1000012277050240711531267079*** のときに ```Congrats! Where did you get these key parts?``` と表示するプログラム．

つまり，これは ***1000012277050240711531267079*** を素因数分解しろという問題である．  

素因数データベースの[factordb](http://www.factordb.com/index.php)で ***1000012277050240711531267079*** を調べると一発でヒットする．

```
FF	28 (show)	1000012277050240711531267079<28> = 1000004059<10> · 1000004099<10> · 1000004119<10>
```

Flagの書式は ```SHA1(FirstRoom:SecondRoom:ThridRoom)``` ，というわけで ```1000004059:1000004099:1000004119``` のsha1ハッシュがFlagである．

## Flag
***89225c98a509271436fd55c3c6aeef44fd07728a***
