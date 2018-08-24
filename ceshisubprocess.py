import subprocess
import os

obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out,err = obj.communicate(input='print(1) \n')
print(out)

print(err)