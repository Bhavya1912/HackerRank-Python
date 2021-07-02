def split_and_join(line):
    # write your code here
    x= line.split()
    y="-".join(x)
    return y
if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result