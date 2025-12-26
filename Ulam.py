import math
import random
import matplotlib.pyplot as plt
from typing import Optional

class Ulam():
    def __init__(self, start: Optional=None, step_function: Optional=None):
        self.start = start
        self.step_function = step_function
        # Setting Central value to 1 unless other supplied
        if start == None:
            self.start = 1

        # Setting step function to identity unless other supplied
        if step_function == None:
            self.step_function = lambda N : N

    # Returns the coordinates of N in Ulam's spiral
    def invUlam(self, N):
        #Deal with initial value problem
        N = N - self.start + 1
        
        n = math.floor((math.isqrt(N)-1)/2)
        (x, y) = (n, -1 * n)
        r = N - (2*n + 1)**2
        if r == 0:
            return (x, y)
        x = x + 1
        r = r - 1
        y = y + min([2*n + 1, r])
        r = r - min([2*n + 1, r])
        if r == 0:
            return (x, y)
        x = x - min([2*n + 2, r])
        r = r - min([2*n + 2, r])
        if r == 0:
            return (x, y)
        y = y - min([2*n + 2, r])
        r = r - min([2*n + 2, r])
        if r == 0:
            return (x, y)
        return (x + r, y)

    # Returns the number at location (x, y) in Ulam's Spiral
    def Ulam(self, x, y):
        m = max([abs(x), abs(y)])
        N = (2*m + 1)**2
        if y == -1 * m: #South
            N = N - (m - x)
            return self.step_function(N + self.start - 1)
        else:
            N = N - 2*m

        if x == -1 * m: #West
            N = N - (m + y)
            return self.step_function(N + self.start - 1)
        else:
            N = N - 2*m

        if y == m: #North
            N = N - (m + x)
            return self.step_function(N + self.start - 1)
        else:
            N = N - 2*m

        if x == m: #East
            N = N - (m - y)
            return self.step_function(N + self.start - 1)

    # Generates a plot of Ulam's spiral marking only those numbers N for which choice_rule(N) is true
    # in the region x_0 <= x < x+0 + width, y_0 <= y < y_0 + height
    def see(self, choice_rule, x_0, y_0, width, height, size: Optional=2):
        X = []
        Y = []
        for x in range(x_0, x_0 + width):
            for y in range(y_0, y_0 + height):
                if choice_rule(self.Ulam(x,y)):
                    X.append(x)
                    Y.append(y)
        plt.scatter(X, Y, s=size)
        plt.xlim(x_0, x_0 + width)
        plt.ylim(y_0, y_0 + height)
        plt.title("Ulam's Spiral: Segment " + str([x_0, x_0 + width - 1]) + "X" + str([y_0, y_0 + height - 1]))
        plt.show()
        return
    
    # Generates a plot of the values given in the list choices in the same region as see(). 
    def see2(self, choices, x_0, y_0, width, height, size: Optional=2):
        X = []
        Y = []
        for val in choices:
            (x, y) = invUlam(val)
            if x_0 <= x and x <= x_0 + width and y_0 <= y and y <= y_0 + height:
                X.append(x)
                Y.append(y)
                
        plt.scatter(X, Y, s=size)
        plt.xlim(x_0, x_0 + width)
        plt.ylim(y_0, y_0 + height)
        plt.title("Ulam's Spiral: Segment " + str([x_0, x_0 + width - 1]) + "X" + str([y_0, y_0 + height - 1]))
        plt.show()
        return
            

    # Creates a list of all numbers that are the sum of numbers which can be covered by any one given polyomino,
    # one of them at most N
    def poly_place(self, polyominoes, N, mode: Optional="additive"):
        if (not mode == "additive") and (not mode == "multiplicative"):
            print("Error, poly_place() only has modes `additive' and `multiplicative', not " + mode)
            return []
        constructible = []
        for n in range(1, N + 1):
            (x_0, y_0) = self.invUlam(n)
            for poly in polyominoes:
                for (i, j) in poly:
                    summe = 0
                    produkt = 1
                    for (k, l) in poly:
                        p = self.Ulam(x_0 + k - i, y_0 + l - j)
                        if mode == "additive":
                            summe = summe + p
                        else:
                            produkt = produkt * p        
                    if mode == "additive":
                        constructible.append(summe)
                    else:
                        constructible.append(produkt)
        constructible.sort()

        copy = [constructible[0]]
        #Remove duplicates
        for i in range(1, len(constructible)):
            if copy[len(copy) - 1] != constructible[i]:
                copy.append(constructible[i])
        return copy

# Returns a function f(N) that returns True if N is of the form N=a*n^2+b*n+c for some n, False else.
# Works by quadratic formula. 
def quadratic_choice(a, b, c):
    return lambda N : b**2 - 4 * a * (c - N) > 0 and (float.is_integer((-1 * b + math.sqrt(b**2 - 4 * a * (c - N)))/(2 * a)) or float.is_integer((-1 * b - math.sqrt(b**2 - 4 * a * (c - N)))/(2 * a)))

# Tests Ulam and invUlam against each other
def test():
    classic_spiral = Ulam()
    
    #Small Tests
    for N in range(1, 10000):
        (x, y) = invUlam(N)
        assert N == Ulam(x, y)
    for x in range(1,100):
        for y in range(1, 100):
            assert (x, y) == invUlam(Ulam(x, y))

    # Big Tests
    for i in range(1, 100000):
        w = random.randint(-1000000000000,1000000000000)
        z = random.randint(-1000000000000,1000000000000)
        N = random.randint(1,1000000000000)
        (x, y) = invUlam(N)
        assert N == Ulam(x, y)
        #print([[w,z],Ulam(w,z),invUlam(Ulam(w,z))])
        assert (w, z) == invUlam(Ulam(w, z))

