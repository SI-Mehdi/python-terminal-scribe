from scribe import TerminalScribe
from robot_scribe import RobotScribe
from canvas import Canvas
from canvas_axis import CanvasAxis

scribe = TerminalScribe(color='green')
scribe.forward(10)
robotScribe = RobotScribe(color='yellow')
robotScribe.drawSquare(20)

canvas = CanvasAxis(40, 40, scribes=[scribe, robotScribe])

canvas.toFile('solution_file')

newCanvas = Canvas.fromFile('solution_file', globals())
newCanvas.go()
