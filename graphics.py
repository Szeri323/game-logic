def show_player_statistics(character):
    print(character)
    print( '\033[93m' + "test" + '\033[0m')

# Printing object without table grad and string marks
# def show_map(city_map):
#     print( '\033[93m' + "test" + '\033[0m')
#     for i in range(len(city_map)):
#         row = ''
#         for j in range(len(city_map[i])):
#             row += city_map[i][j]
#         print(row)

# Printing objects in table and string marks
def show_map(city_map):
    for i in range(len(city_map)):
        print(city_map[i])