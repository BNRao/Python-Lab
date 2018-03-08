from random import randint
import numpy as np
Z = np.random.randint(0,25, size=(15))
print("Array: %s"   %Z)
print("Frequent item in the list:")
print(np.bincount(Z).argmax())