import os

for p in os.environ["PATH"].split(";"):
    print(p)
