import numpy as np
from numpy import random as rd

const_tokens_by_action = 10
const_max_play = 100

world_graph = {"Canada": ["Etats-unis", "Groenland"],
               "Etats-unis": ["Groenland", "France"],
               "Groenland": ["France"],
               "France": ["Russie", "Inde"],
               "Russie": ["Chine", "Inde"],
               "Inde": ["Nouvelle-Zelande", "Australie"],
               "Chine": ["Inde", "Nouvelle-Zelande"],
               "Nouvelle-Zelande": ["Australie", "Antarctique"],
               "Australie": ["Antarctique", "Madagascar", "Congo"],
               "Antarctique": ["Madagascar", "Argentine"],
               "Madagascar": ["Congo", "Argentine"],
               "Congo": ["Argentine", "Brésil"],
               "Argentine": ["Brésil", "Mexique"],
               "Brésil": ["Mexique", "Etats-unis"],
               "Mexique": ["Etats-unis", "Canada"]}


class Player:
    current_position: str = ""

    def __init__(self, initial_position: str) -> None:
        self.current_position = initial_position

    """
    Return a state proposition 
    """

    def act(self, graph: dict) -> str:
        pass
    """
    """
    def update(self, new_position):
        self.move(new_position)
    """
    Update position information of the player
    """

    def move(self, new_position: str) -> None:
        self.current_position = new_position
    """
    Update after match information
    """
    def end_episode_update(self, win_flag:bool) -> None:
        pass


class IaPlayer(Player):
    tokens_by_city = dict()
    current_action = -1
    state_action_list = []

    def __init__(self, initial_position: str):
        super().__init__(initial_position)

    def act(self, graph):
        if self.tokens_by_city.get(self.current_position) is None:
            self.tokens_by_city[self.current_position] = [const_tokens_by_action] * len(graph[self.current_position])
        tokens = self.tokens_by_city[self.current_position]
        print(tokens)
        print(self.current_position)
        token_total = sum(tokens)
        if token_total == 0:
            draw = rd.choice(len(graph[self.current_position]), 1)[0]
        else:
            draw = rd.choice(len(graph[self.current_position]), 1, p=np.array(tokens) / sum(tokens))[0]
        self.current_action = draw
        return graph[self.current_position][self.current_action]

    def update(self, new_position: str):
        self.store_state_action()
        self.move(new_position)
        self.current_action = -1

    def store_state_action(self):
        self.state_action_list.append((self.current_position, self.current_action))

    def end_episode_update(self, win_flag: bool):
        factor = 1 if win_flag else -1
        factor = 2*factor
        impact = 1
        base = 1
        for (state, action) in self.state_action_list:
            tokens = self.tokens_by_city[state][action]
            self.tokens_by_city[state][action] = max(0, tokens + base * factor)
            base += impact
        self.state_action_list = []


class RandomPlayer(Player):
    def __init__(self, initial_position: str):
        super().__init__(initial_position)

    def act(self, graph):
        current_action = rd.choice(len(graph[self.current_position]), 1)[0]
        return graph[self.current_position][current_action]


class Game:
    graph = None
    p1 = None
    p2 = None
    finish_line = ""

    def __init__(self, finish_line:str,game_graph:dict, _p1: Player, _p2: Player):
        self.finish_line = finish_line
        self.graph_keys = list(game_graph.keys())
        self.graph = game_graph
        self.p1_win_count = 0
        self.p2_win_count = 0
        self.p1 = _p1
        self.p2 = _p2
        self.current_player = self.p2

    def play(self):
        nb_play = 0
        winner_found = False
        while nb_play < const_max_play:
            state = self.current_player.act(self.graph)
            self.current_player.update(state)
            # Check if the current player win
            if self.current_player.current_position == self.finish_line:
                winner_found = True
                # Update from loosing condition
                if self.current_player == self.p1:
                    #print("Player n°1 win")
                    self.p1.end_episode_update(True)
                    self.p1_win_count += 1
                    self.p2.end_episode_update(False)
                else:
                    #print("Player n°2 win")
                    self.p2.end_episode_update(True)
                    self.p2_win_count += 1
                    self.p1.end_episode_update(False)
                self.p1.current_position = self.finish_line
                self.p2.current_position = self.finish_line
            # player change
            if self.current_player == self.p1:
                print("To player n°2")
                self.current_player = self.p2
            else:
                print("To player n°1")
                self.current_player = self.p1
            if winner_found:
                print(f"Player 1 win count: {self.p1_win_count} \nPlayer 2 win count: {self.p2_win_count}")
                winner_found = False

if __name__ == '__main__':
    init_pos = "France"
    player1 = IaPlayer(init_pos)
    player2 = RandomPlayer(init_pos)
    game = Game(init_pos, world_graph, player1, player2)
    game.play()






