from gym.envs.registration import register

register(
    id='GridWorld-v0',
    entry_point='Environments.GridWorld:GridEnv',
)