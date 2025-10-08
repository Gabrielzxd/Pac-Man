from sprites import SpriteSheet

sprite = SpriteSheet("src/assets/graphics/tileset.png", 8, 8, 1)

tile_catalog = []
for y in range(3):
    for x in range(16):
        tile_catalog.append(sprite.get_sprite(x, y))

edge_top_right = 0
edge_top_left = 1
wall_right_vertical = 2
wall_left_vertical = 3
edge_bottom_right = 4
edge_bottom_left = 5
edge_double_top_right = 6
edge_double_top_left = 7
edge_double_bottom_right = 8
edge_double_bottom_left = 9
wall_high_1 = 10
wall_high_2 = 11
wall_below_1 = 12
wall_below_2 = 13
wall_single_below_1 = 14
wall_single_below_2 = 15
edge_smooth_top_right = 16
edge_smooth_top_left = 17
edge_smooth_bottom_right = 18
edge_smooth_bottom_left = 19
wall_single_high_1 = 20
wall_single_high_2 = 21
edge_inner_above_right = 22
edge_inner_above_left = 23
wall_single_vertical_1 = 24
wall_single_vertical_2 = 25
edge_inner_high_right_1 = 26
edge_inner_high_left_1 = 27
ninety_degree_above_right = 28
ninety_degree_above_left = 29
ninety_degree_high_right = 30
ninety_degree_high_left = 31
L_lying_down_left = 32
L_lying_down_right = 33
semi_circle_above_left = 34
semi_circle_above_right = 35
semi_circle_high_left = 36
semi_circle_high_right = 37
edge_inner_above_right_tiny = 38
edge_inner_above_left_tiny = 39
edge_inner_high_right_2 = 40
edge_inner_high_left_2 = 41
semi_circle_above_left_full = 42
semi_circle_above_right_full = 43
empty = 44
tiny_pellet = 45
pellet = 46
big_pellet = 47

