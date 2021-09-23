# setlist_forecast
主にアイドル用のセットリスト予想アプリ


## データの取込について

#### ①基本的な情報の取込
 - fixtureを用いる
 - core/fixture/crossnoesiss.jsonでクロスノエシス固有情報が保存できる
 - python manage.py loaddata core/fixtures/crossnoesiss.json

#### ②ツイートの取込方法

- import_tweetのバッチを動かす
   - Twitterアカウントが登録されている全ユーザーを対象に取り込む
  
#### ③　カレンダーの取込
- import_calenderを動かす

#### ライブ情報の取込
- カレンダー情報からライブと思われる物を取り込む(中止は入れない)
- ライブモデルを作成する

