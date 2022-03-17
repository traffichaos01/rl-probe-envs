import gym
import random
from gym import error, spaces, utils

class ProbeEnv3(gym.Env):
    def __init__(self):
        self.action_space = 1
        self.observation_space = spaces.Discrete(2)
        self.state = 0
        self.timestep = 0

    def step(self, action):
        self.state = 1
        reward = 1
        done = True
        info = {}

        return self.state, reward, done, info

    def reset(self):
        self.state = 0
        self.timestep = 0
        return self.state

    def close(self):
        pass

    def render(self, mode='human'):
        pass