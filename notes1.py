from cs1graphics import *
win = Canvas()
win.setBackgroundColor("skyblue")
win.setTitle("My first window")
win.setWidth(400)
win.setHeight(300)

grass = Rectangle(400, 100)
grass.setFillColor("green")
win.add(grass)
grass.move(200,250)

sun = Circle(30, Point(300,50))
sun.setFillColor("yellow")
win.add(sun)

front = Square(50, Point(100, 200))
front.setFillColor('blue')
win.add(front)
top = Polygon(Point(75,175), Point(100,150), Point(125,175))
top.setFillColor('blue')
win.add(top)
roof = Path(Point(70,180), Point(100,150), Point(130,180))
win.add(roof)
roof.setBorderWidth(4)
roof.setBorderColor('brown')
top.setBorderWidth(0)
opening = Rectangle(30,40, Point(100,205))
opening.setFillColor("black")
win.add(opening)
arch = Circle(15, Point(100,185))
arch.setFillColor("black")
win.add(arch)

tree = Layer()
trunk = Path(Point(0,0), Point(0,-20))
trunk.setBorderWidth(7)
trunk.setBorderColor('brown')
tree.add(trunk)
body = Polygon(Point(0,-100), Point(-20,-20), Point(20,-20))
body.setFillColor('darkgreen')
tree.add(body)
win.add(tree)
tree.move(200,240)
tree.rotate(10)

tree2 = tree.clone()
tree2.move(50, -10)
win.add(tree2)
tree2.flip()

animate = Text("click to animate")
animate.moveTo(200,280)
win.add(animate)
grass.wait()
from time import sleep
tree2.move(25, -5)
tree2.flip()
sleep(0.25)
tree2.move(25, -5)
tree2.flip()
sleep(0.25)
tree2.move(25, -5)
tree2.flip()
sleep(0.25)
tree2.move(25, -5)
tree2.flip()
sleep(0.25)
tree2.move(25, -5)
tree2.flip()
sleep(0.25)
tree2.move(25, -5)
tree2.flip()
sleep(0.25)
tree2.move(25, -5)
tree2.flip()
