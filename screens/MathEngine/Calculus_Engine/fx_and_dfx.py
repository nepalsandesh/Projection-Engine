import numpy as np
import sympy as sym
from numba import jit, njit
# import pygame 

@jit()
def Get_tangent_coordinates(fa, dfa, xx, x_point):
    """Returns the tangent line coordinates of a function at given x-point"""
    tanline = dfa * (xx - x_point) + fa
    return (np.array([xx, -tanline]).T).astype(float)
    



class FunctionAndDerivative:
    """Class for computation and rendering of a function, its derivative,
        and tangent line at a point.
        
        Parameters :
            expression : one variable function or polynomial, dtype = str
            x_array : x-axis array, dtype = Ndarray 1dim
                    default : np.linspace(-10, 10, 203)
            
    """

    def __init__(self,expression, x_array=np.linspace(-10,10,2023)):
        self.x = sym.symbols('x')
        self.xx = np.array(x_array) 
        self.f = sym.parsing.sympy_parser.parse_expr(str(expression))
        self.df = self.get_derivative()
        self.f_fn = sym.lambdify(self.x, self.f)(self.xx)
        self.df_fn = sym.lambdify(self.x, self.df)(self.xx)
        self.scale = 50
        

    def get_function_coordinates(self):
        """Returns the array of coordinates of function"""
        coordinates = np.array([self.xx, self.f_fn]).T
        return coordinates 

    
    def get_derivative_coordinates(self):
        """Returns the array of coordinates of derivative of a function"""
        coordinates = np.array([self.xx, self.df_fn]).T
        return coordinates

    
    def get_tangent_coordinates(self, x_point):
        """Returns the tangent line coordinates of a function at given x-point"""
        fa = np.float_(self.f.subs(self.x, x_point, evaluate=True ))
        dfa = np.float_(self.df.subs(self.x, x_point, evaluate=True))
        tanline = dfa * (self.xx - x_point) + fa
        return (np.array([self.xx, -tanline]).T).astype(float)


    def get_tangent_point(self, x_point):
        return np.array([x_point, self.f.subs(self.x, x_point)])


    def get_derivative(self):
        """Returns derivative of a function or expression"""
        function_derivative = sym.diff(self.f)
        return function_derivative




class WindowCoordinante(FunctionAndDerivative):
    """A child class of FunctionAndDerivative. \
        We can get Windoow Coordinate from real Cartesian Coordinate"""
        
    def __init__(self, RESOLUTION, SCALE, expression, x_array=np.linspace(-10,10,203)):
        self.RESOLUTION = RESOLUTION
        self.SCALE = SCALE
        self.expression = expression
        self.x_array = x_array
        
        super().__init__(expression=expression, x_array=x_array)
        
        
    def get_function_coordinates(self):
        cartesian_coordinate = super(WindowCoordinante, self).get_function_coordinates()
        cartesian_coordinate[:,0] = cartesian_coordinate[:,0] * self.SCALE + 1920//2
        cartesian_coordinate[:,1] = -cartesian_coordinate[:,1] * self.SCALE + 540
        return cartesian_coordinate
    
    def get_derivative_coordinates(self):
        cartesian_coordinates = super(WindowCoordinante, self).get_derivative_coordinates()
        cartesian_coordinates[:,0] = cartesian_coordinates[:,0] * self.SCALE + 1920//2
        cartesian_coordinates[:,1] = -cartesian_coordinates[:,1] * self.SCALE + 540
        return cartesian_coordinates
    
    def get_tangent_coordinates(self, x_point):
        cartesian_coordinate = super(WindowCoordinante, self).get_tangent_coordinates(x_point)
        cartesian_coordinate[:,0] = cartesian_coordinate[:,0]  * self.SCALE + 1920//2
        cartesian_coordinate[:,1] = cartesian_coordinate[:,1] * self.SCALE + 540
        return cartesian_coordinate
        
    def get_tangent_point(self, x_point):
        tangent_point = super(WindowCoordinante, self).get_tangent_point(x_point)
        return np.array([tangent_point[0] * self.SCALE + 1920//2, -tangent_point[1] * self.SCALE + 540]).astype(float)
        