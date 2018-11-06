import logging
logger = logging.getLogger(__name__)
import math

from matplotlib import rcParams
import matplotlib.patches as patches

import matplotlib.pyplot as plt
import numpy as np


class TTable:

    def __init__(self,elems):


        row_coords=list(map(lambda x: x.pos.row, elems))
        col_coords=list(map(lambda x: x.pos.col, elems))
        min_row=min(row_coords)
        max_row=max(row_coords)
        min_col=min(col_coords)
        max_col=max(col_coords)

        self.rows=max_row-min_row+1
        self.cols=max_col-min_col+1

        self.Elems=[]
        elems.pop(0)
        for e in elems:
            r=e.pos.row-min_row
            c=e.pos.col-min_col
            val=e.val
            self.Elems.append((r,c,val))

        self.M = []
        for r in range(0, self.rows):
            row = []
            for c in range(0, self.cols):
                row.append("")
            self.M.append(row)

        for e in elems:
            r=e.pos.row-min_row
            c=e.pos.col-min_col
            val=e.val
            self.M[r][c]=val


    def plot(self):
        rcParams['font.family']='serif'
        rcParams['font.size']=10

        m = self.rows
        n = self.cols

        plt.figure(figsize=(n+1,m+1))
        for krow, row in enumerate(self.M):
            for kcol, num in enumerate(row):

                plt.text(10*kcol +15,10*krow +15, num,
                         horizontalalignment='center',
                         verticalalignment='center')

        #plt.axis([0,10*(n +1),10*(m +1),0])
        plt.xticks(np.linspace(0,10*(n +1), n +2),[])
        plt.yticks(np.linspace(0,10*(m +1), m +2),[])
        plt.grid(linestyle="solid")
        plt.savefig("Table.png", dpi=300)
        plt.show()

        pass

    def grid(self):
        rcParams['font.family']='serif'
        rcParams['font.size']=10
        self.figura=plt.figure(1,figsize=(8,8))
        self.axis=self.figura.add_subplot(111)

        rows = self.rows
        cols = self.cols
        plt.axis([0,cols,rows,0])

        self.side=10
        self.margin=15

        for e in self.Elems:
            self.write(e)

        a=np.linspace(0,cols,cols,[])
        plt.xticks(a," ")
        plt.yticks(np.linspace(0,rows,rows,[])," ")
        plt.grid(linestyle="solid")
        plt.show()


    def write(self,rcv):
        row=rcv[0]
        col=rcv[1]
        v=rcv[2]

        x=(col+1)/2
        y=(row+1)/2

        x=col+0.5
        y=row+0.5

        #plt.text(x,y,v,horizontalalignment='center',verticalalignment='center')

        if self.isPrime(v):
            rect = patches.Rectangle((col,row),1,1,linewidth=1,edgecolor='r',facecolor='red')
            self.axis.add_patch(rect)

    def isPrime(self,n):
        if n % 2 == 0 and n > 2:
            return False
        return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
