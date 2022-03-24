import gym
import rl_probe_envs

def print_step(state, action, next_state, reward, done, timestep):
    print("------------------------------------------")
    print("State: {}".format(state))
    print("Action: {}".format(action))
    print("Next State: {}".format(next_state))
    print("Reward: {}".format(reward))
    print("Episode Terminated after Action(True/False): {}".format(done))
    print("Timestep Started From: {}".format(timestep))
    print("------------------------------------------\n\n")

def experiment_1(verbose=False):
    print("Starting Experiment for Probe Env 1")
    env1 = gym.make("rl_probe_envs.envs:ProbeEnv1")
    state = env1.reset()
    dummy_action = 0
    next_state, reward, done, _ = env1.step(dummy_action)
    env1.close()
    if verbose:
        print_step(state, dummy_action, next_state, reward, done, 0)

if __name__ == '__main__':
    experiment_1(verbose=True)


