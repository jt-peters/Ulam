Dependencies:
matplotlib.pyplot
Optional

Contents:

1. A class Ulam() with syntax spiral=Ulam(start=N, step_function=f) that creates a generalized Ulam spiral with of the numbers f(N), f(N + 1), f(N + 2), ... . The class contains the following methods. If start is not given, default is 1. If step_function is not given, default is the identity lambda N : N. 
	1a. spiral.Ulam(x, y) returns the integer at the point (x, y). 
	1b. spiral.invUlam(N) returns the coordinates of the point of value N if step_function were the identity. 
	1c. spiral.see(choice_rule,x_0, y_0, width, height, size=s) creates a scatterplot of points (x, y) for which choice_rule(Ulam(x, y)) is True in the width X height region that has the bottom-left corner at (x_0, y_0). Size controls size of the point markers, if is not given, the default is 2. 
	1d. spiral.poly_place(polyominoes, N, mode=string) Polyominoes is a list of lists of cartesian coordinates, each list represents a set of points. Creates an increasing list of values that are the sum of cells covered by a translation of  polyomino in the list polyominoes. mode is either "additive" or "multiplicative"."additive" is default, else the list is of values that are the product of covered sets. 

2. quadratic_choice(a, b, c) Returns a choice function that returns true if N is of the form a*n^2+b*n+c for an integer n. 