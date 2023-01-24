import random
from schnapsen.game import Bot, PlayerPerspective, Move, SchnapsenTrickScorer, Score
from schnapsen.deck import Suit, Card, Rank, CardCollection, _CardCache
from typing import Optional


class GroupBotRemember(Bot):
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
        print(state.am_i_leader())
        print(state.get_my_score())
        # more methods in the documentation

        # Get valid moves
        moves: list[Move] = state.valid_moves()
        one_move: Move =  self.rng.choice(list(moves))
        
        #Remembering cards technique

        #List of all cards in the game
        all_cards: list[Move] = _CardCache
        print(all_cards)
        #Seen cards list, if leader_move is true, the hand is updated to the list. If none
        seen_cards: list[Move] = state.seen_cards(leader_move)

        #Unseen cards list
        unseen_cards: list[Move] = []


        return one_move

    def __repr__(self) -> str:
        return f"GroupBotRemember(seed={self.seed})"   
