import tcod
from entity import Entity
from input_handlers import handle_keys
from map_objects.game_map import GameMap
from render_functions import clear_all, render_all


def main():
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    colors = {
        'dark_wall': tcod.Color(0, 0, 100),
        'dark_ground': tcod.Color(50, 50, 150)
    }

    player = Entity(int(screen_width / 2),
                    int(screen_height / 2), '@', tcod.white)
    npc = Entity(int(screen_width / 2 - 5),
                 int(screen_height / 2), '@', tcod.yellow)

    entities = [player, npc]

    tcod.console_set_custom_font(
        "BBT\\fonts\\arial10x10.png", tcod.FONT_TYPE_GRAYSCALE | tcod.FONT_LAYOUT_TCOD)
    tcod.console_init_root(screen_width, screen_height, 'Engine', False)

    con = tcod.console_new(screen_width, screen_height)

    game_map = GameMap(map_width, map_height)

    key = tcod.Key()
    mouse = tcod.Mouse()

    # 游戏主循环
    while not tcod.console_is_window_closed():

        tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS, key, mouse)

        render_all(con, entities, game_map,
                   screen_width, screen_height, colors)

        tcod.console_flush()

        clear_all(con, entities)

        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            if not game_map.is_blocked(player.x + dx, player.y + dy):
                player.move(dx, dy)

        if exit:
            return True
        if fullscreen:
            tcod.console_set_fullscreen(not tcod.console_is_fullscreen())


if __name__ == "__main__":
    main()
