import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    bg_img_o = pg.transform.flip(bg_img, True, False)
    kk_img_o = pg.transform.rotozoom(kk_img, 10, 1.0)
    kk_img_lst = [kk_img, kk_img_o]
    tmr = 0
    x=tmr
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img_o, [1600-x, 0])
        screen.blit(bg_img, [3200-x, 0])
        screen.blit(kk_img_lst[tmr%100//50], [300, 200])
        pg.display.update()
        tmr += 1 
        x += 1       
        clock.tick(100)
        if x >= 3199:
            x = 0


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()