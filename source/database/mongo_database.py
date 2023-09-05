import datetime as datetime
from pymongo import MongoClient
from pymongo.database import Database

from ..core.agent import Agent
from ..core.game_state import GameState
from ..core.move import Move
from .move_encoder import encode_moves


class MongoDatabase:
    __database_name = 'connect-x-data'
    __database: Database
    __client: MongoClient
    connected = False

    __game_collection = 'game-history'

    def connect(self, connection_string: str):
        try:
            self.__client = MongoClient(connection_string)
        except:
            print('Error connecting to database')
            raise
        self.connected = True

        #database_names = self.__client.list_database_names()
        #if self.__database_name not in database_names:
        #    print(f"Couldn't find database {self.__database_name}, creating")
        self.__database = self.__client[self.__database_name]  # Creates the database connection if it doesn't exist

    def write_game(self, moves: list[Move], final_state: GameState, agent1: Agent, agent2: Agent,
                   datetime: datetime.datetime):
        data = {'datetime': datetime,
                'agent1': agent1.get_name(),
                'agent2': agent2.get_name(),
                'final_state': final_state,
                'moves': encode_moves(moves)}
        collection = self.__database[self.__game_collection]
        collection.insert_one(data)
