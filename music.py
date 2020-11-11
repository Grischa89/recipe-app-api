import musicalbeeps


player = musicalbeeps.Player(volume = 0.3,
                            mute_output = False)

print(dir(player))
player.play_note("F5#")

player.play_note("A", 2.2)

