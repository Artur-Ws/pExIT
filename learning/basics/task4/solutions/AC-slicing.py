
color_list = ['red', 'blue', 'yellow', 'orange', 'purple', 'gray', 'green']


def get_colors(categories, color_list):
    return color_list[:categories]


print(get_colors(2, color_list))
