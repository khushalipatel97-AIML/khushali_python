
try:
    with open("fileHandling.txt") as f1:
        with open("fileHandling1.txt", "w") as f2:
            for i in f1:
                f2.write(i)
except:
    print("File not found")
# else:
#     f1.close()


# try:
#     with open("fileHandling.txt") as f1:
#         with open("output.txt", "w") as f2:
#             for i in f1:
#                 f2.write(i)
# except:
#     print("File not found")