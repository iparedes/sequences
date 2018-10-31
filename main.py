
from TSeq import *




def main():
    S=TSeq()

    while S.Context['i']<20:
        S.Walk()

    l=S.Context['elems']
    for elem in l:
        a=elem.getText()
        print(a)

    row_coords=list(map(lambda x: x.pos.row, l))
    col_coords=list(map(lambda x: x.pos.col, l))
    min_row=min(row_coords)
    max_row=max(row_coords)
    min_col=min(col_coords)
    max_col=max(col_coords)

    pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    #logging.basicConfig(level=logging.INFO)
    logger=logging.getLogger(__name__)
    main()



