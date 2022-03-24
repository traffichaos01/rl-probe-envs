import gym
import random
from gym import error, spaces, utils

class ProbeEnv2(gym.Env):
    def __init__(self):
        self.action_space = spaces.Discrete(1)
        self.observation_space = spaces.Discrete(2)
        self.possible_values = [-1, 1]
        self.state = self.possible_values[random.randint(0, 1)]

    def step(self, action):
        reward = self.state
        done = True
        info = {}

        return self.state, reward, done, info

    def reset(self):
        self.state = self.possible_values[random.randint(0, 1)]
        return self.state

    def close(self):
        pass

    def render(self, mode='human'):
        pass