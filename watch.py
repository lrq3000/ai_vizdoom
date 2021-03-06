#!/usr/bin/python

import sys

from qengine import *

agent_loadfile = "params/superhealth/" + "vlad"
config_file = "superhealth" + ".cfg"

if len(sys.argv) > 1:
    agent_loadfile = sys.argv[1]
    if len(sys.argv) > 2:
        config_file = sys.argv[2]

game = DoomGame()
game.load_config("common.cfg")
game.load_config(config_file)

game.set_window_visible(True)

game.set_screen_format(ScreenFormat.GRAY8)

print "Initializing DOOM ..."
game.init()
print "\nDOOM initialized."

engine = QEngine.load(game, agent_loadfile)
print engine._skiprate
print "\nNetwork architecture:"
for p in get_all_param_values(engine.get_network()):
    print p.shape

episode_sleep = 0.5
action_sleep = 1 / 35.0

episodes = 20
rewards = []
for i in range(episodes):
    r = engine.run_episode(action_sleep)
    rewards.append(r)
    print i + 1, "Reward:", r
    if episode_sleep > 0:
        sleep(episode_sleep)

print "Mean rewards:", np.mean(rewards)
