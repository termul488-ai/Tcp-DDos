import os

print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("pip install django")
    os.system("pip install fade")
elif c == "1":
    os.system("pip3 install django")
    os.system("pip3 install fade")
print("Done.")
