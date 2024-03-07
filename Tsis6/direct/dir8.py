import os
if os.path.exists("copy1.txt"):
  os.remove("copy1.txt")
else:
  print("The file does not exist")