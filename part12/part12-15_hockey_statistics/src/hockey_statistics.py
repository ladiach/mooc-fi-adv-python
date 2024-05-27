# Write your solution here
import json
    
class Player:
    def __init__(self, name:str, nationality:str, assists:int, goals:int, penalties:int, team:str, games:int):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
    
    def __str__(self):
        return f"{self.name:21}{self.team:3}{self.goals:4} + {self.assists:2} = {(self.goals+self.assists):3}"
    
    
class FileHandler:
    def __init__(self, filename:str):
        self.__filename = filename
    
    def load_file(self):
        with open(self.__filename) as f:
            all_data = f.read()
        return json.loads(all_data)
    
    
class PlayerApplication:
    def __init__(self):
        self.players = []
    
    def add_players(self, all_players:list):
        for player in all_players:
            p = Player(player["name"], player ["nationality"], player["assists"], player["goals"], player["penalties"],player["team"],player["games"])
            self.players.append(p)
    
    def help(self):
        print()
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")
    
    def search_player(self):
        name = input("name: ")
        for player in self.players:
            if player.name == name:
                print(player)
    
    def teams(self):
        teams = set([player.team for player in self.players])
        for t in sorted(teams):
            print(t)
    
    def countries(self):
        countries = set([player.nationality for player in self.players])
        for c in sorted(countries):
            print(c)
    
    def players_by_team(self):
        team = input("team: ")
        players_team = list(filter(lambda player: player.team==team, self.players))
        players_team = sorted(players_team, key=lambda p:p.assists+p.goals, reverse=True)
        for p in players_team:
            print(p)
    
    def players_from_country(self):
        country = input("country: ")
        players_country =list(filter(lambda player:player.nationality==country, self.players))
        players_country=sorted(players_country, key=lambda p:p.assists+p.goals, reverse=True)
        for p in players_country:
            print(p)
    
    def most_points(self):
        n =int(input("how many: "))
        top_players =sorted(self.players, key=lambda p:(p.assists+p.goals, p.goals), reverse = True)[:n]
        for tp in top_players:
            print(tp)
    
    def by_goals(self, player:Player):
        return [player.goals, (player.games)*-1]
    
    def most_goals(self):
        n = int(input("how many: "))
        top_goals = sorted(self.players, key=self.by_goals, reverse = True)[:n]
        for tg in top_goals:
            print(tg)
    
    def execute(self):
        if False:
            file_name = "partial.json"
        else:
            file_name = input("file name: ")
        file = FileHandler(file_name)
        all_players = file.load_file()
        print(f'read the data of {len(all_players)} players')
        self.add_players(all_players)
    
        self.help()
    
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.search_player()
            elif command == "2":
                self.teams()
            elif command == "3":
                self.countries()
            elif command == "4":
                self.players_by_team()
            elif command == "5":
                self.players_from_country()
            elif command == "6":
                self.most_points()
            elif command == "7":
                self.most_goals()
            else:
                self.help()
    
    
    
app = PlayerApplication()
app.execute()