import sys

from dotenv import load_dotenv
from eval.game import Game, Player1, Player2
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO")

load_dotenv()


def main():
    # Environment Settings
    game = Game(
        render=True,
        player_1=None,
        player_2=Player2(
            nickname="Baby",
            model="yi:yi-spark",
        ),
    )
    return game.run()


if __name__ == "__main__":
    main()
