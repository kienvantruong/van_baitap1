#https://ophim17.cc/phim/to-chat-anh-hung-phan-1
import requests
import json
# import yt_dlp
import subprocess
ten = 1
print("hãy đưa link của phim mà bạn muốn xem:")
a = input("link của bạn là:")

# print(ophim_response.text)
# link_api = 'https://ophim1.com/phim/to-chat-anh-hung-phan-1'
# link_api = 'https://ophim17.cc/phim/huong-vi-cua-bien-phan-2'
link_api = a
# print(link_api[23:])
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=800000,RESOLUTION=1920x1080
# 3000k/hls/mixed.m3u8
#https://vip.opstream16.com/20250519/42992_c5475a75/index/hls/mixed.m3u8
#https://vip.opstream16.com/3000k/hls/mixed.m3u8
#https://vip.opstream16.com/20250519/42992_c5475a75/3000k/hls/mixed.m3u8

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

# print(res)

# print(link_api[res:])

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
# print(linkload)
ophim_response = requests.get(linkload)
# print(ophim_response.text)
# print("hãy đưa link của phim mà bạn muốn xem:")
ophim_data = json.loads(ophim_response.text)
movie_test = ophim_data["movie"]["episode_current"]
moonbeo = int(input("bạn muốn xem tập:"))
so_tap = moonbeo - 1
movie_index_link = ophim_data["episodes"][0]["server_data"][so_tap]["link_m3u8"]

movie_index_reponse = requests.get(movie_index_link)
# print(movie_index_link)
movie_index_link = movie_index_link[:-10] + "3000k/hls/mixed.m3u8"
print(movie_index_link)
print("Vui lòng đợi trong giây lát...")
# Method 1: Using subprocess.run (recommended for Python 3.5+)
result = subprocess.run(['yt-dlp.exe', movie_index_link, '-o ' +a+ '.mp4'], capture_output=True, text=True)
print(result.stdout)  # Print the output of the executable
print(result.returncode)  # Print the return code of the executable

# https://ophim17.cc/phim/sat-thu-ve-vuon