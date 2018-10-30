'''
various file reading techniques
'''

import json

def read_file_1(filename):
    file = open(filename, 'rt')
    for line in file.readlines(): print(line, end='')
    file.close()

def read_file_2(filename):
    file = open(filename, 'rt')
    # the 'file' object itself is iterable; no need to call .readlines()
    for line in file: print(line, end='')
    file.close()

def read_file_3(filename):
    # when you exit the 'with' block, file.close() is called automatically
    with open(filename) as file:
        for line in file:
            print(line, end = '')

def csv2json(filename):
    with open(filename) as file:
        headers = file.readline().strip().split(',')
        lines = file.readlines()

        data = [dict(zip(headers, line.strip().split(','))) 
            for line in lines]
        
        out_filename = filename[:-4] + '.json'
        with open(out_filename, 'w') as outfile:
            json.dump(data, outfile, indent=3)

def main():
    filename = 'people.csv'
    # read_file_3(filename)
    csv2json(filename)
if __name__=='__main__': main()