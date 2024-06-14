import os
import gc  # Thêm thư viện gc để giải phóng bộ nhớ

# Đường dẫn tới thư mục cần đọc
directory = 'Folder_Files'

# Lấy danh sách tất cả các tệp .txt trong thư mục và các thư mục con
txt_files = []
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.csv'):
            txt_files.append(os.path.join(root, file))

# Sắp xếp theo thứ tự bảng chữ cái
txt_files_sorted = sorted(txt_files)

# In danh sách các tệp .txt
for txt_file in txt_files_sorted:
    print(txt_file)

# Đếm số lượng tệp đã đọc
# files_read = 0

# # Đọc và in nội dung của từng tệp .txt
# for txt_file in txt_files_sorted:
#     file_path = txt_file
#     with open(file_path, 'r') as f:
#         content = f.read()
#         # print(f"Contents of {txt_file}:\n{content}\n")
    
#     # Tăng số lượng tệp đã đọc
#     files_read += 1
    
#     # Giải phóng bộ nhớ mỗi khi đã đọc 100 tệp
#     if files_read % 100 == 0:
#         gc.collect()
