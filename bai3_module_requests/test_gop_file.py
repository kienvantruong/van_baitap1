import shutil
import os

# lay tat ca file trong thu muc
# all_files = [f for f in os.listdir(".") if os.path.isfile(f)]
all_files = list()
for f in os.listdir("."):
    if os.path.isfile(f) and f.format(".ts"):
        all_files.append(f)
    
sorted_ts = list()
idx = 1

# lặp cho tới khi all_files ko còn phần tử nào hết
while len(all_files) > 0:
    # vòng lặp tất cả phần tử trong all_files
    for ts in all_files:
        # tách tên file theo ký tự _
        # [SỐ]_[tên].ts
        if ts.split("_")[0] == str(idx):
            # thêm vào danh sách sorted_ts
            sorted_ts.append(ts)
            # xóa khỏi danh sách all_files, xóa tới khi không còn phần tử để dừng vòng lặp
            all_files.remove(ts)
    # tăng idx để tiếp tục tìm
    idx = idx + 1
            

output_file = "output.mp4"
with open(output_file, "wb") as outfile:
    for ts_file in sorted_ts:
        with open(ts_file, "rb") as infile:
            shutil.copyfileobj(infile, outfile)
