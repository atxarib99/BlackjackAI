import os
from PIL import Image
for filename in os.path.dirname(os.path.realpath(__file__)):
    print(filename[1:3])

