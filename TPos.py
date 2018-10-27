import logging
logger = logging.getLogger(__name__)

class TPos:
    row=0
    col=0


    def __init__(self,r=0,c=0):
        self.row=r
        self.col=c

    def Set(self,r,c):
        self.row=r
        self.col=c

    #   returns a new position that is s steps away in the specified direction
    def Go(self,dir,s=1):
        nr=self.row
        nc=self.col

        if dir=='N':
            nr=nr+s
        elif dir=='S':
            nr=nr-1
        elif dir=='W':
            nc=nc-1
        elif dir=='E':
            nc=nc+1
        else:
            logger.debug("TPos::go Unknown dir %s",dir)
            pass

        return TPos(nr,nc)

    def getText(self):
        a="(r:"+str(self.row)+",c:"+str(self.col)+")"
        return a
