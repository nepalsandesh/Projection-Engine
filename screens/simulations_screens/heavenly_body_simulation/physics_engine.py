import numpy as np


def magnitude(arr):
    """Returns the magnitide of the vector.
    """
    return np.sqrt(arr[0]**2 + arr[1]**2 + arr[2]**2)

def unit_vector(arr):
    """Computes and returns unit vector."""
    mag = magnitude(arr=arr)
    return arr/mag



class PhysicsEngine:
    def __init__(self):
        self.bodies = None
        
    def compute_force_vectors(self, bodies):
        self.bodies  = np.array(bodies)
        for body in self.bodies:
            body.position = np.array([body.position[0], body.position[1], body.position[2]])
        
        distance_list = []
        force_list = []
        net_force = []
        
        # computing distance vectors
        for primary_body in self.bodies:
            temp = []
            for secondary_body in self.bodies:
                distance = secondary_body.position - primary_body.position
                temp.append(distance)
            distance_list.append(temp)
        distance_list = np.array(distance_list)
        # print("distance list : \n", distance_list)    
            
        
        # computing gravitational force
        for i, primary_body in enumerate(self.bodies):
            temp = []
            for j, secondary_body in enumerate(self.bodies):
                # compute the distance and its magnitude between two bodies
                distance = secondary_body.position - primary_body.position
                dist_mag = magnitude(distance)

                # Check if the distance is non-zero before calculating the force
                if dist_mag != 0:
                    force = 6.67e-11 * primary_body.mass * secondary_body.mass / dist_mag**2
                    force = force * unit_vector(distance)
                    temp.append(force)
                else:
                    temp.append(np.array([0.0, 0.0, 0.0]))
            force_list.append(temp)
        force_list = np.array(force_list)
    
        for obj in force_list:
            net_force.append(obj.sum(axis=0))
            
        return net_force
    
    