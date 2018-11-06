
from TSeq import *
from TTable import *

def main():

    #stream = antlr4.InputStream("(5*2)N[I:2]SE")
    #stream = antlr4.InputStream("(2*1)N[Z:2]")
    #stream = antlr4.InputStream("[Z]N:2W:1")
    #stream = antlr4.InputStream("3[L]N:2W:1")
    # The cube
    #stream = antlr4.InputStream("{i}((l+1)/2)E;(l/2)N;((l+1)/2)W;(l/2)S;")
    # The pyramid
    stream = antlr4.InputStream("{j/2+1} [((l-1)^2)+1]S,(l)[(l^2)+1]EW:(j/2);")
    #stream = antlr4.InputStream("{j} N,E;")

    S=TSeq(stream)

    while S.Context['i']<20000:
        S.Walk()


    for e in S.Context['elems']:
        print(e.getText())

    t=TTable(S.Context['elems'])
    t.grid()
    pass


if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)
    logging.basicConfig(level=logging.INFO)
    logger=logging.getLogger(__name__)
    main()



