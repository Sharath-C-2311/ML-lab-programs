




import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

d = pd.read_csv('ToyotaCorolla.csv')

x=d["KM"]
y=d["Weight"]
z=d["Price"]

# 3d surface
a = plt.axes(projection="3d")
a.plot_trisurf(x,y,z)
plt.show()



#3
#Visualize the n-dimensional data using contour plots.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("ToyotaCorolla.csv")

#contour plot
x = data['KM']
y = data['Weight']
z = data['Price']

plt.tricontourf(x, y, z, levels=20, cmap='jet')
plt.colorbar(label='Price')
plt.xlabel('KM')
plt.ylabel('Weight')
plt.title('Contour Plot')
plt.show()





#4
#Visualize the n-dimensional data using heat-map.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("ToyotaCorolla.csv")

#heat map
sns.heatmap(data[["Price","KM","Doors", "Weight"]].corr(),cmap='jet',annot=True)
plt.show()


#5
# Visualize the n-dimensional data using Box-plot.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("ToyotaCorolla.csv")

#box plot
plt.title('Box Plot')
plt.boxplot([data["Price"],data["HP"],data["KM"]])

plt.xticks([1,2,3],["Price","HP","KM"])

plt.show()



