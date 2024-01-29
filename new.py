import os
def Batch_Rename():
    location = "D:\DataStructure\Batch_Rename\image"
    dir_list = os.listdir(location)
    change = os.chdir(location)
    i = 1

    for filename in dir_list:
        name, ext = os.path.splitext(filename)
        name1 = "{:03d}.png".format(i)
        name2 = "a.png"
        os.rename(filename , name1)
        print(name,ext)
        i +=1

if __name__ == "__main__" :
    Batch_Rename()


    