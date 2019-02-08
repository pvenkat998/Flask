import os
path = "\\\\172.16.0.232\\CoffeeCrazy3\\その他\\受け渡し用\\20180703橋本さん受け渡し用\\加工済み会議資料"
print (os.listdir(path))
paths = [os.path.join(path, basename) for basename in path]
latest_file = max(paths, key=os.path.getctime)
