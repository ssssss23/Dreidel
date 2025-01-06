import random
import time

def spin_dreidel():
    """Simulates spinning the dreidel."""
    outcomes = ["Nun", "Gimmel", "Hey", "Shin"]
    return random.choice(outcomes)

def display_state(players, pot):
    """Displays the current state of the game."""
    print("\n--- Game State ---")
    for player, coins in players.items():
        print(f"{player}: {coins} coins")
    print(f"Pot: {pot} coins\n")

def bot_turn():
    """Simulates the bot's turn, which is the same as a player's turn."""
    print("Bot's turn...")
    time.sleep(1)
    return spin_dreidel()

def main():
    print("Welcome to the Virtual Dreidel Game!")
    players = {}
    num_players = int(input("Enter the number of players (exclude bot if playing with one): "))

    # If the player wants to play against the bot, add the bot as a player
    play_with_bot = input("Do you want to play against a bot? (y/n): ").strip().lower() == "y"
    if play_with_bot:
        players["Bot"] = 10
        num_players += 1

    for i in range(1, num_players + 1):
        if play_with_bot and i == num_players:
            continue  # Skip adding the bot manually, it's already added
        name = input(f"Enter the name for player {i}: ")
        players[name] = 10

    rounds = int(input("Enter the number of rounds: "))
    pot = 10
    print("\nGame initialized!")
    time.sleep(1)

    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")
        for player in list(players.keys()):
            if player == "Bot" and play_with_bot:
                result = bot_turn()  # Bot takes its turn
            else:
                input(f"{player}'s turn! Press Enter to spin the dreidel...")
                result = spin_dreidel()  # Human player takes their turn
            
            print(f"{player} spun {result}!")

            if result == "Nun":
                print("Nothing happens.")
            elif result == "Gimmel":
                print(f"{player} wins the pot!")
                players[player] += pot
                pot = 0
            elif result == "Hey":
                half_pot = pot // 2
                print(f"{player} takes half the pot ({half_pot} coins).")
                players[player] += half_pot
                pot -= half_pot
            elif result == "Shin":
                print(f"{player} adds 1 coin to the pot.")
                players[player] -= 1
                pot += 1

            display_state(players, pot)
            time.sleep(1)

    print("\n--- Game Over! ---")
    display_state(players, pot)
    print("Thank you for playing!")

if __name__ == "__main__":
    main()