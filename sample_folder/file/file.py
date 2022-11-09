# zipファイルの解凍と圧縮
# 今回扱うzipファイル(気象庁 平年値ダウンロード) https://www.data.jma.go.jp/obd/stats/data/mdrr/normal/index.html
# Users/(ユーザ名)の直下にworkplaceフォルダを作成し、上記URLを開き、サイト下部のデータファイルから 台風(発生数・接近数・上陸数) ZIP:314KB をダウンロードする
# 以下のコードはcdコマンドでworkplaceに移動してから実行

import zipfile
files = zipfile.ZipFile('normal_typhoon.zip')
print(files.namelist())

print(files.extract('normal_typhoon/nml_typhoon.pdf'))
files.extractall()
files.close()

zip_file = zipfile.ZipFile('my_typhoon.zip', mode = 'w')
zip_file.write('normal_typhoon/nml_typhoon.pdf')
zip_file.close()
file = zipfile.ZipFile('my_typhoon.zip')
print(file.namelist())