# 概要
設定したホットキーを押すとウィンドウをトレイアイコンとして登録できるものです  

# 使い方
"Settings"フォルダの"Keyboard.json"に書いてある「HotKey」のキーの値を設定したいキーの組み合わせに書き換えて  
"main.pyw"を実行し、お好きなウィンドウを選択(アクティブに)してから設定したホットキーを呼び出すとトレイにアイコンが登録されます  
アイコンを左クリックすると非表示と表示を切り替えられます  
右クリックすると「表示、非表示、終了(トレイアイコンのみ)、メニューを閉じる」の動作を選ぶことができます  
最大30個までトレイにアイコンを登録できます(変更したい場合はソースコードを読んで変更してください)  

# 既知の問題
1. 一部ソフトのアイコンを取得できない
1. 透明なアイコンを判定できないためアイコンの置き換えができていない
1. ハンドルリークが発生してしまう(常時起動に向いていない、リソースを無駄に占拠してしまう)
1. このソフト専用のアイコンを作れていない(タスクトレイにこのソフトのアイコンを登録できない)
1. タスクバーやスタートメニューなどのものまで登録できてしまう(OSの動作が不安定になる可能性がある, 非表示の解除方法がないため作る必要がある)
1. UWPアプリを登録できない(原因不明, exeから起動しているものは可能？)
1. スレッドが大量生成されてしまう
1. 一部win32apiを通していないものがあるためコード側からのカスタマイズ性が低くなっている(Pystrayなど)
  
1. コードに一貫性がない
1. 変数名の書式を統一していない
1. 構造が雑
1. コードに無駄や遠回りをしている処理が存在する
1. 実装がわかりずらい(Pythonの「シンプル イズ ベスト」の考えに背いている、初心者にすごくわかりずらい、普通にわかりずらすぎる)

# 予定
1. ハンドルリークの徹底的な修正をする
1. スタートメニューを登録できないようにする
1. タスクバー専用にホットキーを登録できるようにし、通常の動作では登録できないようにする
1. ウィンドウ毎に設定を保存できるようにする(exeファイル単位で設定)
1. タスクトレイでの動作をすべてwin32apiで独自実装する
1. コードを読みやすくする
1. 構造を改善する
1. 変数名の規則を作り修正する
1. このソフトのアイコンを作りこのソフトのトレイアイコンを実装する
1. 「.py」ファイルで処理を変更、追加できるようにする