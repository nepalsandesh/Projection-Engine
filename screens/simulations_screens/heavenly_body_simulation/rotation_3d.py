import numpy as np

# Define our initial array of 3D points
points_3d = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9],
                      [10, 11, 12]])

# Step 1: Define Rotation Matrix for Y-axis
def rotation_matrix_y(phi):
    return np.array([
        [np.cos(phi), 0, np.sin(phi)],
        [0, 1, 0],
        [-np.sin(phi), 0, np.cos(phi)]
    ])
    
def rotation_matrix_x(phi):
    return np.array([
        [1, 0, 0],
        [0, np.cos(phi), -np.sin(phi)],
        [0, np.sin(phi), np.cos(phi)]
    ], dtype=np.float32)
    
def rotation_matrix_z(phi):
    return np.array([
        [np.cos(phi), -np.sin(phi), 0],
        [np.sin(phi), np.cos(phi), 0],
        [0, 0, 1]
    ], dtype=np.float32)

# Step 2: Define Perspective Projection Matrix
# fov = np.radians(150)  # Field of view in radians, Adjust this value to control the zoom level

distance = 10.0  # Distance from the center point
view_width = 1920.0  # Width of the viewport (screen)

fov = 2 * np.arctan(view_width / (2 * distance))
# fov = 1

aspect_ratio = 1920/1080   # Aspect ratio of viewport
near = 0.1            # Near clipping plane
far = 100.0           # Far clipping plane

projection_matrix = np.array([
    [1 / (aspect_ratio * np.tan(fov / 2)), 0, 0, 0],
    [0, 1 / np.tan(fov / 2), 0, 0],
    [0, 0, -(far + near) / (far - near), -2 * far * near / (far - near)],
    [0, 0, -1, 0]
])

# Step 3: Apply Rotation and Perspective Projection
phi = np.radians(30)  # Rotation angle around y-axis

# Apply rotation to each point
rotated_points = np.dot(points_3d, rotation_matrix_y(phi).T)

# Extend rotated points with homogeneous coordinates
homogeneous_rotated_points = np.hstack((rotated_points, np.ones((rotated_points.shape[0], 1))))

# Apply perspective projection
projected_points = np.dot(homogeneous_rotated_points, projection_matrix.T)

# Normalize projected points by dividing by the homogeneous coordinate
projected_points = projected_points[:, :3] / projected_points[:, 3:]

# Print the results
# print("Original Points:\n", points_3d)
# print("Rotated Points:\n", rotated_points)
# print("Projected Points:\n", projected_points)


# Normalize projected points to (x, y) coordinates
projected_points_x_y = projected_points[:, :2]
# Print the (x, y) coordinates
# print("Projected (x, y) Coordinates:\n", projected_points_x_y)

# Adjust (x, y) coordinates to screen dimensions
projected_points_x_y[:, 0] = (projected_points_x_y[:, 0] + 1) * (1920 / 2)
projected_points_x_y[:, 1] = (projected_points_x_y[:, 1] + 1) * (1080 / 2)



# def get_projected_points(points_3d, phi, distance):
#     distance = distance
#     view_width = 1920.0 
#     fov = 2 * np.arctan(view_width / (2 * distance))
#     aspect_ratio = 1920/1080   # Aspect ratio of viewport
#     near = 0.1            # Near clipping plane
#     far = 100.0           # Far clipping plane
#     projection_matrix = np.array([
#         [1 / (aspect_ratio * np.tan(fov / 2)), 0, 0, 0],
#         [0, 1 / np.tan(fov / 2), 0, 0],
#         [0, 0, -(far + near) / (far - near), -2 * far * near / (far - near)],
#         [0, 0, -1, 0]
#     ])
#     rotated_points = np.dot(points_3d, rotation_matrix_y(phi).T) 
#     homogeneous_rotated_points = np.hstack((rotated_points, np.ones((rotated_points.shape[0], 1))))
#     projected_points = np.dot(homogeneous_rotated_points, projection_matrix)
#     # print("projected_points : \n", projected_points)
#     projected_points[:, 3][projected_points[:, 3] == 0] = 1e-6
#     projected_points = projected_points[:, :3] / projected_points[:, 3:]
#     projected_points_x_y = projected_points[:, :2]
#     # # Adjust (x, y) coordinates to screen dimensions
#     projected_points_x_y[:, 0] = (projected_points_x_y[:, 0] + 1) * (1920 / 2)
#     projected_points_x_y[:, 1] = (projected_points_x_y[:, 1] + 1) * (1080 / 2)
#     return projected_points_x_y


def custom_projection_matrix(distance, rotated_points):
    z = 1 / (distance - rotated_points[:, 2])
    
    projected_points = rotated_points[:, :2] * z[:, np.newaxis]
    
    return projected_points
    
    
# def get_projected_points(points_3d, phi, distance=500, scale=1000, rotate_x=False, rotate_y=False, rotate_z=False):
#     rotated_points = points_3d
#     if rotate_y == True:
#         rotated_points = np.dot(rotated_points, rotation_matrix_y(phi).T)
#     if rotate_x == True:
#         rotated_points = np.dot(rotated_points, rotation_matrix_x(phi).T)
#     if rotate_z == True:
#         rotated_points = np.dot(rotated_points, rotation_matrix_z(phi).T)
#     projected_points = custom_projection_matrix(distance, rotated_points)
#     x = projected_points[:, 0] * scale + (1920/2)
#     y = projected_points[:, 1] * scale + (1080/2)
#     points = np.array([x, y]).T
#     # print("points : \n", points)
#     return points



def get_projected_points(points_3d, angle_x, angle_y, angle_z, distance=500, scale=1000):
    rotated_points = points_3d
    rotated_points = np.dot(rotated_points, rotation_matrix_x(angle_x).T)
    rotated_points = np.dot(rotated_points, rotation_matrix_y(angle_y).T)
    rotated_points = np.dot(rotated_points, rotation_matrix_z(angle_z).T)
    projected_points = custom_projection_matrix(distance, rotated_points)
    x = projected_points[:, 0] * scale + (1920/2)
    y = projected_points[:, 1] * scale + (1080/2)
    points = np.array([x, y]).T
    # print("points : \n", points)
    return points