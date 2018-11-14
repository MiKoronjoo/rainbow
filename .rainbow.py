import math

def rgb(x) :
    period = 0.1
    return int(math.sin(period * float(x) + 0) * 127 + 128), \
           int(math.sin(period * float(x) + 2 * math.pi / 3) * 127 + 128), \
           int(math.sin(period * float(x) + 4 * math.pi / 3) * 127 + 128)

k = 0

while True :
    k += 1
    try :              # Reading lines
        line = input()
        for i in range(len(line)) :
            r, g, b = rgb(i+k)
            print("\033[38;2;%d;%d;%dm%c\033[0m"%(r, g, b, line[i]), end = '')

        print()        # Put '\n' --> Move cursor to new line

    except EOFError :  # End of file
        break
