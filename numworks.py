from kandinsky import *
draw_rect=fill_rect
from ion import *
from time import sleep
from random import *
try:
    lx,ly=WIDTH,HEIGHT
    env="pc"
except:
    lx, ly = 320, 222
    env="pc"

print("Attaque Ecureuil Numworks Edition")
print("1. Facile")
print("2. Normal")
print("3. Difficile")
diff=int(input())*5
bcol=(128,0,128)
fill_rect(0,0,lx,ly,bcol)
ccol=(255,150,0)
scol=(255,255,0)
ptc=(255,255,255)
chx,chy=0,0
chp=5
pts=0
ptx,pty=randint(20,lx-20),randint(20,ly-20)

tixdelay=0

sqx,sqy=lx-30,ly-30
slpt=0.03
while True:
    #cat loop
    if keydown(KEY_LEFT):
        chx-=10
        chx=max(chx,0)

    if keydown(KEY_RIGHT):
        chx+=10
        chx=min(chx,lx)

    if keydown(KEY_UP):
        chy-=10
        chy=max(chy,0)

    if keydown(KEY_DOWN):
        chy+=10
        chy=min(chy,ly)

    #squirrel loop
    #logic
    dx,dy=chx-sqx,chy-sqy
    if abs(dx)<10 and abs(dy)<10:
        if tixdelay<=0:
            chp-=1
            print("oof")
            tixdelay=30
    else:
        psqx,psqy=sqx,sqy
        if dx<0: sqx-=diff
        else: sqx+=diff
        if dy<0: sqy-=diff
        else: sqy+=diff
    if chp<=0:
        print("PTS:",pts)
        exit()
    tixdelay-=1
    #the points.........
    if abs(chx-ptx)<=20 and abs(chy-pty)<=20:
        pts+=1
        if pts%10==0:
            chp+=1
            bcol=(randint(1,255),randint(1,255),randint(1,255))
        ptx,pty=randint(20,lx-20),randint(20,ly-20)
    fill_rect(0,0,lx,ly,bcol)
    draw_rect(ptx,pty,20,20,ptc)
    draw_rect(sqx-10,sqy-10,20,20,scol)
    draw_rect(chx,chy,10,10,ccol)
    draw_string(str(chp)+"pv",0,0)
    draw_string(str(pts)+"pts",0,20)
    sleep(slpt)

