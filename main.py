import sys
import pygame
from math import pi
from elements_check import check
from maxmin_num import maxmin_num
import win32api
import win32con

pygame.display.set_caption("HELLO WORLD")
screen = pygame.display.set_mode((700, 700))
screen.fill((255, 255, 255))
pygame.init()

def draw_line(start_pos,end_pos):# 起点# 终点  
    RED = (255, 0, 0)  # 定义红色
    pygame.draw.line(screen, RED, start_pos, end_pos, 5)  # 画线段

    

for i in range (4):
    start_pos = 50,50+200*i
    end_pos  =650,50+200*i
    draw_line(start_pos, end_pos)
for i in range (4):
    start_pos = 50+200*i,50
    end_pos  =50+200*i,650
    draw_line(start_pos, end_pos)


img1 = pygame.image.load("白.png")
img2 = pygame.image.load("黑.png")

# 缩放图片
img1_transfrom = pygame.transform.scale(img1,(180,180))  # 参数：缩放对象，目标大小
img2_transfrom = pygame.transform.scale(img2,(180,180))

def out(x,y):#边缘检测
    if x>=650:
        x=649
    if x<50:
        x=50
    if y>=650:
        y=649
    if y<50:
        y=50
    return x,y

pygame.display.update()

data = []
history = [0 for i in range(9)]
k = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: # 当前在屏幕中的坐标      
            a,b = event.pos#分离坐标x，y
            a,b = out(a,b)
            a2 = int((a-50)/200)+1#数字的坐标
            b2 = int((b-50)/200)+1
            position = a2+(b2-1)*3            
            a1 = int((a-50)/200)*200+60#画点的坐标
            b1 = int((b-50)/200)*200+60
            
            
            if history[position-1] ==1:
                print("不能下")
                pygame.display.update()
            else:
                            
                screen.blit(img1_transfrom,(a1,b1))
                history[position-1] = 1
                data.append(position)               
                print (data)
                
                pygame.display.update()
                if check(data)==1:
                    win32api.MessageBox(0,"不过如此","白赢了",win32con.MB_OK)
                    pygame.quit()
                    sys.exit()
                if check(data)==0:
                    win32api.MessageBox(0,"哈哈","黑赢了",win32con.MB_OK)
                    pygame.quit()
                    sys.exit()
                if check(data)==0.5:
                    win32api.MessageBox(0,"彼此彼此","平了",win32con.MB_OK)
                    pygame.quit()
                    sys.exit()
                print(data)
                data = maxmin_num(data)
                
                position_0 = data[-1]                
                b3 = int((position_0-1)/3)+1
                a3 = position_0 - 3*(b3-1)
                a4 = (a3-1)*200+60
                b4 = (b3-1)*200+60                
                screen.blit(img2_transfrom,(a4,b4))
                history[position-1] = 1
                print(data)
                
                pygame.display.update()
                if check(data)==1:
                    win32api.MessageBox(0,"不过如此","白赢了",win32con.MB_OK)
                    pygame.quit()
                    sys.exit()
                if check(data)==0:
                    win32api.MessageBox(0,"哈哈","黑赢了",win32con.MB_OK)
                    pygame.quit()
                    sys.exit()
                if check(data)==0.5:
                    win32api.MessageBox(0,"彼此彼此","平了",win32con.MB_OK)
                    pygame.quit()
                    sys.exit()
                
        
        if event.type == pygame.QUIT:
            print(data)
            pygame.quit()
            sys.exit()