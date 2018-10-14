import os
import time

start = time.time()

a = os.system("th eval.lua -model model_id1-501-1448236541.t7_cpu.t7 "
    "-image_folder img -num_images 5 -gpuid -1")

print ("Time taken for 5 images -> " + str(time.time() - start) + "seconds.")

