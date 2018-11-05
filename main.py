
from TSeq import *
from TTable import *

def main():
    S=TSeq()

    while S.Context['i']<50:
        S.Walk()


    for e in S.Context['elems']:
        print(e.getText())

    t=TTable(S.Context['elems'])
    #t.plot()
    t.grid()
    pass


if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)
    logging.basicConfig(level=logging.CRITICAL)
    logger=logging.getLogger(__name__)
    main()



