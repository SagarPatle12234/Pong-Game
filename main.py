from pong_env import PongEnv
import time

def heuristic_agent(ball_y, paddle_y):
    """A simple bot that just tries to align its paddle with the ball."""
    paddle_center = paddle_y + 0.1 # Half of paddle_height (0.2)
    
    if paddle_center < ball_y - 0.05:
        return 2 # Move Down
    elif paddle_center > ball_y + 0.05:
        return 1 # Move Up
    else:
        return 0 # Stay

def main():
    # Set to "human" to watch it play. 
    # Set to None later when you are training a neural network!
    env = PongEnv(render_mode="human") 
    obs = env.reset()
    
    running = True
    while running:
        # Extract features from the observation array
        ball_y = obs[1]
        p1_y = obs[4]
        p2_y = obs[5]
        
        # Get actions
        action_left = heuristic_agent(ball_y, p1_y)
        action_right = heuristic_agent(ball_y, p2_y)
        
        # Step the environment forward
        obs, rewards, done = env.step(action_left, action_right)
        
        # Draw the frame
        env.render()
        
        if done:
            print(f"Goal scored! Rewards -> P1: {rewards[0]}, P2: {rewards[1]}")
            time.sleep(1) # Pause for a second to see who won
            obs = env.reset()

if __name__ == "__main__":
    main()