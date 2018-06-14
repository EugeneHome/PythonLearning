import wx
import os
import random
from itertools import chain

class Frame(wx.Frame):
    def __init__(self,title,size=4,winScore=2048):
        super(Frame,self).__init__(None,-1,title,
                style=wx.DEFAULT_FRAME_STYLE^wx.MAXIMIZE_BOX^wx.RESIZE_BORDER)
        self.colors={0:(204,192,179),2:(238, 228, 218),4:(237, 224, 200),
                8:(242, 177, 121),16:(245, 149, 99),32:(246, 124, 95),
                64:(246, 94, 59),128:(237, 207, 114),256:(237, 207, 114),
                512:(237, 207, 114),1024:(237, 207, 114),2048:(237, 207, 114),
                4096:(237, 207, 114),8192:(237, 207, 114),16384:(237, 207, 114),
                32768:(237, 207, 114),65536:(237, 207, 114),131072:(237, 207, 114)}
        icon=wx.Icon('icon.ico',wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
        self.bgFont=wx.Font(50,wx.FONTFAMILY_SWISS,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD)
        self.scFont=wx.Font(36,wx.FONTFAMILY_SWISS,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD)
        self.sbFont=wx.Font(15,wx.FONTFAMILY_SWISS,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL)
        self.smFont=wx.Font(12,wx.FONTFAMILY_SWISS,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL)
        
        self.actions=['up','down','left','right']
        self.keyCodes=[ord(ch) for ch in 'WSAD']
        self.keyCodes+=[wx.WXK_UP,wx.WXK_DOWN,wx.WXK_LEFT,wx.WXK_RIGHT]
        self.keyAction=dict(zip(self.keyCodes,self.actions*2))
        
        self.size=size
        self.winScore=winScore
        self.bstScore=self.loadBst()
        self.reset()
        
        self.panelSize=wx.Panel(self,-1,pos=(195,40),size=(70,50))
        
        self.panelGoal=wx.Panel(self,-1,pos=(270,40),size=(70,50))
        self.panelGoal.SetBackgroundColour((250,248,239))
#        panel.Bind(wx.EVT_KEY_DOWN,self.onKeyDown)
#        panel.SetFocus()
        
        
        self.panelSize.Bind(wx.EVT_LEFT_DOWN,self.reSize)
        self.panelGoal.Bind(wx.EVT_LEFT_DOWN,self.onGoal)
        
        self.Bind(wx.EVT_KEY_DOWN,self.onKeyDown)
        self.Bind(wx.EVT_SIZE,self.onSize)
        self.Bind(wx.EVT_PAINT,self.onPaint)
        self.Bind(wx.EVT_CLOSE,self.onClose)
        self.SetClientSize((505,720))
        self.Center()
        self.Show()

    def reset(self):
        self.grid=Grid(self.size)
        self.cells=self.grid.cells
        self.curScore=self.grid.score
        self.win=False

    def loadBst(self):
        if os.path.exists('bestscore.ini'):
            with open('bestscore.ini') as f:
                try:
                    readScore=int(f.read())
                except ValueError:
                    readScore=0
        else:
            readScore=0
        return readScore
    
    def reSize(self,event):
        self.size=self.size+1 if self.size<7 else 3
        self.reset()
        self.drawAll()
        
    def onGoal(self,event):
        self.winScore=self.winScore*2 if self.winScore<8192 else 16
        self.reset()
        self.drawAll()
    
    def onKeyDown(self,event):
        keyCode=event.GetKeyCode()
        if keyCode in self.keyCodes:
            self.move(self.keyAction[keyCode])
        elif keyCode==ord('R'):
            self.reset()
            self.drawAll()
        elif keyCode==ord('Q'):
            self.close()
        elif keyCode==wx.WXK_BACK:
            self.gameBack()
        elif keyCode==wx.WXK_F10:
            self.move(self.grid.move_best())
        
    def onSize(self,event):
        w,h=self.GetClientSize()
        self.buffer=wx.Bitmap(w,h)
        self.drawAll()
    
    def onPaint(self,event):
        dc=wx.BufferedPaintDC(self,self.buffer)
        
    def onClose(self,event):
        self.close()
        
    def move(self,direction):
        if self.can_move(direction):
            self.cells=self.grid.cells
            getattr(self.grid,'move_'+direction)()
            self.grid.add_random_item()
            self.curScore=self.grid.score
            self.bstScore=self.curScore if self.curScore>self.bstScore else self.bstScore
            self.drawAll()
            if self.is_win:
                self.gameWin()
            if self.is_over:
                self.gameOver()
        
    def can_move(self,direction):
        return getattr(self.grid,'can_move_'+direction)()
    
    def gameBack(self):
        self.grid.cells=self.cells
        self.drawAll()
    
    @property
    def is_win(self):
        return max(chain(*self.grid.cells))>=self.winScore
    
    def gameWin(self):
        if not self.win:
            if wx.MessageBox(u"恭喜获胜，是否继续游戏？",u"哈哈",wx.YES_NO|wx.ICON_INFORMATION)==wx.NO:
                self.reset()
                self.drawAll()
            else:
                self.win=True
       
    @property
    def is_over(self):
        return not any(self.can_move(direction) for direction in self.actions)
        
    def gameOver(self):
        if wx.MessageBox(u"挑战失败，是否重新开始？",u"呜呜",wx.YES_NO|wx.ICON_INFORMATION)==wx.YES:
            self.reset()
            self.drawAll()
        else:
            self.close()
        
    def drawAll(self):
        dc=wx.BufferedDC(wx.ClientDC(self),self.buffer)
        self.drawBg(dc)
        self.drawLabel(dc)
        self.drawScore(dc)
        self.drawTiles(dc)
        dc=wx.BufferedDC(wx.ClientDC(self.panelSize),wx.Bitmap(70,50))
        self.drawSize(dc)
        dc=wx.BufferedDC(wx.ClientDC(self.panelGoal),wx.Bitmap(70,50))
        self.drawGoal(dc)
        
    def drawBg(self,dc):
        dc.SetBackground(wx.Brush((250,248,239)))#background color
        dc.Clear()
        dc.SetBrush(wx.Brush((187,173,160)))
        dc.SetPen(wx.Pen((187,173,160)))
        dc.DrawRoundedRectangle(15,150,475,475,5)
        
    def drawLabel(self,dc):
        dc.SetTextForeground((119,110,101))
        dc.SetFont(self.bgFont)
        dc.DrawText(u"2048",15,28)
        dc.SetFont(self.smFont)
        dc.DrawText(u"当两个相同数字的方块碰到一起时会进行合成，向目标前进吧!",15,114)
        dc.DrawText(u"(W)上 (S)下 (A)左 (D)右 (BackSpace)悔棋 (R)重置 (Q)退出\n\n点击SIZE更改棋盘大小，点击GOAL更改目标",15,639)

    def drawSize(self,dc):
        self.panelSize.SetBackgroundColour((250,248,239))        
        dc.SetFont(self.sbFont)
        dc.SetBrush(wx.Brush((250,248,239)))
        dc.SetPen(wx.Pen((250,248,239)))
        dc.DrawRectangle(0,0,70,50)
        dc.SetBrush(wx.Brush((187,173,160)))
        dc.SetPen(wx.Pen((187,173,160)))
        dc.DrawRoundedRectangle(0,0,70,50,3)
        dc.SetTextForeground((238,228,218))
        sizeLabelSize=dc.GetTextExtent(u"SIZE")
        dc.DrawText(u"SIZE",35-sizeLabelSize[0]/2,5)
        self.drawNum(dc,self.size,35,35)

    def drawGoal(self,dc):
        self.panelSize.SetBackgroundColour((250,248,239))        
        dc.SetFont(self.sbFont)
        dc.SetBrush(wx.Brush((250,248,239)))
        dc.SetPen(wx.Pen((250,248,239)))
        dc.DrawRectangle(0,0,70,50)
        dc.SetBrush(wx.Brush((187,173,160)))
        dc.SetPen(wx.Pen((187,173,160)))
        dc.DrawRoundedRectangle(0,0,70,50,3)
        dc.SetTextForeground((238,228,218))
        goalLabelSize=dc.GetTextExtent(u"GOAL")
        dc.DrawText(u"GOAL",35-goalLabelSize[0]/2,5)
        self.drawNum(dc,self.winScore,35,35)

    def drawScore(self,dc):            
        dc.SetFont(self.sbFont)
        dc.SetBrush(wx.Brush((187,173,160)))
        dc.SetPen(wx.Pen((187,173,160)))
        scoreLabelSize = dc.GetTextExtent(u"SCORE")
        bestLabelSize = dc.GetTextExtent(u"BEST")
        dc.DrawRoundedRectangle(420,40,70,50,3)
        dc.DrawRoundedRectangle(345,40,70,50,3)
        dc.SetTextForeground((238,228,218))
        dc.DrawText(u"SCORE",380-scoreLabelSize[0]/2,45)
        dc.DrawText(u"BEST",455-bestLabelSize[0]/2,45)      
        self.drawNum(dc,self.bstScore,455,75)
        self.drawNum(dc,self.curScore,380,75)
        
    def drawNum(self,dc,num,midx,midy):
        sgFont=self.sbFont
        dc.SetFont(sgFont)
        dc.SetTextForeground((255,255,255))        
        size = dc.GetTextExtent(str(num))
        while size[0]>50:
            sgFont=wx.Font(sgFont.GetPointSize()*0.8,wx.FONTFAMILY_SWISS,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL)
            dc.SetFont(sgFont)
            size=dc.GetTextExtent(str(num))
        dc.DrawText(str(num),midx-size[0]/2,midy-size[1]/2)

    def drawTiles(self,dc):
        dc.SetFont(self.scFont)
        for row in range(self.grid.size):
            for col in range(self.grid.size):
                value=self.grid.cells[row][col]
                color=self.colors[value]
                if value==2 or value==4:
                    dc.SetTextForeground((119,110,101))
                else:
                    dc.SetTextForeground((255,255,255))
                dc.SetBrush(wx.Brush(color))
                dc.SetPen(wx.Pen(color))
                width=475/(self.grid.size*1.15+0.15)
                dc.DrawRoundedRectangle(15+(0.15+1.15*col)*width,150+(0.15+1.15*row)*width,width,width,2)
                size=dc.GetTextExtent(str(value))
                while size[0]>0.7*width:
                    self.scFont=wx.Font(self.scFont.GetPointSize()*0.8,wx.FONTFAMILY_SWISS,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD)
                    dc.SetFont(self.scFont)
                    size=dc.GetTextExtent(str(value))
                if value!=0:
                    dc.DrawText(str(value),15+(0.15+1.15*col)*width+(width-size[0])/2,150+(0.15+1.15*row)*width+(width-size[1])/2)
        
    def close(self):
        if self.loadBst()<self.bstScore:
             with open('bestscore.ini','w+') as f:
                 f.write(str(self.bstScore))
        self.Destroy()
    
class Grid(object):
    def __init__(self,size):
        self.size=size
        self.reset()
    
    def reset(self):
        self.cells=[[0 for i in range(self.size)] for j in range(self.size)]
        self.add_random_item()
        self.add_random_item()
        self.score=0
    
    def add_random_item(self):
        empty_cells=[(i,j) for i in range(self.size) for j in range(self.size) if self.cells[i][j]==0]
        (i,j)=random.choice(empty_cells)
        self.cells[i][j]=4 if random.randrange(100)>=90 else 2

    def transpose(self):
        self.cells=[list(row) for row in zip(*self.cells)]
        
    def invert(self):
        self.cells=[row[::-1] for row in self.cells]
        
    def move_row_left(self,row):
        def tighten(row):
            new_row=[i for i in row if i!=0]
            new_row+=[0 for i in range(len(row)-len(new_row))]
            return new_row
        
        def merge(row):
            pair=False
            new_row=[]
            for i in range(len(row)):
                if pair:
                    new_row.append(2*row[i])
                    self.score+=row[i]
                    pair=False
                else:
                    if i+1<len(row) and row[i]==row[i+1]:
                        pair=True
                        new_row.append(0)
                    else:
                        new_row.append(row[i])
            assert len(new_row)==len(row)
            return new_row
        
        return tighten(merge(tighten(row)))
    
    def move_left(self):
        self.cells=[self.move_row_left(row) for row in self.cells]
        
    def move_right(self):
        self.invert()
        self.move_left()
        self.invert()
        
    def move_up(self):
        self.transpose()
        self.move_left()
        self.transpose()
        
    def move_down(self):
        self.transpose()
        self.move_right()
        self.transpose()

    def move_best(self):
        cellsTmp=self.cells
        scoreTmp=self.score
        score=scoreTmp
        best='up'
        actions=['up','down','left','right']
        for action in actions:
            getattr(self,'move_'+action)()
            if self.score>score:
                score=self.score
                best=action
            self.cells=cellsTmp
            self.score=scoreTmp
        if score==scoreTmp:
            for action in actions:
                if getattr(self,'can_move_'+action)():
                    best=action
                    break
        return best

    @staticmethod
    def row_can_move_left(row):
        def change(i):
            if row[i]==0 and row[i+1]!=0:
                return True
            if row[i]!=0 and row[i+1]==row[i]:
                return True
            return False
        return any(change(i) for i in range(len(row)-1))
    
    def can_move_left(self):
        return any(self.row_can_move_left(row) for row in self.cells)
    
    def can_move_right(self):
        self.invert()
        can=self.can_move_left()
        self.invert()
        return can
    
    def can_move_up(self):
        self.transpose()
        can=self.can_move_left()
        self.transpose()
        return can
    
    def can_move_down(self):
        self.transpose()
        can=self.can_move_right()
        self.transpose()
        return can

if __name__=='__main__':
    app = wx.App()  
    Frame('2048')
    app.MainLoop()