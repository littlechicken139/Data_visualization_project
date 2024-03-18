
import numpy as np
import pandas as pd
# 数据分析,  使用pandas导入csv再使用seaborn绘图
import matplotlib.pyplot as plt
# 2D绘图
import seaborn as sns
# 基于matplotlib进行高级封装的可视化库

original_data = pd.read_csv("Penguins.csv")
# 通过Pandas的read_csv函数，
# 将原始数据文件Penguins.csv里的数据内容，
# 解析为DataFrame(表格)并赋值给变量original_data
original_data.head()

print("\n=================================================\n")


cleaned_data = original_data.copy()
cleaned_data.head(10)
cleaned_data.info()

print("\n=================================================\n")

# 性别sex,物种species,岛屿island都是分类变量
# 可绘制饼图,看占比
cleaned_data['species'] = cleaned_data['species'].astype("category")
cleaned_data['sex'] = cleaned_data['sex'].astype("category")
cleaned_data['island'] = cleaned_data['island'].astype("category")
cleaned_data.info()

print("\n=================================================\n")

cleaned_data.query("culmen_length_mm.isna()")
cleaned_data.query("culmen_depth_mm.isna()")
cleaned_data.query("body_mass_g.isna()")

cleaned_data.drop(3, inplace=True)
cleaned_data.drop(339, inplace=True)
cleaned_data.query("sex.isna()")

cleaned_data["species"].value_counts()
cleaned_data["island"].value_counts()
cleaned_data["sex"].value_counts()

# cleaned_data['sex'] = cleaned_data['sex'].replace(".", np.nan)
cleaned_data["sex"].value_counts()
cleaned_data.describe()

# 可视化开始

# 选画盘颜色: 查palette参数
# (sns.set_palette("pastel"))
# (sns.set_palette("rocket"))
# (sns.set_palette("bone"))
(sns.set_palette("bright"))
cleaned_data

# 用groupby进行聚合运算, 先分组再数个数
cleaned_data["species"].value_counts()
# cleaned_data.groupby("species")["island"].count()

species_count = cleaned_data["species"].value_counts()
plt.pie(species_count, autopct='%.0f%%', labels=species_count.index)
plt.show()

island_count = cleaned_data["island"].value_counts()
plt.pie(island_count, autopct='%.0f%%', labels=island_count.index)
plt.show()

sex_count = cleaned_data['sex'].value_counts()
plt.pie(sex_count, labels=sex_count.index, autopct='%.0f%%')
plt.show()

# ===================

sns.countplot(cleaned_data, x="island", hue="species")
plt.show()

sns.pairplot(cleaned_data)
plt.show()

sns.pairplot(cleaned_data, hue='species')
plt.show()

sns.pairplot(cleaned_data, hue='species', kind='reg', plot_kws={'scatter_kws': {'alpha': 0.3}})
plt.show()

sns.pairplot(cleaned_data, hue='sex')
plt.show()