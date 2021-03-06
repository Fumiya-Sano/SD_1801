# Food Manipulator

[![Product Name](image.png)](https://www.youtube.com/watch?v=G5rULR53uMk)

## 製品概要
### Food X Tech

### 背景（製品開発のきっかけ、課題等）
一人暮らしをしていると食材を余らせてしまうことがよくあります。料理をする頻度も多くないのでその食材を傷ませて、捨ててしまうことが少なくありません。せっかく買ってきた食材を廃棄してしまうのは勿体無いし、環境にも悪い。そこで、食材管理の苦手な一人暮らしの人でも、賞味期限が切れそうな食材を消費できるような、手軽に使えるアプリがあると便利だと考えました。

### 製品説明（具体的な製品の説明）
Food Manipulatorは自宅の食材を管理することのできるアプリです。食品名の記載されたレシートをスマートフォンのカメラで撮影し、商品名を自動で読み込み、賞味期限を登録します。登録された食材は賞味期限が近づくとスマートフォン上で通知されて、使用者は賞味期限前に知ることができます。さらにFood Manipulatorは手持ちの食材を材料としたレシピを提案してくれるので余った食材もすぐに活用できます。

### 特長

#### 1. レシートから簡単読み取り！
レシートをスマートフォンのカメラに写すだけなので簡単に、かつ一度に複数の食材を読み込むことができるので手軽に利用できます。
#### 2. 賞味期限を事前に通知！
登録した食材は賞味期限が近づくと自動で通知されるので、忘れていても腐る心配なし。
#### 3. 余った食材はすぐにレシピ検索！
アプリ上で余った食材を使ったレシピを提案してくれるので、レシピに悩むことも無くなります。

### 解決出来ること
賞味期限が過ぎて食材を捨ててしまう問題を解決します。広く言えば食料廃棄問題の解決策です。
また、レシピに悩むようなことも無くなります。

### 今後の展望
・読み取り精度の向上: 
レシートに記載されている商品名は途切れていたり、表記が統一されていなかったりして読み取れない場合があります。また食材によってはレシピ検索をしてもヒットしないことがあります。

・複数食材でのレシピ検索: 
複数の食材（例：豆腐とネギ）が余っているとき、それぞれの食材を使うレシピ（例：冷奴とネギ焼き）は検索できますが、全ての材料を使ったレシピ（例：豆腐とネギの味噌汁）は検索することがまだできていません。効率的に余った食材を消費するには複数食材のレシピ検索が必要です。

## 開発内容・開発技術
### 活用した技術
#### API・データ

* Google Cloud Vision API
* 楽天レシピカテゴリ一覧API
* 楽天レシピカテゴリ別ランキングAPI

#### フレームワーク・ライブラリ・モジュール
* flask
* heroku

#### デバイス
* iPhone

### 研究内容・事前開発プロダクト（任意）
ご自身やチームの研究内容や、事前に持ち込みをしたプロダクトがある場合は、こちらに実績なども含め記載をして下さい。

*  
*


### 独自開発技術（Hack Dayで開発したもの）
#### 2日間に開発した独自の機能・技術
* https://github.com/Fumiya-Sano/DFM.git
