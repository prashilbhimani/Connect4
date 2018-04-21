
# coding: utf-8

# In[1]:


import numpy as np
import random
import import_ipynb
from Board import Board
from RandomPlayer import RandomPlayer
from RLPlayer import RLPlayer

# In[12]:


class Game():
    def __init__(self, player1, player2, play=True):
        
        self.winner=None
        self.completed=False
        self.win_direction=None
        self.win_point=None
        self.p=[None,None]
        self.board=Board()
        player1.move=1
        player2.move=2
        self.p[0]=player1
        self.p[1]=player2
        print("Welcome to Connect4")
        print("Player 1 (X) is " + self.p[0].name)
        print("Player 2 (O) is " + self.p[1].name)


    def reset():
        self.winner=None
        self.completed=False
        self.win_direction=None
        self.win_point=None
        self.p=[None,None]
        self.board=Board()
        
        
    
    def verticalCheck(self,r,c):
        win=False
        if 6-r>=4:
            win=True
            for i in range(4):
                if self.board.board[r][c]!=self.board.board[r+i][c]:
                    win=False
                    break
        if win:
            self.win_direction='vertical'
        return win
    
    def horizontalCheck(self,r,c):
        win=False
        if 7-c>=4:
            win=True
            for i in range(4):
                if self.board.board[r][c]!=self.board.board[r][c+i]:
                    win=False
                    break
        if win:
            self.win_direction='horizontal'
        return win
    
    def positiveDiagonalCheck(self,r,c):
        win=False
        if 6-r>=4 and 7-c>=4:
            win=True
            for i in range(4):
                if self.board.board[r][c]!=self.board.board[r+i][c+i]:
                    win=False
                    break
        if win:
            self.win_direction='positiveDiagonal'
        return win
    
    def negativeDiagonalCheck(self,r,c):
        win=False
        if 6-r>=4 and 7-c<=4:
            win=True
            for i in range(4):
                if self.board.board[r][c]!=self.board.board[r+i][c-i]:
                    win=False
                    break
        if win:
            self.win_direction='negativeDiagonal'
        return win
    
    def findWinner(self):
        for r in range(6):
            for c in range(7):
                if self.board.board[r][c]!=3 and self.board.board[r][c]!=0:
                    win= self.verticalCheck(r,c) or self.horizontalCheck(r,c) or self.positiveDiagonalCheck(r,c) or self.negativeDiagonalCheck(r,c)
                    if win:
                        self.winner=self.board.board[r][c]
                        self.completed=True
                        self.win_point=(r,c)
                        return
    
    def run(self):
        move=0
        while not self.completed and not self.board.checkFilled():
            flatten_board=self.board.board.flatten()
            possible=self.board.nextPossibleMove()
            p=self.p[move].playMove(flatten_board,possible)
            r=p[0]
            c=p[1]
            if not self.board.checkValidMove(r,c):
                print("Invalid Move")
                print("Game ends")
                return
            self.board.makeMove(r,c,move+1)
            self.findWinner()
            if move:
                move=0
            else:
                move=1
        print(self.winner)
        print(self.board.board)
        print(self.win_direction)
        print(self.win_point)

    def learn_game(self, episodes=1000):
        agent = RLPlayer(168,42)
        self.p[0]=agent
        self.p[1]=RandomPlayer()
        # Iterate the game
        for e in range(episodes):
            # reset state in the beginning of each game
            self.board = Board() 
            while not self.completed:
                # turn this on if you want to render
                # env.render()
                # Decide action
                curr_move=self.board.board.flatten()
                action = agent.playMove(state,self.board.board.flatten(),self.board.nextPossibleMove())
                # Advance the game to the next frame based on the action.
                # Reward is 1 for every frame the pole survived
                if not self.board.checkValidMove(r,c):
                    print("Invalid Move")
                    print("Game ends")
                    return
                self.board.makeMove(r,c,move+1)
                self.findWinner()

                next_state =self.board.board.flatten()
                if self.completed:
                    if self.winner==1:
                        reward=100
                        done=1
                    elif self.winner==2:
                        reward=-100
                        done=1

                # Remember the previous state, action, reward, and done
                agent.remember(curr_move, action, reward, next_state, done)
                # make next_state the new current state for the next frame.
                # done becomes True when the game ends
                # ex) The agent drops the pole
                if done:
                    # print the score and break out of the loop
                    print("episode: {}/{}, score: {}"
                          .format(e, episodes, time_t))
                    break
            # train the agent with the experience of the episode
            agent.replay(32)
    


# In[14]:


a=Game(RandomPlayer(),RandomPlayer())
a.run()

