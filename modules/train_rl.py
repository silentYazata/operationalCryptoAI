import numpy as np
import pandas as pd
import gym
from gym import spaces
from stable_baselines3 import PPO

class TradingEnv(gym.Env):
    def __init__(self, data):
        super(TradingEnv, self).__init__()
        self.data = data
        self.current_step = 0
        self.action_space = spaces.Discrete(3)  # Buy, Hold, Sell
        self.observation_space = spaces.Box(low=0, high=np.inf, shape=(len(data.columns),), dtype=np.float32)
        self.current_balance = 1000  # Starting balance
        self.current_position = 0  # Current position in the market

    def reset(self):
        self.current_step = 0
        self.current_balance = 1000
        self.current_position = 0
        return self.data.iloc[self.current_step].values

    def step(self, action):
        current_price = self.data.iloc[self.current_step]['Close']
        reward = 0

        if action == 0:  # Buy
            if self.current_balance >= current_price:
                self.current_position += 1
                self.current_balance -= current_price
                reward = -1  # Cost of buying
        elif action == 1:  # Hold
            reward = 0
        elif action == 2:  # Sell
            if self.current_position > 0:
                self.current_position -= 1
                self.current_balance += current_price
                reward = 1  # Profit from selling

        self.current_step += 1
        done = self.current_step >= len(self.data) - 1
        next_state = self.data.iloc[self.current_step].values if not done else np.zeros(self.data.shape[1])

        return next_state, reward, done, {}

    def render(self):
        profit = self.current_balance + (self.current_position * self.data.iloc[self.current_step]['Close']) - 1000
        print(f'Step: {self.current_step}, Balance: {self.current_balance}, Position: {self.current_position}, Profit: {profit}')

def train_agent(data):
    env = TradingEnv(data)
    model = PPO('MlpPolicy', env, verbose=1)
    model.learn(total_timesteps=10000)
    return model

# Example usage:
# data = pd.read_csv('historical_data.csv')  # Load your historical data
# trained_model = train_agent(data)