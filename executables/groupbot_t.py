import random
from schnapsen.game import Bot, PlayerPerspective, Move, SchnapsenTrickScorer, Score
from schnapsen.deck import Suit, Card, Rank
from typing import Optional


class GroupBotTracking(Bot):
    """
    This Bot is here to serve as an example of the different methods the PlayerPerspective provides.
    In the end it is just playing the first valid move.
    """
    def __init__(self, seed: int) -> None:
        self.seed = seed
        self.rng = random.Random(self.seed)
        self.my_last_move_suit: Optional[Suit] = None


    def get_move(self, state: PlayerPerspective, leader_move: Optional[Move]) -> Move:
        # You can get information on the state from your perspective
        # more methods in the documentation

        # Get valid moves
        moves: list[Move] = state.valid_moves()
        next_move_choices: list[Move] = []

        selected_move: Move
        
        #Beginner Schnapsen moves and ending with advanced technique: Tracking points 


        # Beginner move: Marriages and trump exchange
        # "If your score of the bot is lower than the opponent"
        # get opponent's score
        opponents_score = state.get_opponent_score().direct_points
        # get my score
        my_score = state.get_opponent_score().direct_points
        # if my score is lower than the opponent's
        if my_score < opponents_score:
            # for every valid move I can in principle play at this point of the game following the rules
            for valid_move in valid_moves:
                # "Try to play a marriage or trump exchange (if this is a valid move)"
                # if this move is either a trump exchange or a marriage
                if valid_move.is_trump_exchange() or valid_move.is_marriage():
                    next_move_choices.append(valid_move)

        #Advanced technique: Tracking points

        #If this occurs, win at all cost
        if 66 >= opponents_score >= 55:
            
        elif 66 >= opponents_score >= 55 and my_score < 33:

        elif :
            selected_move = self.rng.choice(list(moves))

        return selected_move

    def __repr__(self) -> str:
        return f"GroupBotTracking(seed={self.seed})"   
