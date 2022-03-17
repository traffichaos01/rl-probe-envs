import gym
import random
from gym import error, spaces, utils

class ProbeEnv5(gym.Env):
    def __init__(self):
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Discrete(3, start=-1)
        self.state = 0
        self.possible_values = [-1, 1]
        self.rewards = [[-1, 1], [1, -1]]

    def step(self, action):
        state_index = 0 if self.state is -1 else 1
        self.state = self.possible_values[random.randint(0,1)]
        reward = self.possible_values[state_index][action]
        done = True
        info = {}

        return self.state, reward, done, info

    def reset(self):
        self.state = self.possible_values[random.randint(0,1)]
        return self.state

    def close(self):
        pass

    def render(self, mode='human'):
        pass