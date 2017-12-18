import numpy as np
import pandas as pd
import time

# Q leaning
# https://www.bilibili.com/video/av16921335/index_2.html#page=2
# https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/blob/master/contents/1_command_line_reinforcement_learning/treasure_on_right.py

np.random.seed(2)

N_STATES = 6
ACTIONS = ['left', 'right']
EPSILON = 0.9
ALPHA = 0.1
LAMBDA = 0.9
MAX_EPISODES = 13
FRESH_TIME = 0.3


def build_q_table(n_states, actions):
    table = pd.DataFrame(
        np.zeros((n_states, len(ACTIONS))),
        columns=actions
    )
    # print(table)
    return table


def chose_action(state, q_table):
    state_action = q_table.iloc[state, :]
    if (np.random.uniform() > EPSILON or (state_action.all() == 0)):
        action_name = np.random.choice(ACTIONS)
    else:
        action_name = state_action.argmax()
    return action_name

# build_q_table(N_STATES, ACTION)

# print(np.zeros((N_STATES, len(ACTION))))
