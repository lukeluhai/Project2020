import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
df = pd.DataFrame(np.random.randn(10,4),columns=['a','b','c','d'])
sty = df.style
print(sty,type(sty))
# 查看样式类型
print(df)
