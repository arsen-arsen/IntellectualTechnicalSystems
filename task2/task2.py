def triangle(a):
    for i in range(a, -1, -1):
        print(' '*i + '*'*((a - i)*2 + 1))

def hDistance(h1, h2) -> float:
    if (len(h1) != len(h2)):
        return -1
    else:
        sum = 0
        for i in range(len(h1)):
            sum += (h1[i] - h2[i])**2
        return sum**0.5
def readH(path, separator = ','):
    f = open(path, "r")
    line = f.readline()
    if(not line):
        print('File is empty.')
        return -1
    hist = [int(x) for x in line.split(separator)]
    f.close()
    return hist
def writeH(path, h, separator = ','):
    f = open(path, "w")

    line = [str(x) for x in h]
    line = separator.join(line)
    f.write(line)
    f.close()
if __name__ == '__main__':
    print('triangle(3):')
    triangle(3)
    print('\n\n') 
    print('hDistance([1,2,3], [0,0,0])^2:', hDistance([1,2,3], [0,0,0])**2, '\n\n')
    path = "D:\\text.txt"
    print('Read histogram:', readH(path))
    t_hist = [0,3,2,1]
    print('Wrote as:', t_hist)
    writeH(path, t_hist)
    print('Read as:', readH(path)) 
