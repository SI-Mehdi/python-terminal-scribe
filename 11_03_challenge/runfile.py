import argparse
import time
from canvas import Canvas
from canvas_axis import CanvasAxis 
from plot_scribe import PlotScribe 
from random_walk_scribe import RandomWalkScribe
from robot_scribe import RobotScribe
from scribe import TerminalScribe

parser = argparse.ArgumentParser()

parser.add_argument('--file', '-f', required=True, help="The target JSON file to run without the .json extension")

args = parser.parse_args()

print(f'Running {args.file}.json')
time.sleep(3)
canvas = Canvas.fromFile(args.file, globals())
canvas.go()