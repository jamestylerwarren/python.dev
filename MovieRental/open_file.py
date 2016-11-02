# ---- how to open and write/read to a file --- #

#always need to close a file that is opened

#open file and write ('w'), read ('r'), etc to a file
#open construct automatically closes file, no need for f.close
with open('my_file.txt', 'r') as f:
    #f.write("hello world")
    print(f.readline())