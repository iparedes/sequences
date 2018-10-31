import logging
logger = logging.getLogger(__name__)

class TPos:

    def __init__(self,r=0,c=0):
        self.row=r
        self.col=c

    def Set(self,r,c):
        self.row=r
        self.col=c

    #   returns a new position that is s steps away in the specified direction
    def Go(self,dir,s=1):
        logger.info("Going %s:%d",dir,s)

        nr=self.row
        nc=self.col

        if dir=='N':
            nr=nr+s
        elif dir=='S':
            nr=nr-s
        elif dir=='W':
            nc=nc-s
        elif dir=='E':
            nc=nc+s
        else:
            logger.debug("TPos::go Unknown dir %s",dir)
            pass

        return TPos(nr,nc)

    #   Moves the pos s steps away in the specified direction
    def Move(self,dir,s=1):
        p=self.Go(dir,s)
        logger.debug("Moved from (r:%d,c:%d) to (r:%d,c:%d)",self.row,self.col,p.row,p.col)
        self.row=p.row
        self.col=p.col

    def getText(self):
        a="(r:"+str(self.row)+",c:"+str(self.col)+")"
        return a
