import pygame

uncollidable = ["cherry", "pineapple", "checkpoint"]

def handle_vertical_collision(player, objects, dy):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if dy > 0 and obj.name not in uncollidable:
                
                player.rect.bottom = obj.rect.top
                player.landed()
            elif dy < 0 and obj.name not in uncollidable:
                player.rect.top = obj.rect.bottom
                player.hit_head()

            collided_objects.append(obj)

    return collided_objects


def collide(player,objects,dx):
    player.move(dx,0)
    player.update()
    collided_object = None
    for obj in objects:
        if pygame.sprite.collide_mask(player,obj):
            collided_object = obj
            break

    player.move(-dx, 0)
    player.update()
    return collided_object

def handle_move(player, objects):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    collide_left = collide(player,objects,-player.PLAYER_VEL*2)
    collide_right = collide(player,objects,player.PLAYER_VEL*2)

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and (not collide_left or collide_left.name in uncollidable):
        player.move_left(player.PLAYER_VEL)
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and (not collide_right or collide_right.name in uncollidable):
        player.move_right(player.PLAYER_VEL)

    vertical_collide = handle_vertical_collision(player, objects, player.y_vel)
    to_check = [collide_left, collide_right, *vertical_collide]
    for obj in to_check:
        if obj and obj.name == "fire":
            player.make_hit()
        if obj and obj.name == "trampoline":
            player.highjump()
            obj.activated()
        if obj and obj.name == "spikes":
            player.make_hit()
        if obj and obj.name=="falling_platform":
            obj.start_falling(300) #300 så plattformen respawner etter 5 sekunder
            player.landed()
        if obj and obj.name == "fan":
            player.hover()
        if obj and obj.name == "cherry":
            if obj.isCollected == False:
                if player.lives < 3:
                    player.lives += 1
                obj.collected()
        if obj and obj.name == "pineapple":
            obj.collected()
            player.activate_superspeed()
        if obj and obj.name == "checkpoint":
            obj.activate()
            player.update_respawn_position(obj.rect.x, obj.rect.y)
        if obj and obj.name == "speedplatform":
            player.activate_conveyor()
        if obj and obj.name != "speedplatform":
            player.deactivate_conveyor()

