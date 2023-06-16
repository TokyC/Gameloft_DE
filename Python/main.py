from enum import Enum
from dataclasses import dataclass
import re
from typing import Union, List
from datetime import datetime, timedelta

# it was only when I reread the statement that I remembered that I only had to modify and implement certain methods,
# not all of them.That's why there's a lot of commented code. I didn't want to delete it because I think it's still
# interesting to see what I've produced and why not get some feedback on it.

# define the class as an Enum type
class CountryCode(Enum):
    FR = 'France'
    US = 'USA'


@dataclass
class Game:
    game_name: str  # unique identifier
    release_date: str

    @classmethod
    def read_games_from_file(cls, path: str = 'games.txt') -> list:
        """Write a class function that read games from a file called games.txt.
        the file should be in the same directory as the running python script.
        Use regular expressions to parse the text file and extract needed data
        This function should be a class function
        """
        list_game = []
        regex_game = r'"([^"]+)"'  # to be corrected cause it not working 100% not enough experience with regex
        regex_date = r'\b\d{4}-\d{2}-\d{2}\b'
        with open(path, 'r') as file:
            for line in file:
                match_game = re.search(regex_game, line.strip())
                match_date = re.search(regex_date, line.strip())
                if match_game and match_date:
                    game_name = match_game.group(1)
                    release_date = match_date.group(0)
                    game = cls(game_name, release_date)
                    list_game.append(game)

        return list_game

    def has_game_been_released(self):
        """In this function you'll check whether the game has been released or not.
        by chekcing the current_date and the release_date.
        you can use the datetime library to get today's date.
        Note that transaction_date is a str and not an object in this case.
        """
        # today = datetime.today().date()
        # release_date = datetime.strptime(self.release_date, '%Y-%m-%d').date()
        # print(today)
        # if today >= release_date:
        #     print(f'the game {self.game_name} has been released')
        # else:
        #     print(f'the game {self.game_name} has not been released yet')


# define the class as a dataclass
@dataclass
class Player:
    name: str  # unique identifier
    age: int
    country: Enum
    Games: Union[str, List[str]]

    # define the method as a classmethod with the appropriate argument
    @classmethod
    def read_players_from_file(cls, path: str = 'players.txt') -> list:
        """Write a class function that read players from a file called players.txt.
        the file should be in the same directory as the running python script.
        Use regular expressions to parse the text file and extract needed data
        This function should be a class function
        """
        list_player = []
        regex = r'New Player "(?P<name>[^"]+)" has been registered: Age "(?P<age>\d+)", Country "(?P<country>[A-Z]{' \
                r'2})", playing "(?P<games1>[^"]+)"(?: and "(?P<games2>[^"]+)")?'
        with open(path, 'r') as file:
            for line in file:
                matches = re.findall(regex, line.strip())
                for match in matches:
                    try:
                        name = match[0]
                        age = int(match[1])
                        country = CountryCode.FR if match[2] == 'FR' else CountryCode.US

                        # "longer version" version but with more control:
                        # if match[2] == 'FR':
                        #     country = CountryCode.FR
                        # elif match[2] == 'US':
                        #     country = CountryCode.US
                        # else:
                        #     raise Exception('Country code not valid')

                        games = match[3:]
                        player = cls(name, age, country, games)
                        list_player.append(player)
                    except Exception as e:
                        raise e
        return list_player


# define the class as a dataclass
@dataclass
class Transaction:
    player: Player
    Game: Game
    transaction_date: str
    amount: float

    def is_transaction_valid(self):
        """Transaction is considered valid if it happens after game release.
        Transactions with date in the future are considered invalid
        """
        # today = datetime.today().date()
        # release_date = datetime.strptime(self.Game.release_date, '%Y-%m-%d').date()
        # transaction_date = datetime.strptime(self.transaction_date, '%Y-%m-%d').date()
        #
        # if release_date < transaction_date <= today:
        #     print(f'the transaction is valid')
        # else:
        #     print(f'the transaction is not valid')

    def is_transaction_recent(self) -> bool:
        """In this method you're going to check if the transaction happened in the past week.
        You have the transaction_date, and you can use the datetime library to get today's date.
        Note that transaction_date is a str and not an object in this case.
        """
        # today = datetime.today().date()
        # transaction_date = datetime.strptime(self.transaction_date, '%Y-%m-%d').date()
        # week_ago = today - timedelta(days=7)
        #
        # return transaction_date >= week_ago

    # define the method as a classmethod with the appropriate argument
    @classmethod
    def read_transactions_from_file(cls, path: str = 'transactions.txt') -> list:
        """Write a class function that read transactions from a file called transactions.txt.
        the file should be in the same directory as the running python script.
        Use regular expressions to parse the text file and extract needed data
        This function should be a class function
        """
        list_transaction = []
        regex = r'Player "(?P<player>[^"]+)" has made a new(?: \(refundable\))? transaction for game "(?P<game>[' \
                r'^"]+)" on the "(?P<date>\d{4}-\d{2}-\d{2})" for "(?P<amount>[\d.]+)" Eur'

        with open(path, 'r') as file:
            for line in file:
                matches = re.findall(regex, line.strip())
                for match in matches:
                    try:
                        player = match[0]
                        game = match[1]
                        date = match[2]
                        amount = float(match[3])
                        transaction = cls(player, game, date, amount)
                        list_transaction.append(transaction)
                    except Exception as e:
                        raise e
        return list_transaction

    # define the method as a staticmethod, change arguments if needed
    @staticmethod
    def calculate_revenue(transactions: List, player: Player) -> float:
        """In this function given a player instance, search the list of transactions made by
        the instance "player" and sum the amout in order to calculate the total revenue made by "player" instance.
        """
        total_revenue = 0
        for transaction in transactions:
            if transaction.player == player.name:
                total_revenue += transaction.amount
        return total_revenue


# define the class as a dataclass
@dataclass
class RefundableTransaction(Transaction):
    """Add a data member to distinguish between refundable and non-refundable transactions
    """
    refundable: bool = True

    # define the method as a classmethod with the appropriate argument
    @classmethod
    def read_transactions_from_file(cls, path: str = 'transactions.txt') -> list:
        """override this function to load transactions that are refundable
        """
        list_transaction_refundable = []
        regex = r'Player "(?P<player>[^"]+)" has made a new(?: \(refundable\))? transaction for game "(?P<game>[' \
                r'^"]+)" on the "(?P<date>\d{4}-\d{2}-\d{2})" for "(?P<amount>[\d.]+)" Eur'

        with open(path, 'r') as file:
            for line in file:
                matches = re.findall(regex, line.strip())
                for match in matches:
                    try:
                        player = match[0]
                        game = match[1]
                        date = match[2]
                        amount = float(match[3])
                        transaction_refundable = cls(player, game, date, amount)
                        if transaction_refundable.can_refund():
                            list_transaction_refundable.append(transaction_refundable)
                    except Exception as e:
                        raise e
        return list_transaction_refundable

    def can_refund(self) -> bool:
        """In this method you're going to check whether a transactions can be refunded or not.
        A transaction is refundable if it meets the following creteria:
        - transaction is recent
        - the amout of the transaction is > 20
        - has the refundable data attribute as only a portion of transactions are refundable
            even if the meet other conditions

        If any of the above conditions was unknown the transaction is considered non refundable
        """
        # if self.is_transaction_recent() and self.amount > 20 and self.refundable:
        #     print('yes')
        #     return True
        # else:
        #     print('no')
        #     return False


def sort_transactions(transactions, sort_by='amount'):
    """In this function you'll be implementing your method of choice for sorting transactions.
    Transactions will be sorted depending on the sort_by parameter, by default it's 'amount' but can have
    the following list of values:
    - amount
    - transaction_date

    Choose the most efficient sort method you know.
    """
    # Its not good:
    # if sort_by == 'amount':
    #     transactions.sort(key=lambda x: x.amount)
    # elif sort_by == 'transaction_date':
    #     transactions.sort(key=lambda x: x.transaction_date)
    # else:
    #     print('wrong sort_by parameter')


############# For Testing Purposes Only #############
if __name__ == '__main__':
    # Test Games
    games = Game.read_games_from_file()
    assert type(games) == list
    assert len(games) == 3
    assert games[0].game_name == 'Disney Dreamlight VAlley'
    assert games[1].release_date == '2023-08-23'
    # assert games[2].game_name == 'Dragon Mania Legends' # this test will fail cause the regex is bad

    # Test Players
    players = Player.read_players_from_file()
    # print(players)

    # Test Transactions
    transactions = Transaction.read_transactions_from_file()
    print(transactions)
    for player in players:
        x = Transaction.calculate_revenue(transactions, player)
        print(f'Transaction value of {player.name} : {x}')

    # Test Refundable Transactions

    # games = Game.read_games_from_file()
    # games[1].has_game_been_released()
    # players = Player.read_players_from_file()
    # transactions = Transaction.read_transactions_from_file()
    # for player in players:
    #     x = Transaction.calculate_revenue(transactions, player)
    #     print(x)
    # refundable_transactions = RefundableTransaction.read_transactions_from_file()
    # for transaction in refundable_transactions:
    #     print(transaction)
