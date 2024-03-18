数据可视化小项目 -"帕默群岛上企鹅样本"
=====

## 一.项目目标
1. 对数据集进行: 读取-评估-清理-可视化
2. 此数据分析报告的目的是对帕默群岛上企鹅样本的相关变量进行可视化，
3. 从而探索和分析种类、性别、所在岛屿等因素，
4. 与企鹅的身体属性，包括体重、嘴峰长度和深度、鳍的长度，之间的关系。


## 二.数据

1. 原始数据在文件`Penguins.csv`,包括334个收集自南极洲帕尔默群岛的3个岛屿上的企鹅样本，以及企鹅相关属性数据，包括种类名、所在岛、嘴峰长度、嘴峰深度、鳍长度、体重、性别。


2. 文件中`Penguins.csv`每列的含义：
   - species：企鹅的种类
   - island：企鹅所在岛
   - culmen_length_mm：企鹅嘴峰的长度（单位为毫米）
   - culmen_depth_mm：企鹅嘴峰的深度（单位为毫米）
   - flipper_length_mm：企鹅鳍的长度（单位为毫米）
   - body_mass_g：企鹅体重（单位为克）
   - sex：企鹅性别

3. 变量的类型与绘图规划
   1. 分类变量:species,island,sex
      1. 用饼图看比例pie
   2. 数值变量:剩下的那四个
      1. 直方图, 密度图, 箱型图, 小提琴图, 散点图, 
      2. 成对图(pairplot)

## 三.用到的库与方法

### 1. pandas 库的方法
1. pd.read_csv()
   1. 作用：用于读取CSV文件，并将其解析为pandas DataFrame对象。
   2. 参数：通常包括文件路径、分隔符、列名等。
   3. 返回值：返回一个pandas DataFrame对象，包含CSV文件中的数据。
2. DataFrame.head()
   1. 作用：返回DataFrame的前几行，默认是前5行。
   2. 参数：可以指定要返回的行数。
   3. 返回值：返回一个包含指定行数的新DataFrame。
3. DataFrame.info()
   1. 作用：输出DataFrame的简短摘要，包括索引、列名、数据类型、非空值的数量以及内存使用情况。
   2. 参数：无。
   3. 返回值：无返回值，直接打印摘要信息。
4. DataFrame.astype()
   1. 作用：将DataFrame中的列转换为指定的数据类型。
   2. 参数：要转换的列名和对应的数据类型。
   3. 返回值：返回一个新的DataFrame，其中指定的列已被转换为新的数据类型。
5. DataFrame.query()
   1. 作用：使用字符串表达式对DataFrame进行过滤查询。
   2. 参数：一个字符串表达式，用于过滤行。
   3. 返回值：返回一个新的DataFrame，包含满足查询条件的行。
6. DataFrame.drop()
   1. 作用：删除DataFrame中的指定行或列。
   2. 参数：要删除的行或列的标签或索引，以及一个指示是删除行还是列的参数。
   3. 返回值：返回一个新的DataFrame，其中指定的行或列已被删除。
7. Series.value_counts()
   1. 作用：返回Series中唯一值的计数，按计数的降序排列。
   2. 参数：可以包括是否排除NaN值、排序方式等。
   3. 返回值：返回一个新的Series，索引是唯一值，值是对应的计数。
8. DataFrame.describe()
   1. 作用：生成DataFrame的描述性统计信息，
      1. 包括计数、均值、标准差、最小值、四分位数、最大值等。
   2. 参数：可以指定要包含哪些统计量。
   3. 返回值：返回一个新的DataFrame，包含描述性统计信息。
9. DataFrame.groupby()
   1. 作用：根据一个或多个列对DataFrame进行分组，并返回一个GroupBy对象，用于进一步聚合或转换操作。
   2. 参数：用于分组的列名或列名列表。
   3. 返回值：返回一个GroupBy对象。
10. isna() 
    1. 是 pandas Series 的一个方法，用于生成一个布尔序列，
    2. 其中的每个元素表示原始序列中相应位置的元素是否为 NaN

### matplotlib/seaborn 库的方法
1. seaborn.set_palette()
   1. 作用：设置seaborn的调色板，用于后续的绘图操作。
   2. 参数：调色板的名称或列表。
   3. 返回值：无返回值，但会影响后续绘图的颜色。
2. matplotlib.pyplot.pie()
   1. 作用：绘制饼图，用于展示数据的比例分布。
   2. 参数：包括数据、标签、颜色、百分比格式等。
   3. 返回值：返回一个包含饼图元素的列表。
3. matplotlib.pyplot.show()
   > seaborn是基于matplotlib的高级封装库
   1. 作用：显示使用matplotlib绘制的图形。
   2. 参数：无。
   3. 返回值：无返回值，但会弹出一个窗口显示图形。
   seaborn.countplot()、seaborn.pairplot()等，这些函数在原始问题中已有提及，但并未包含在分组介绍中。

## 运行效果示例
![可视化项目图片实例.png](%BF%C9%CA%D3%BB%AF%CF%EE%C4%BF%CD%BC%C6%AC%CA%B5%C0%FD.png)![可视化项目图片实例.png](%BF%C9%CA%D3%BB%AF%CF%EE%C4%BF%CD%BC%C6%AC%CA%B5%C0%FD.png)
见png的截图

