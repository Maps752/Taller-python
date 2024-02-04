import turtle

def dibujar_arbol(t, longitud_de_rama, nivel):
    if nivel <= 0:
        return
    else:
        t.forward(longitud_de_rama)
        t.right(20)
        dibujar_arbol(t, longitud_de_rama - 15, nivel - 1)
        t.left(40)
        dibujar_arbol(t, longitud_de_rama - 15, nivel - 1)
        t.right(20)
        t.backward(longitud_de_rama)

ventana = turtle.Screen()
ventana.bgcolor("white")

brad = turtle.Turtle()
brad.left(90)
brad.up()
brad.backward(100)
brad.down()
brad.color("green")

dibujar_arbol(brad, 100, 5)

ventana.exitonclick()
