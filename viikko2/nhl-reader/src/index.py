import requests
from player import Player 
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

class PlayerReader:
    def __init__(self):
        self.year = self.ask_year()
        self.url = f"https://studies.cs.helsinki.fi/nhlstats/{self.year}/players"
        self.response = requests.get(self.url).json()
        self.players = self.get_players()
    
    def ask_year(self):
        years = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]

        while True:
            year = Prompt.ask("Select season [cyan][2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25][/cyan]")
            if year in years:
                break
            else:
                print("Season isn't one of the available options")
            
        return year

    def get_players(self):
        players = []

        for player_dict in self.response:
            player = Player(player_dict)
            players.append(player)
        
        return players

class PlayerStats:
    def __init__(self, reader):
        self.year = reader.year
        self.players = reader.players
        self.nat = self.ask_nationality()
        self.table = Table(title=f"Top scorers of {self.nat} season {self.year}")
        self.make_table()
    
    def ask_nationality(self):
        nats = ["AUT", "CZE", "AUS", "SWE", "GER", "DEN",
                 "SUI", "SVK", "NOR", "RUS", "CAN", "LAT",
                 "BRL", "SLO", "USA", "FIN", "GBR"]

        while True:
            nat = Prompt.ask("Select nationality [cyan][AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BRL/SLO/USA/FIN/GBR][/cyan]")
            if nat.upper() in nats:
                break
            else:
                print("Nationality isn't one of the available options")
            
        return nat.upper()


    def make_table(self):
        self.table.add_column("name", justify="left", style="cyan", no_wrap=True)
        self.table.add_column("team", style="magenta")
        self.table.add_column("goals", justify="right", style="green")
        self.table.add_column("assists", justify="right", style="green")
        self.table.add_column("points", justify="right", style="green")
    
    def top_scorers_by_nationality(self):
        def sort_by(x):
            return x.goals + x.assists

        self.players.sort(reverse=True, key=sort_by)

        for player in self.players:
            if player.nationality == self.nat:
                self.table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.goals + player.assists))
        
        console = Console()
        console.print(self.table)

def main():
    reader = PlayerReader()
    stats = PlayerStats(reader)
    stats.top_scorers_by_nationality()

if __name__ == "__main__":
    main()
