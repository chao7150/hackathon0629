# バーチャル文豪
- このプログラムは2018年6月29日のドワンゴエンジニアハッカソン（お題：バーチャル）で書かれた。


## 使用法
```
pip install -r requirements.txt
python main.py
```

## 機能
入力された文章を形態素解析し、青空文庫に公開されている文豪の文章と適当にブレンドして返します。同じ文章を入力しても同じ文章が返ってくるとは限りません。

## 例
[from](http://dwango.co.jp/corporate/greetings.html)
>ドワンゴは「クリエイティブリーダーシップ」の会社です。クリエイティブリーダーシップとは、「テクノロジー」と「コンテンツ」両面の進化で新しい文化を創り出し続けていくことです。インターネットの世界には、才能のある人がまだまだたくさん埋もれています。自ら発信する意欲を持ったネットユーザーが、これほど多く存在している国は日本を於いて他にありません。ドワンゴがテクノロジーを結集して作るオープンなプラットフォームのニコニコ動画で、コンテンツを生み出す才能のあるユーザーの皆さんが活躍する―――そんな未来を共に創る、新しいチーム・ドワンゴを作ることが私の経営コンセプトです。

to
>やはりドワンゴと云う新クリエイティブのリーダーシップの会社な名を付けておく方が彼等のためによかろうと思う。。クリエイティブでもない。。互いに相インターネットをある、互いに相世界埋もれて、ついには才能人たくさんのいを取り、世間に歯すべからざるに至るものなり。。するで持っ自らは発信の意欲のネットのユーザーのこれな存在国であった。。ドワンゴがそのテクノロジーであるから、結集のオープンなどは、元よりプラットフォームもして動画るコンテンツがなかった。


## LICENSE
- 本プログラムに含まれる文学作品データ（resourcesディレクトリの中身）の複製・再配布等にあたっては青空文庫及び青空文庫形態素解析データ集の規約を参照されたい。
- それ以外のプログラムは<a rel="license" href="http://creativecommons.org/licenses/by-sa/2.1/jp/"><img alt="クリエイティブ・コモンズ・ライセンス" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/2.1/jp/88x31.png" /></a><a rel="license" href="http://creativecommons.org/licenses/by-sa/2.1/jp/">クリエイティブ・コモンズ 表示 - 継承 2.1 日本 ライセンス</a>に従う。

## THANKS
- 青空文庫工作員のみなさま
  - [〔雨ニモマケズ〕](https://www.aozora.gr.jp/cards/000081/card45630.html)
  - [山月記](https://www.aozora.gr.jp/cards/000119/card624.html)
  - [吾輩は猫である](https://www.aozora.gr.jp/cards/000148/card789.html)
  - [舞姫](https://www.aozora.gr.jp/cards/000129/card2078.html)
  - [走れメロス](https://www.aozora.gr.jp/cards/000035/card1567.html)
  - [羅生門](https://www.aozora.gr.jp/cards/000879/card127.html)
  - [源氏物語 01 桐壺](https://www.aozora.gr.jp/cards/000052/card5016.html)
  - [学問のすすめ](https://www.aozora.gr.jp/cards/000296/card47061.html)
- [青空文庫形態素解析データ集（河原翔氏作成）](http://aozora-word.hahasoha.net/index.html)
