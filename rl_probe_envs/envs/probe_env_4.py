import gym
import random
from gym import error, spaces, utils

class ProbeEnv4(gym.Env):
    def __init__(self):
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Discrete(1)
        self.state = 0
        self.possible_values = [-1, 1]

    def step(self, action):
        reward = self.possible_values[action]
        done = True
        info = {}

        return self.state, reward, done, info

    def reset(self):
        return self.state

    def close(self):
        pass

    def render(self, mode='human'):
        pass