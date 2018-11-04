import logging
logger = logging.getLogger(__name__)

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
        from matplotlib import rcParams
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

    def isPrime(n):
        return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
