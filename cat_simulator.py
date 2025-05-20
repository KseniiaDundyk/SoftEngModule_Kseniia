# cat_simulator.py

import argparse

def feed_cat(cat_name, food)
    """
    Simulates feeding a cat. Cats are notoriously picky.

    Parameters:
        cat_name : str
            The name of the cat.
        food : str
            The type of food being offered to the cat.

    Returns:
        None
    """
    favorite_foods = ["tuna", "chicken", "ice cream", "cardboard (only at 3am)"]

    print(f"{cat_name} sniffs the {food}... 👃🐾")

    if food in favorite_foods:
        print(f"{cat_name} devours the {food} 🍽️ and immediately knocks over a glass. 💥🥛")
    elif food == "dog food":
        print(f"{cat_name} looks personally offended 😾 and knocks your phone off the table. 📱💥")
    else:
        print(f"{cat_name} stares at you in judgment 👁️👁️ and walks away. 🚶‍♂️🐈")

def nap_time(cat_name, hours):
    """
    Simulates the cat taking a nap.

    Parameters:
        cat_name : str
            The name of the cat.
        hours : int
            The number of hours the cat naps.

    Returns:
        None
    """
    if hours == 0:
        print(f"{cat_name} hisses loudly and knocks everything off your desk. 😾💢🖥️📚💥")
        print("You dare suggest a nap with ZERO hours?! Unacceptable.")
        return    
    print(f"{cat_name} curls up in a sunbeam for a {hours} hour nap. 🌞🛏️😴")

    if hours > 4:
        print(f"{cat_name} wakes up and demoands snacks! 😼📢🧱")
    else:
        print(f"{cat_name} dreams of world domination. 🧠🌍🐈‍⬛")
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cat Simulator: Feed or nap your cat from the command line.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Feed subcommand
    feed_parser = subparsers.add_parser("feed", help="Feed a cat.")
    feed_parser.add_argument("cat_name", type=str, help="Name of the cat.")
    feed_parser.add_argument("food", type=str, help="Food to offer.")

    # Nap subcommand
    nap_parser = subparsers.add_parser("nap", help="Let a cat take a nap.")
    nap_parser.add_argument("cat_name", type=str, help="Name of the cat.")
    nap_parser.add_argument("hours", type=int, help="How many hours the cat naps.")

    args = parser.parse_args()

    if args.command == "feed":
        feed_cat(args.cat_name, args.food)
    elif args.command == "nap":
        nap_time(args.cat_name, args.hours)

