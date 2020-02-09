from turtle import*
screen=Screen()
screen.register_shape('verycute.gif')
shape('verycute.gif')
col=["orange","limegreen","gold","plum","tomato"]
for i in range(5):
    color(col[i])
    forward(200)
    left(144)
done()
