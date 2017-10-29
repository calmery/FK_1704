# すぺちゃるぺ~ん
[![Product Name](https://raw.github.com/GabLeRoux/WebMole/master/ressources/WebMole_Youtube_Video.png)](https://www.youtube.com/channel/UC4PtjOfZTbVp9DwtJv82Lzg)

## 製品概要
### X Tech（X → 教育）

### 背景（製品開発のきっかけ、課題等）
ここに

プロダクトの開発に至った経緯として,
- こんかいのプロダクトの開発に至った背景
- 着目した顧客・顧客の課題・現状
を記入してください

### 製品説明（具体的な製品の説明）
本製品は,ペン型のADコンバーターである.
具体的には,本デバイスを装着したペンで文字を書くと,PC上からその文字がフォントとして扱うことが可能となる.
また,デバイスとPC間の通信の方法としてbluetoothとwifiを利用する.書いた文字のデータの受け渡しはbluetooth,ペンへのプラグインの追加の際はwifiを用いる.

### 特長

#### 1. センサーから取得した加速度を用いて文字を認識することができる
#### 2. キャップ型デバイスだからこそ得られる汎用性の高さ
#### 3. プラグインによる,昨日面における豊かな拡張性

### 解決出来ること
初等教育現場における,宿題や提出物の採点にかかる教師の負担の軽減.

### 今後の展望
デバイスの小型や文字認識の精度向上.
対応文字(ひらがな,カタカナ,漢字,外国語)の拡大.

## 開発内容・開発技術

### 活用した技術
機械学習

#### API・データ
特になし

#### フレームワーク・ライブラリ・モジュール
##### Raspberry Pi Zero W
[Pykka](https://www.pykka.org/en/latest/)  
[Keras](https://keras.io/)  
[TensorFlow](https://www.tensorflow.org/)  
[Requests](http://docs.python-requests.org/en/master/)  
##### Server
[Laravel](https://laravel.com/)
##### Client ([package.json](https://github.com/jphacks/FK_1704/blob/master/Client/package.json)/[elm-package.json](https://github.com/jphacks/FK_1704/blob/master/Client/elm-package.json))
[Express](http://expressjs.com/)  
[Socket.IO](https://socket.io/)  
[Electron](https://electron.atom.io/)  
[Elm](http://elm-lang.org/)  
[Babel](https://babeljs.io/)  
[Webpack](https://webpack.js.org/)

#### デバイス
[Raspberry Pi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/)  
MPU-9250 9軸センサモジュール

### 研究内容・事前開発プロダクト（任意）
特になし

### 独自開発技術（Hack Dayで開発したもの）
#### 2日間に開発した独自の機能・技術
* 独自で開発したものの内容をこちらに記載してください
* 特に力を入れた部分をファイルリンク、またはcommit_idを記載してください（任意）
