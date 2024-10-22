import pandas as pd
import glob

# 获取指定路径下所有 CSV 文件的路径
csv_files = glob.glob(r"C:\Users\PC307\Desktop\data_apex\气象数据\tongyu\*.csv")

# 读取并拼接所有 CSV 文件
dataframes = [pd.read_csv(file) for file in csv_files]
combined_dataframe = pd.concat(dataframes, ignore_index=True)

# 将拼接后的数据保存为新的 CSV 文件
combined_dataframe.to_csv(r"C:\Users\PC307\Desktop\data_apex\气象数据\tongyu\combined_file.csv", index=False)

print("CSV 文件拼接完成！")
