
import logging
import antlr4
from gen.seqLexer  import *
from gen.seqParser import *
from semseq import *



def main():
    #stream = antlr4.InputStream("((3 - 5) * 2)")
    #stream = antlr4.InputStream("(-2)^10")
    stream = antlr4.InputStream("4 N 5")
    #stream = antlr4.InputStream("3*2+1 N 7-3-2 ")

    #lexer = seqLexer(antlr4.StdinStream())

    lexer = seqLexer(stream)
    tokens = antlr4.CommonTokenStream(lexer)
    parser = seqParser(tokens)


    #tree = parser.expr()
    tree=parser.sequence()

    seq=SemSeq()
    #result=seq.visit(tree)

    walker=ParseTreeWalker()
    walker.walk(seq,tree)

#    a=seq.Stack.pop()
#    print(a)

    print(seq.Queue)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger=logging.getLogger(__name__)
    main()



