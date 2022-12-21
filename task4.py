from git import Repo
Def_Folder = "D:\\testfolder"
def MyGenerator():
    start = 0
    while True:
        yield start
        start += 2
def print_even(n):
    x = MyGenerator()
    for i in range(n):
        print(next(x))
if __name__ == '__main__':
    with open("in.txt", "r") as infile:
        lines = in_file.readlines()
        infile.close()
        for line in lines:
            part = line.split('/')
            try:
                Repo.clone_from(line, Def_Folder + "\\" + part[-1])
                line = "OK........." + line + "\n"
            except:
                line = "FAIL........." + line + "\n"
        with open("out.txt", "w") as outfile:
            outfile.writelines(lines)
            outfile.close()
