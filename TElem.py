import logging
logger = logging.getLogger(__name__)

from TPos import *


class TElem:
    def __init__(self,v,row,col):
        self.val=v
        self.pos=TPos(row,col)


    def Move(self,dir,steps):
        newpos=self.pos.Go(dir,steps)
        self.pos=newpos

    def Set(self,v):
        self.val=v

    def getText(self):
        a=str(self.val)+" at "+self.pos.getText()
        return a

