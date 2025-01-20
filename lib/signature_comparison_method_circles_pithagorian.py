def parse_sig_str_to_list(sig: str) -> list[(int,int)]:
    points_strs = sig.split("/")
    points = []
    for point_str in points_strs:
        point_x = int(point_str.split(",")[0])
        point_y = int(point_str.split(",")[1])
        points.append((point_x, point_y))
    return points

# sig = "123,128/50,70/250,40"
# print(parse_sig_str_to_list(sig))

def parallel_rebase(points: list[(int, int)], delta_x: int, delta_y: int):
    length = len(points)
    i = 0
    while i < length:
        point_new_x = points[i][0] + delta_x
        point_new_y = points[i][1] + delta_y
        point = (point_new_x, point_new_y)
        points[i] = point
        i += 1

# sig = "123,128/50,70/250,40"
# sig_list = parse_sig_str_to_list(sig)
# parallel_rebase(sig_list, 1, 1)
# print(sig_list)

def compare_two_signatures(ethalone: str, comparable: str, tolerance: int) -> int:
    ethalone_points = parse_sig_str_to_list(ethalone)
    comparable_points = parse_sig_str_to_list(comparable)
    ethalone_length = len(ethalone_points)
    comparable_length = len(comparable_points)
    length_ratio_coefficient = (comparable_length / ethalone_length)

    if length_ratio_coefficient > 1:
        length_ratio_coefficient = 1 / length_ratio_coefficient # makes the coefficient always being in range of 0 and 1

    acceptable_radius_pow2 = tolerance * tolerance
    parallel_rebase(comparable_points,
                    ethalone_points[0][0] - comparable_points[0][0],
                    ethalone_points[0][1] - comparable_points[0][1]) # alignment of the whole points sets by the first point (offset)

    quantity_of_curve_fitting_points = 0 # the amount of points considered matching by the radius 
    for comparable_point in comparable_points:
        for ethalone_point in ethalone_points:
            if ((ethalone_point[0]-comparable_point[0])**2
                + (ethalone_point[1]-comparable_point[1])**2
                    <= acceptable_radius_pow2):
                quantity_of_curve_fitting_points += 1
                break
    return int(100 * quantity_of_curve_fitting_points/comparable_length * length_ratio_coefficient )

# sig_e = "123,128/50,70/250,40"
# sig_c = "143,148/70,90/250,40"
# print(compare_two_signatures(sig_e, sig_c))
