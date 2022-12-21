class classifier:
    def __init__(self, path):
        self.objects = self.__readObjects__(path)
    def __readObjects__(self, path):
        out = []
        f = open(path, "r")
        for line in f.readlines():
            if (not line):
                print('File is empty. Skipping.')
                continue
            name = line.split(':')[0]
            hist = [int(x) for x in (line.split(':')[1]).split(',')]
            out.append([name, hist])
        f.close()
        return out
    def __hdist__(self, h1, h2) -> float:
        if (len(h1) != len(h2)):
            print('Cannot calculate distance.')
            return -1
        summ = 0
        for i in range(len(h1)):
            summ += (h1[i] - h2[i]) ** 2
        return summ ** 0.5
    def getType(self, hist):
        dist = []
        for obj in self.objects:
            dist.append([self.__hdist__(hist, obj[1]), obj[0]])
        return min(dist)[1]
if __name__ == '__main__':
    clsr = classifier("D:/text.txt")
    print(clsr.getType([1, 2, 3]))
