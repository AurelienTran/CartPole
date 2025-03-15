import gymnasium as gym
import time

# Create environment
env = gym.make('CartPole-v1', render_mode="human")


# PID for cart position
P1 = 0.001
I1 = 0.000
D1 = 0.000

# PID for angle position
P2 = 2.0
I2 = 0.00
D2 = -0.5

for episod in range(10):
    # Initialize environment and get initial state
    (state, _) = env.reset()
    pid1_integral = 0
    pid2_integral = 0

    for step in range(500):
        # Get all state data
        cart_pos, cart_vel, ang_pos, ang_vel = state

        # PID calculation for setting ang position target
        cart_error = 0 - cart_pos
        pid1_integral += cart_error
        ang_target = cart_error * P1 + cart_vel * D1 + pid1_integral * I1

        # PID calculation for angle
        ang_error  = ang_target - ang_pos
        pid2_integral += ang_error
        output = ang_error * P2 + ang_vel * D2 + pid2_integral * I2

        # Set action based on PID output
        action = 0
        if output < 0:
            action = 1

        # print("angle={:2.4f} | ouput={:2.4f} | {} |".format(ang_pos, output, action))

        # Apply action to environment
        state, reward, terminated, truncated, info = env.step(action)

        # render the environment
        env.render()

        # Wait a little before going to next rendering frame
        #time.sleep(0.01)

        # if episode is complete, start a new one
        if terminated or truncated:
            (state, _) = env.reset()
            break

# close the environment
env.close()
 