import os
import shutil

# Đường dẫn tới tệp gốc
source_file = './Folder_Files/CSV_Name_01.csv'

# Đường dẫn tới thư mục lưu các bản sao (có thể thay đổi)
destination_dir = './Folder_Files/folder_'

# Số lượng bản sao cần tạo
num_copies = 100

# Tạo các bản sao
for y in range(1, num_copies + 1):
    for i in range(1, num_copies + 1):
        destination_file = os.path.join(destination_dir + f"{y}", f'CSV_Copy_{i}.csv')
        shutil.copyfile(source_file, destination_file)
        print(f"Created copy: {destination_file}")