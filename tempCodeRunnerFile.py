 if ((Player1.rect.right - offset_x >= WIDTH - scroll_area_width and Player1.x_vel > 0) or 
            (Player1.rect.left - offset_x <= scroll_area_width and Player1.x_vel < 0)):
            offset_x += Player1.x_vel