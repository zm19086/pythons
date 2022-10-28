### pythonと共同開発の練習

# python

・自由に開発してOK

・各々フォルダを作っておく
　-> okayuフォルダ、donフォルダ など

・ファイル名は内容がわかりやすい名前にする

・基本的な文法などはsample_folderを参照する



### 共同開発 git

一番最初のみ行う操作 ▼

git clone -b work1 https://github.com/zm19086/pythons.git

git remote add origin https://github.com/zm19086/pythons.git



作業を始める前に毎回行う操作 ▼

git checkout -b (ブランチ名)
*ブランチ名はなんでもいい -> 例) git checkout -b work1
*ブランチ名の最後に数字をつけると管理が楽　次の開発の時は work2 など



作業が終わったら毎回行う操作 ▼

git add .
->      ^ ここのドット(.)を忘れずに！

git commit -m "変更内容"
-> 例) git commit -m "chenge sample_folder/.class.py line 4"

git push origin (その時のブランチ名)
＊その時のブランチ名を確認するには　git branch を入力し、緑色で表示されているところが今のブランチ



最新の状態に更新する時 ▼  (※要検証)

git checkout main

git pull origin main

git checkout (その時のブランチ名)