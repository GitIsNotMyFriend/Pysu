# Pysu
A pygame-based rhythm game wrriten in Python 2.7 that can read .osu file formats ( Osu!mania beatmaps format ).
This game was written as a school-project which was intended to be handed in 2 weeks from the assignment's handing.
The game's current state doesn't allow you to do much as I didn't have enough time to add user interaction due to bug handling.
( The feature above might be added in the future but the current state is still nice to watch )

## Requirements
You will need:
- Python 2.7
- Pygame library

## Installation
1. Clone the repository, preferably cloning the 'experimental' branch: `git clone https://github.com/GitIsNotMyFriend/Pysu/tree/experimental`

2. Run the "main.py" file using what ever platform you desire ( Python interpreter, Pycharm IDE, etc.. )

3. Enjoy "playing"!

## Adding a beatmap

As it was mentioned in the intro the game is able to read osu!mania beatmap format, so all you have to do
in order to add a new beatmap are the following steps:

1. Download an osu!mania beatmap ( Make sure your map is a 4 key one, the game doesn't support any other keys because it's supposed
to copy Stepmania's gamestyle rather than Osu!'s)

2.1. If you have osu installed, click on the installed file and it would create a folder in your game's directory
2.2. If you don't have osu installed, open the .osu file as rar and extract it

3. Grab the beatmap folder into the game's directory inside the beatmaps folder.

## Credits
The skin I use for the game assets is a modified version of [this skin](https://osu.ppy.sh/forum/t/512453).

I want to thank Osu!© for making readable file formats so I don't have to create my own maps for the game!
