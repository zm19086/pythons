# ファイルのパス指定
windowsの場合 -> C:\Users\(ユーザ名)\Desktop
macの場合 -> /Users/(ユーザ名)/Desktop

## windwsの場合

### 現在パソコンが参照している階層を確認するcdコマンド
C:¥Users¥(ユーザ名)>cd
C:¥Users¥(ユーザ名)

C:¥Users¥(ユーザ名)>cd


### 今いる階層にあるファイルのリストを確認するdirコマンド
C:¥Users¥(ユーザ名)>dir
  ドライブ C のボリューム ラベルがありません
  ボリューム シリアル番号は xxxx-xxxx です

C:¥Users(ユーザ名) のディレクトリ

xxxx/xx/xx xx:xx     <DIR>        .
xxxx/xx/xx xx:xx     <DIR>        ..
       .
       .
       .


### 今いる階層から移動するcdコマンド
C:\Users¥(ユーザ名)>cd (移動先パス(今回はDesktop))

C:\Users¥(ユーザ名)¥Desktop>


### 今いる階層に新しくフォルダを作成するmkdirコマンド
C:\Users¥(ユーザ名)¥Desktop>mkdir (フォルダ名)


### ここまでのまとめ
cd     (current directory : 現在の参照地点を表示する)(change directory : 現在地から指定した別の場所に移動する)
dir    (directory : 現在の階層にあるファイルのリストを表示する)
mkdir  (make directory : 現在の階層に指定したフォルダを作成する)



## Macの場合

### 現在パソコンが参照している階層を確認するpwdコマンド
$ pwd
/Users/(ユーザ名)

# 現在の階層にあるフォルダ、ファイルのリストを表示するlsコマンド
$ ls
Applications    Public      Library
Desktop         Movies      Documents
Music           Downloads   Pictures

### 指定した別の場所に移動する
$ cd (移動先パス(今回はDesktop))
$ pwd
/Users/(ユーザ名)/Desktop
$ ls
Applications    Public      Library
Desktop         Movies      Documents
Music           Downloads   Pictures

# 現在の階層に新たにフォルダを作成するmkdirコマンド
$ mkdir (フォルダ名)

### ここまでのまとめ
pwd    (print working directory : 現在の参照地点を表示する)
ls     (list : 現在の階層にあるファイルのリストを表示する)
cd     (change directory : 現在地から指定した別の場所に移動する)
mkdir  (make directory : 現在の階層に指定したフォルダを作成する)