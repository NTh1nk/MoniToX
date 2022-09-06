import string
from matplotlib import pyplot as plt
import numpy as np


keys = ["Windows", "Mac "]
os = {"Windows":3,"Mac":5}
osname = []
osdata = [2,5]



 
fig = plt.figure(figsize =(10, 7))

plt.pie(osdata, labels = keys)
       
plt.show()  