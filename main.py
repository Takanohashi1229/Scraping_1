from os import makedirs, path
from time import sleep
from urllib.request import urlretrieve

ids = [
    ["ps6vr70000010d6y-att", "2023r05h_ap_"],
    ["gmcbt80000008smf-att", "2022r04a_ap_"],
    ["gmcbt80000009sgk-att", "2022r04h_ap_"],
    ["gmcbt8000000apad-att", "2021r03a_ap_"],
    ["gmcbt8000000d5ru-att", "2021r03h_ap_"],
    ["gmcbt8000000d05l-att", "2020r02o_ap_"],
    ["gmcbt8000000dict-att", "2019r01a_ap_"],
    ["gmcbt8000000ddiw-att", "2019h31h_ap_"],
    ["gmcbt8000000f01f-att", "2018h30a_ap_"],
    ["gmcbt8000000fabr-att", "2018h30h_ap_"],
    ["gmcbt8000000fqpm-att", "2017h29a_ap_"],
    ["gmcbt8000000fzx1-att", "2017h29h_ap_"],
    ["gmcbt8000000g6fw-att", "2016h28a_ap_"],
    ["gmcbt8000000gn5o-att", "2016h28h_ap_"],
    ["gmcbt8000000gxj0-att", "2015h27a_ap_"],
    ["ug65p90000000f52-att", "2015h27h_ap_"],
    ["ug65p90000000ye5-att", "2014h26a_ap_"],
    ["ug65p90000001dzu-att", "2014h26h_ap_"],
    ["ug65p900000027za-att", "2013h25a_ap_"],
    ["ug65p90000002e6g-att", "2013h25h_ap_"],
    ["ug65p90000002h5m-att", "2012h24a_ap_"],
    ["ug65p900000038er-att", "2012h24h_ap_"],
    ["ug65p90000003ojp-att", "2011h23a_ap_"],
    ["ug65p90000003ya2-att", "2011h23tokubetsu_ap_"],
    ["ug65p90000004d6f-att", "2010h22a_ap_"],
    ["ug65p90000004n2z-att", "2010h22h_ap_"],
    ["gmcbt8000000f3yi-att", "2009h21a_ap_"],
    ["ug65p90000009bhl-att", "2009h21h_ap_"]]

fileTypes = [["am_qs", "am_ans", "pm_qs", "pm_ans"],
             ["AM_問題", "AM_解答", "PM_問題", "PM_解答"]]

baseUrl = "https://www.ipa.go.jp/shiken/mondai-kaiotu/"

for id in ids:
    # 季節を特定する
    filetmp = (id[1])[7]
    if filetmp == "h":
        filetmp = "春季"
    elif filetmp == "a":
        filetmp = "秋季"
    else:
        filetmp = "特別"
    createDir = f"./ap/{(id[1])[0:4]}/{filetmp}"
    # ディレクトリが存在するか判定
    if not path.exists(createDir):
        makedirs(createDir)

    for i, fileType in enumerate(fileTypes[0]):
        url = f"{baseUrl}{id[0]}/{id[1]}{fileType}.pdf"
        filen = f"{(id[1])[0:4]}{filetmp}-{fileTypes[1][i]}.pdf"
        urlretrieve(url, f"{createDir}/{filen}")
        print(f"{filen} saved successflly.")
        sleep(3)
print("ok")

