import sys, tty, os, termios

# maps = []
# for i in range(10):
#     maps.append([]) 
#     for j in range(10):
#         maps[i].append(" ") 
# Player = [0, 0]

def getkey():
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    try:
        while True:
            b = os.read(sys.stdin.fileno(), 3).decode()
            if len(b) == 3:
                k = ord(b[2])
            else:
                k = ord(b)
            key_mapping = {
                127: 'backspace',
                10: 'return',
                32: 'space',
                9: 'tab',
                27: 'esc',
                65: 'up',
                66: 'down',
                67: 'right',
                68: 'left'
            }
            return key_mapping.get(k, chr(k))
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
# try:
#     while True:
#         k = getkey()
#         if k == 'esc':
#             quit()
#         else:
#             if k == 'w':
#                 Player[0]-=1
#                 print(k)
#                 print(Player)
#             if k == 's':
#                 Player[0]+=1
#                 print(k)
#                 print(Player)
#             if k == 'd':
#                 Player[1]+=1
#                 print(k)
#                 print(Player)
#             if k == 'a':
#                 Player[1]-=1
#                 print(k)
#                 print(Player)
#             maps[Player[0]][Player[1]] = "P"
#             for i in range(len(maps)):
#                 print(maps[i])
#             maps[Player[0]][Player[1]] = " "
# except (KeyboardInterrupt, SystemExit):
#     os.system('stty sane')
#     print('stopping.')
    