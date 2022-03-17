import gym
from gym import error, spaces, utils

class ProbeEnv1(gym.Env):
    def __init__(self):
        self.action_space = 1
        self.observation_space = spaces.Discrete(1)

    def step(self, action):
        state = 0
        reward = 1
        done = True
        info = {}

        return state, reward, done, info

    def reset(self):
        state = 0
        return state

    def close(self):
        pass

    def render(self, mode='human'):
        pass