"""

    Conway's Game of Life
    
    Nadyan Suriel Pscheidt
    
    -------------------------------
    
    Copyright 2017-2019 Grant Jenks

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
    
"""

from random import choice
from turtle import *
from freegames import square

matriz = {}

def inicializa():
    "Inicializa as posições aleatoriamente"
    for x in range(-200,200,10):
        for y in range(-200,200,10):
            matriz[x,y] = False # Todas vazias
            
    for x in range(-50,50,10):
        for y in range(-50,50,10):
            matriz[x,y] = choice([True,False])  # Aleatório vazio ou não

def passo():
    """
    Calcula um passo para cada celula, de acordo com as regras:
        https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
        1 - Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        2 - Any live cell with two or three live neighbors lives on to the next generation.
        3 - Any live cell with more than three live neighbors dies, as if by overpopulation.
        4 - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    """
    vizinhos = {} # Quantidade de vizinhos de cada célula da matriz
    for x in range(-190,190,10):
        for y in range(-190,190,10):
            contador = 0
            for h in [-10,0,10]:
                for v in [-10,0,10]:
                    contador += matriz[x+h,y+v] # Ex: 2 + True = 3 // 2 + False = 1
            vizinhos[x,y] = contador

    for celula, contador in vizinhos.items():
        if matriz[celula]:
            if (matriz[celula]) and (contador < 2 or contador > 3):
                matriz[celula] = False # Regra 1 e 3
            elif (matriz[celula]) and (contador == 2 or contador == 3) 
                matriz[celula] = True # Regra 2
            elif not celulas[celula] and contador == 3:
                matriz[celula] = True # Regra 4

def desenhaTela():
    passo()
    clear()
    for (x,y), vivo in matriz.items():
        cor = 'green' if vivo else 'white'
        square(x,y,10,cor)
    update()                    # Perform a TurtleScreen update. To be used when tracer is turned off.
    ontimer(desenhaTela,100)    # Install a timer that calls fun after t milliseconds.

setup(420,420,370,0)    # Tamanho e posição da janela.
hideturtle()            # Make the turtle invisible. Hiding the turtle speeds up the drawing observably.
tracer(False)           # Turn turtle animation on/off and set delay for update drawings. If n is given, only each n-th regular screen update is really performed.
inicializa()
desenhaTela()
done()                  # Starts event loop, calling Tkinter’s mainloop function.
