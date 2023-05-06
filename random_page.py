import os
import random
   
def random_file():
  files = [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser("./")) for f in fn if f.endswith("md")]
  print(random.choice(files))

if __name__ == "__main__":
    random_file()
