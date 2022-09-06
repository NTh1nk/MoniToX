from matplotlib import pyplot as plt
import numpy as np



os = {"Windows":3,"Mac":5}
osdata = []
osname = []
osname = os.items(os["Mac","Windows"])
osdata = os.items(os["Mac"])

 
fig = plt.figure(figsize =(10, 7))
plt.pie(osdata, labels = osname)
       
plt.show()  