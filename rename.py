import os

def rename_files(folder_path, file_name:str):
    # 獲取資料夾內所有檔案的絕對路徑
    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # 對檔案進行重新命名
    counter = 0
    for file_path in files:
        # 獲取檔案的目錄和原始檔案名稱
        directory, filename = os.path.split(file_path)
        
        # 構造新的檔案名稱
        new_filename = f"{file_name}{counter:02d}{os.path.splitext(filename)[1]}"
        new_file_path = os.path.join(directory, new_filename)
        
        # 重新命名檔案
        os.rename(file_path, new_file_path)
        
        # 更新計數器
        counter += 1
    
    print(f"已成功重新命名{counter}個檔案。")

# 使用示例
rename_files("C:/Project/Yolo5/yolov5/dataset/smoking/images/train", 'smoking')
