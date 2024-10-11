class GameLobbyManager:
    def __init__(self):
        self.available_lobbies = []
        self.game_room_requests = []
        self.undo_stack = []

    def add_lobby(self, lobby_name):
        self.available_lobbies.append(lobby_name)
        print(f"Lobby '{lobby_name}' added.")

    def remove_lobby(self, lobby_name):
        if lobby_name in self.available_lobbies:
            self.available_lobbies.remove(lobby_name)
            print(f"Lobby '{lobby_name}' removed.")
        else:
            print(f"Lobby '{lobby_name}' not found.")

    def request_game_room(self, player_name, lobby_name):
        if lobby_name in self.available_lobbies:
            self.game_room_requests.append((player_name, lobby_name))
            print(f"Player '{player_name}' requested room in '{lobby_name}'.")
        else:
            print(f"Lobby '{lobby_name}' is not available.")

    def undo_last_entry(self):
        if self.undo_stack:
            last_entry = self.undo_stack.pop()
            print(f"Undoing last entry: {last_entry}")
        else:
            print("No entries to undo.")

    def join_lobby(self, player_name, lobby_name):
        if lobby_name in self.available_lobbies:
            self.undo_stack.append((player_name, lobby_name))
            print(f"Player '{player_name}' joined '{lobby_name}'.")
        else:
            print(f"Lobby '{lobby_name}' is not available.")

    def process_requests(self):
        while self.game_room_requests:
            player_name, lobby_name = self.game_room_requests.pop(0)
            self.join_lobby(player_name, lobby_name)

    def list_available_lobbies(self):
        if self.available_lobbies:
            print("Available Lobbies:")
            for lobby in self.available_lobbies:
                print(f"- {lobby}")
        else:
            print("No available lobbies.")

def main():
    manager = GameLobbyManager()

    while True:
        print("\nCommands: \n1. add \n2. remove \n3. request \n4. join \n5. list \n6. undo \n7. process\n8. exit")
        command = input("Enter command: ").strip().lower()

        if command == "1":
            lobby_name = input("Enter lobby name: ")
            manager.add_lobby(lobby_name)

        elif command == "2":
            lobby_name = input("Enter lobby name: ")
            manager.remove_lobby(lobby_name)

        elif command == "3":
            player_name = input("Enter player name: ")
            lobby_name = input("Enter lobby name: ")
            manager.request_game_room(player_name, lobby_name)

        elif command == "4":
            player_name = input("Enter player name: ")
            lobby_name = input("Enter lobby name: ")
            manager.join_lobby(player_name, lobby_name)

        elif command == "5":
            manager.list_available_lobbies()

        elif command == "6":
            manager.undo_last_entry()

        elif command == "7":
            manager.process_requests()

        elif command == "8":
            print("Exiting Game Lobby Manager.")
            break

        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
