import string
from matplotlib import pyplot as plt
import numpy as np



os = {"Windows":5,"Mac":5}
 
fig = plt.figure(figsize =(10, 7))

plt.pie(os.values(), labels = os.keys())
       
plt.show()  