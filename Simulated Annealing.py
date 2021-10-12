import numpy
import matplotlib.pyplot as plt

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def get_distance(a, b):
        return numpy.sqrt(numpy.abs(a.x-b.x)+numpy.abs(a.y-b.y))

    @staticmethod
    def get_total_distance(coords):
        dist=0
        for first, second in zip(coords[:-1], coords[1:]):
            dist += Coordinate.get_distance(first,second)
        dist += Coordinate.get_distance(coords[0], coords[-1])
        return dist

if __name__ == '__main__':
    coords= []
    for i in range(10):  #range
        coords.append(Coordinate(numpy.random.uniform(), numpy.random.uniform()))

    fig = plt.figure(figsize=(10,5))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    for first, second in zip(coords[:-1], coords[1:]):
        ax1.plot([first.x, second.x], [first.y, second.y], 'b')
    ax1.plot([coords[0].x, coords[-1].x], [coords[0].y, coords[-1].y], 'b')
    for c in coords:
        ax1.plot(c.x, c.y, 'ro')

# Simulated Annealing Algorithm
    cost0 = Coordinate.get_total_distance(coords)

    T=30  #T
    factor = 0.99 #factor
    T_init = T
    for i in range(1000):  #Max
        print(i, 'cost=', cost0)

        T = T*factor
        for j in range (100):
            #Exchange two coordinates and get a new neighbour solution
            r1, r2 = numpy.random.randint(0, len(coords), size=2)

            temp = coords[r1]
            coords[r1] = coords[r2]
            coords[r2] = temp

            #Get the new cost
            cost1 = Coordinate.get_total_distance(coords)

            if cost1< cost0:
                #Accept the new solution
                cost0 = cost1
            else:
                #Accept the new (worse) solution with a given propability
                x=numpy.random.uniform()
                if x < numpy.exp((cost0-cost1/T)):
                    #Accept the solution
                    cost0 = cost1
                else:
                    #Do not accept the solution
                    temp = coords[r1]
                    coords[r1] = coords[r2]
                    coords[r2] = temp


    for first, second in zip(coords[:-1], coords[1:]):
        ax2.plot([first.x, second.x], [first.y, second.y], 'b')
    ax2.plot([coords[0].x, coords[-1].x], [coords[0].y, coords[-1].y], 'b')
    for c in coords:
        ax2.plot(c.x, c.y, 'ro')
    plt.show()
