from gym.envs.registration import register

register(
    id='probe-env-v1',
    entry_point='rl_probe_envs.envs:ProbeEnv1',
)

register(
    id='probe-env-v2',
    entry_point='rl_probe_envs.envs:ProbeEnv2',
)

register(
    id='probe-env-v3',
    entry_point='rl_probe_envs.envs:ProbeEnv3',
)

register(
    id='probe-env-v4',
    entry_point='rl_probe_envs.envs:ProbeEnv4',
)

register(
    id='probe-env-v5',
    entry_point='rl_probe_envs.envs:ProbeEnv5',
)
