
import gymnasium as gym

class ResetAgentWrapper(gym.Wrapper):

    def __init__(self, env, agent):
        super().__init__(env)
        self.agent = agent  # Pass the externally created agent here

    def reset(self, **kwargs):
        # Call the original environment's reset method
        observation = super().reset(**kwargs)
        
        # Notify the agent to update
        self.agent.reset(self)

        return observation