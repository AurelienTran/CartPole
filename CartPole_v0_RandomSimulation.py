import gymnasium as gym
import time

# Create environment
env = gym.make('CartPole-v1', render_mode="human")

# Initialize environment and get initial state
state = env.reset()
print("The initial observation is", state)

for step in range(1500):
    # Select a random action
    action = env.action_space.sample()

    # Apply action to environment
    state, reward, terminated, truncated, info = env.step(action)

    # render the environment
    env.render()

    # Wait a little before going to next rendering frame
    #time.sleep(0.001)

    # if episode is complete, start a new one
    if terminated or truncated:
        state = env.reset()

# close the environment
env.close()
 