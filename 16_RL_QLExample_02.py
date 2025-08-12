# Q-Learning Example
import gym

# There are two versions of the game slippery ice and a non-slippery one We'll use the non-slippery one
env = gym.make("FrozenLake-v1", is_slippery=False, render_mode="human")

print("States: ",env.observation_space.n)   # States
print("Actions: ",env.action_space.n)   # Actions

# In FrozenLake environment, the actions are 0: Left, 1: Down, 2: Right, 3: Up
action_list = {
    0: "Left",
    1: "Down",
    2: "Right",
    3: "Up"
}

env.reset()  # reset enviornment to default state

action = env.action_space.sample()  # get a random action 
print(f"Random action: {action} ({action_list[action]})")


new_state, reward, terminated, truncated, info = env.step(action)  # take action, notice it returns information about the action

env.render()