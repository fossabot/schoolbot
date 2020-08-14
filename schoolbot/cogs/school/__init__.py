import os

from .meal import Meal


def setup(bot):
    bot.add_cog(Meal(bot, os.environ["API_KEY"]))