# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 14:05:40 2017

@author: Nzix
"""

def matrix_chain(matrixs):
    calculation = []
    split = []
    for i in range(0,len(matrixs)):
        calculation.append([-1]*len(matrixs))
        split.append([-1]*len(matrixs))
        calculation[i][i] = 0
        split[i][i] = 0
        
    for i in range(1,len(matrixs)):
        for j in range(0,len(matrixs)):
            x = j
            y = j + i
            if y > len(matrixs)-1:
                break
        
            least = matrixs[x][0] * matrixs[x][1] * matrixs[y][1] + calculation[x+1][y]
            choice = x + 1
            for z in range(x+1,y):
                if matrixs[z][1] != matrixs[z+1][0]:
                    print "unvalid matrix chain"
                    return
                do = matrixs[x][0] * matrixs[z][1] * matrixs[y][1] + calculation[x][z] + calculation[z+1][y]
                if do < least:
                    least = do
                    choice = z + 1
                    
            calculation[x][y] = least
            split[x][y] = choice
        
    return calculation[0][len(matrixs)-1]


def main():
    example = [[3,7],[7,8],[8,5],[5,12],[12,10]]
    print example    
    print matrix_chain(example)
    
if __name__ == "__main__":
    main()