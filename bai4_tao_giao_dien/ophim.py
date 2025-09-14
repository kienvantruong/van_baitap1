# if you don't 
from tkinter import *
from tkinter import filedialog
import sys
import time
import requests
import hashlib
import json
import subprocess
import os
import re as recuatui
import shutil
import fnmatch
import math

# # print("1= có , 0= không")
# moonbeo2 = int(input("bạn muốn xem tất cả?"))
# # if moonbeo2 == 1: 
# # moonbeo = int(input("bạn muốn xem tập:"))
# so_tap = moonbeo2 - 1
# hoi = input("bạn muốn tải hết? 0= có ,1= không")
# if hoi == "1":
# gamemode_0 = input("bạn muốn xem tất cả? 1=có 2=không:")
jun_dep_trai = 0
abc = 0

# so_segment = 0
tong_so_segments2 = 0.0
aaa= 0

print("Vui lòng đợi trong giây lát...")
# time.sleep(5.0)

# Window
window = Tk()
window.geometry("600x200")
window.resizable(width=False, height=False)
window.title("OphimDownload")

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)
window.columnconfigure(2, weight=1)
label2 = Label(text="Ophim Video Downloader", font=("Arial", 15))
label2.grid(column=1, row=0, sticky="ew")

label4 = Label(text="Link Phim")
label4.grid(row=1, column=0)
inputLinkPhim = Entry()
inputLinkPhim.grid(row=1, column=1, sticky='ew')
input_test = inputLinkPhim
labelSaveTo = Label(text="Save to")
labelSaveTo.grid(row=2, column=0)
inputSaveTo = Entry()
inputSaveTo.grid(row=2,column=1,sticky='ew')

# Button
def runDownload():
    linkPhimText = inputSaveTo.get()
    # label2.config(text=linkPhimText)
    folder_path = filedialog.askdirectory()    
    if folder_path:
        print("Selected folder:", folder_path) # You can store the path in a variable or label
        print(input_test)
    inputSaveTo.insert(0,folder_path)
    
    return folder_path
browse = Button(text="Browse",command=runDownload)
browse.grid(row=2,column=3,sticky="e")
folder_path = runDownload
def browse_folder(): 
    so_segment = 0
    jun_test = 0.0
    ads = [
    "28fed2d8ad9fe2ddeb62dd3481daab6e",
    "bda8130f048c83d4c57cb963f4de029c",
    "9624d8d6a153184fbd2c719a879ce8e2",
    "26f379738a0f84cffe9b18b2f5d0d375",
    "303ac1a09d8991ef1478c4ca07640c5b",
    "073af4b992430092b0431207936fa326",
    "4bd3076e7149875817eb151eef791b02",
    "e0aefabf9b96516472db5df4700341b3",
    "87ad3731e00df9cb9cf1c0a8b34f26de",
    "87ef22878816c4c996b7deae4970f12a",
    "ff6f4af84dc1c454d44d75c9d5e947bd",
    "ca55fcc163273e0c0fb3afd77b0e88a6",
    "924dd874998ef514acfd6c3264a875bb",
    "1e262fceba5921de1c07b350fa5a5928",
    "c57574cfd8633fb9cdc2d84a9dc0701d",
    "9a49678d9c94b7aea4a44acf94486673",
    "3ca454309c0ad67090ab6c82c9f6e866"]
    print("hãy đưa link của phim mà bạn muốn xem:")
    a = inputLinkPhim.get()

    link_api = a


    s = a
    k = '/'
    v = 0

    res = -1
    for i in range(len(s)):
        if s[i] == k:
            res = i+1
            v +=1
            if v == 4:
                break
    tenphim = link_api[res:]
    api = 'https://ophim1.com/phim/${slug}'

    d = 'https://ophim1.com/phim/${slug}'
    k = '/'
    b = 0

    re = -1
    for i in range(len(d)):
        if d[i] == k:
            re = i+1
            b +=1
            if b == 4:
                break       
    # print(api[0:re])

    linkphim = api[0:re]
    linkload = linkphim + tenphim

    ophim_response = requests.get(linkload)

    ophim_data = json.loads(ophim_response.text)
    movie_test = ophim_data["movie"]["episode_current"]    
    
    ophim_data = json.loads(ophim_response.text)
    movie_test = ophim_data["movie"]["episode_current"]
        
    movie_index_link = ophim_data["episodes"][0]["server_data"]
    for tap in movie_index_link :
    
    # movie_index_reponse = requests.get(tap['link_m3u8'])
    
# print(movie_index_link)
        movie_index_link = tap['link_m3u8'][:-10] + "3000k/hls/mixed.m3u8"
        # print(movie_index_link)
    # https://vip.opstream14.com/20220805/19581_ec172391/3000k/hls/mixed.m3u8
    # https://vip.opstream14.com/20220805/19581_ec172391/3000k/hls/e3d02b634432ed789dd1ffbf944c862c.ts
        noi_dung = requests.get(movie_index_link)
        lines = recuatui.split(r'\n', noi_dung.text)
        moon_map_dit = 0

    #phim có 1568 segments      100%
    #down 20 segment   sss         2%
        tong_so_segments = 0
        for dong in lines:
            if dong != '' and dong[0] != '#':
                tong_so_segments += 1

        # print("chạy tới dòng 155")
        for dong in lines:
            # for test in lines:
            #     if test != '' and test[0] != '#':
            #         jun_dep_trai += 1
            # jun = 100 / jun_dep_trai
            if dong == '':
                break
            elif dong[0] != '#':
                # print(dong)
                moon_map_dit +=1
                        # 1337
                url = movie_index_link[:-10] + dong
                r = requests.get(url, allow_redirects=True)
                open(str(moon_map_dit) + "_" + dong, 'wb').write(r.content)
                # print(moon_map_dit)
                    # for file in file_name2:
                with open(str(moon_map_dit) + "_"+ dong, 'rb') as file_obj:
                    file_contents = file_obj.read()
                
                    md5_hash = hashlib.md5(file_contents).hexdigest()
                    
                for moon_bi_ngu in ads:
                    if moon_bi_ngu == md5_hash:
                        print("\rĐã phát hiện quảng cáo:" + dong)
                        os.remove(str(moon_map_dit) + "_" + dong)
                so_segment = so_segment + 1
                tong_so_segments2 = so_segment * 100 / tong_so_segments
                bbb = math.ceil(tong_so_segments2)
                # os.system('cls')
                if bbb < 10:
                    print("tìm kiếm file |",end="")
                elif bbb >= 10 and bbb < 25:
                    print("kiểm tra file |",end="")
                elif bbb >= 25 and bbb < 51:
                    print("kiểm tra nội dung file |",end="")
                elif bbb >= 51 and bbb < 60:
                    print("kiểm tra thứ tự |",end="")
                elif bbb >= 60 and bbb < 93:
                    print("đang điều chỉnh file |",end="")
                elif bbb >= 93 and bbb < 100:
                    print("đang tạo file |",end="")
                for moon_bien_dang in range(bbb):
                    print("#",end="")    
                # print("|" + str(math.ceil(tong_so_segments2)) + "%")
                # print("chạy tới dòng 200")
                print("\r| {}% :".format(math.ceil(tong_so_segments2)), end='')
                sys.stdout.flush()
                
                jun_test += tong_so_segments2
                if tong_so_segments2 == 100.0:
                    print("\rHoàn thành 100/100 :")
                    tong_so_segments2 = 0.0
                    all_files = list()
                    for f in os.listdir("."):
                        if os.path.isfile(f) and f.format(".ts"):
                            all_files.append(f)
                    sorted_ts = list()
                    idx = 1
                    # print("chạy tới dòng 215")
                    # lặp cho tới khi all_files ko còn phần tử nào hết
                    while len(all_files) > 0:
                        # vòng lặp tất cả phần tử trong all_files
                        for ts in all_files:
                            # tách tên file theo ký tự _
                            # [SỐ]_[tên].ts
                            # if ts.split("_")[0] != str(idx) and ts.split("_")[0] == :
                                # pass    
                            if ts.split("_")[0] == str(idx):
                                # thêm vào danh sách sorted_ts
                                sorted_ts.append(ts)
                                # xóa khỏi danh sách all_files, xóa tới khi không còn phần tử để dừng vòng lặp
                                all_files.remove(ts)
                                # tăng idx để tiếp tục tìm
                        idx = idx + 1
                            # number_list = ts.split("_")[0]
                    # print("chạy tới dòng 229") 
                                
                    output_file = inputSaveTo.get()+"/output.mp4"
                    with open(output_file, "wb") as outfile:
                        for ts_file in sorted_ts:
                            with open(ts_file, "rb") as infile:
                                shutil.copyfileobj(infile, outfile)
                    # print("chạy tới dòng 325")
    
btnDownload = Button(text="Download",command=browse_folder)
btnDownload.grid(row=3,column=1, sticky='e')

window.mainloop()
