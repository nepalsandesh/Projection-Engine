import numpy as np
import pygame

from .physics_engine import PhysicsEngine
from .rotation_3d import get_projected_points
from .ui_components import *

def rotate_y(theta):
    return np.array([
        [np.cos(theta), 0, -np.sin(theta)],
        [0, 1, 0],
        [np.sin(theta), 0, np.cos(theta)]
    ])
    

def get_window_coordinates(point_array):
    """point array : [x, y, z]
        Returns [x+1920//2, y+1080//2, z]
    """
    if point_array.ndim == 1:
        point_array = [point_array[0] + 1920//2, point_array[1] + 1080//2, point_array[2]]
        return np.array(point_array)
    
    elif point_array.ndim == 2:
        x = point_array[:, 0] + 1920//2
        y = point_array[:, 1] + 1080//2
        z = point_array[:, 2]
        return np.array([x,y,z]).T


class Body:
    """Body Class"""
    def __init__(self, position, mass, color=np.random.randint(0, 255, 3), radius=10, TIME_DELAY=0.009):
        self.position = position
        self.mass = mass
        self.color = color
        self.radius = radius
        self.TIME_DELAY = TIME_DELAY
        self.velocity = np.zeros(3)
        self.force = np.zeros(3)
        self.position_history = np.array([self.position])
    
    def add_velocity(self, velocity_array):
        self.velocity += velocity_array
        
    def add_force(self, force_array):
        self.force += force_array
        
    def move(self):
        self.velocity = self.velocity + (self.force / self.mass) * self.TIME_DELAY
        self.position = self.position + self.velocity * self.TIME_DELAY
    
    def append_position(self, position):
        self.position_history = np.append(self.position_history, np.array([position]), axis=0)
        


class RenderEngine:
    """Engine Renderer Class
    """
    def __init__(self, screen, clock, FPS, bodies, save_image=False, display_logo=False):
        # pygame.init()
        self.width, self.height = 1920, 1080
        self.screen = screen
        self.clock = clock
        self.FPS = 60
        self.font = pygame.font.Font('freesansbold.ttf', 15)
        
        self.distance = 4400
        self.scale = 2200
        
        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0
        
        self.render_orbit = False       
        
        self.save_image = save_image
        self.frame_count = 0
        self.engine = PhysicsEngine()
        self.running = True
        
        # self.display_logo = display_logo
        # self.logo = pygame.image.load("VORTEX_LAB_logo.png")
        # self.logo = pygame.transform.rotozoom(self.logo, 0, 0.35)
        
        self.rotation_speed = 0.004
        self.bodies = [Body(
            position=np.random.randint(-500, 500, 3),
            mass=np.random.randint(5, 20) * 6e15,
            color=np.random.randint(0, 256, 3)
                ) for i in range(1)]
        
        self.bodies.append(Body(
            position=np.zeros(3),
            mass= 6e15 * 400,
            radius=40,
            color=np.array([255, 255, 255])
            ))

        for body in self.bodies:
            body.add_velocity(np.random.randint(-500, 500, 3))
            
        self.bodies = np.array(self.bodies, dtype=object)
        
        
        
    def check_events(self):
        """Input Events Handling Function"""
        [exit() for event in pygame.event.get() if event.type==pygame.QUIT]
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.running = False
            

        
    # def rotate(self, angle):
    #     bodies_position = np.array([body.position for body in bodies])
    #     rotated_points = np.dot(rotate_y(angle), bodies_position.T)
    #     rotated_points = rotated_points.T
        
    #     for i, body in enumerate(bodies):
    #         window_coordinate = get_window_coordinates(rotated_points[i])
    #         if (window_coordinate[0] >= 0 and window_coordinate[0] <= 1920) and (window_coordinate[1] >= 0 and window_coordinate[1] <= 1080):
    #             pygame.draw.circle(self.screen, body.color, window_coordinate[:2], body.radius)
            
    #         orbit_points = body.position_history
    #         rotated_orbit_points = np.dot(rotate_y(angle), orbit_points.T)
    #         rotated_orbit_points = rotated_orbit_points.T
    #         rotated_orbit_points = get_window_coordinates(rotated_orbit_points)[:, :2]
            
    #         pygame.draw.lines(self.screen, body.color, False, rotated_orbit_points, 1)
    
    
    def rotate(self):
        """Rotation Function"""
        bodies_position = np.array([body.position for body in self.bodies])
        # projected_points = get_projected_points(bodies_position, self.angle, self.distance, self.scale, rotate_y=True)
        projected_points = get_projected_points(
            points_3d=bodies_position,
            angle_x=self.angle_x,
            angle_y=self.angle_y,
            angle_z=self.angle_z,
            distance=self.distance,
            scale=self.scale            
        )
        
        
        for i, body in enumerate(self.bodies):
            point = projected_points[i]
            if (point[0] >= 0 and point[0] <= 1920) and (point[1] >= 0 and point[1] <= 1080):
                pygame.draw.circle(self.screen, body.color, point, body.radius)

                if self.render_orbit:
                    orbit_points = body.position_history
                    projected_orbit_points = get_projected_points(orbit_points, self.angle_x, self.angle_y, self.angle_z, self.distance,  self.scale)
                    pygame.draw.lines(self.screen, body.color, False, projected_orbit_points, 2)


        
        
        
        if self.angle_x >= 2* np.pi:
            self.angle_x = 0
        if self.angle_y >= 2* np.pi:
            self.angle_y = 0
        if self.angle_z >= 2* np.pi:
            self.angle_z = 0
        if self.angle_x <= -2* np.pi:
            self.angle_x = 0
        if self.angle_y <= -2* np.pi:
            self.angle_y = 0
        if self.angle_z <= -2* np.pi:
            self.angle_z = 0
    
    def update(self):
        net_force = self.engine.compute_force_vectors(bodies=self.bodies)
        for i, body in enumerate(self.bodies):
            body.force = net_force[i]
            body.move()
            body.append_position(body.position)
            

    def draw(self):       
        self.rotate()
            
            
    def render_ui(self):
        panel.render(self.screen)
        distance_text_UI.render(self.screen, f"{self.distance}")
        scale_text_UI.render(self.screen, f"{self.scale}")
        rotate_text_UI.render(self.screen)
        fps_text_UI.render(self.screen, f"{np.round(self.clock.get_fps(), 2)}")
        
        if rotate_x_radiobutton.render(self.screen):
            self.angle_x += self.rotation_speed

        if rotate_y_radiobutton.render(self.screen):
            self.angle_y += self.rotation_speed

            
        if rotate_z_radiobutton.render(self.screen):
            self.angle_z += self.rotation_speed

            
        if display_orbit_radiobutton.render(self.screen):
            self.render_orbit = True
        else:
            self.render_orbit = False
        
        if add_body_button.Draw(self.screen):
            mass = np.random.randint(5, 20) * 6e15
            # mass = np.random.randint(4, 400) * 6e15
            self.bodies = np.append(self.bodies, 
                      Body(
                          position=np.random.randint(-500, 500, 3),
                          mass=mass,
                          color= np.random.randint(0, 256, 3),
                          radius= mass / 6e15
                        #   radius= 10
                      ))
            idx = self.bodies.size - 1
            self.bodies[idx].add_velocity(np.random.randint(-500, 500, 3))
            self.bodies = self.bodies[::-1]

        if distance_plus_button.is_double_clicked(self.screen):
            self.distance += 22
        if distance_minus_button.is_double_clicked(self.screen):
            self.distance -= 22

        if scale_plus_button.is_double_clicked(self.screen):
            self.scale += 22
        if scale_minus_button.is_double_clicked(self.screen):
            self.scale -= 22
            
        display_orbit_text_UI.render(self.screen)
        rotation_speed_text_UI.render(self.screen)
        if rotation_speed_plus_button.is_double_clicked(self.screen):
            self.rotation_speed += 0.0001
        if rotation_speed_minus_button.is_double_clicked(self.screen):
            self.rotation_speed -= 0.0001
            
        if save_images_button.render(self.screen):
            self.save_image = True
        else:
            self.save_image = False
            
    
    def run(self):
        while self.running:
            self.screen.fill((0,0,0))
            self.clock.tick(self.FPS)
            self.check_events()        
            self.update()
            self.draw()
            self.render_ui()
            self.bodies[-1].position = np.zeros(3)
            
            # if self.display_logo:
            #     self.screen.blit(self.logo, (1740, 1000))
            
            # # image save
            # if self.save_image:
            #     filename = "captures/observe/%08d.png" % (self.frame_count)
            #     pygame.image.save(self.screen, filename)
            #     print(f"Frame : {self.frame_count}")
            #     self.frame_count += 1  
                
            # # print("Distance: %g, Scale: %g, FPS: %g, Rotation_speed: %g"%(self.distance, self.scale, self.clock.get_fps(), self.rotation_speed))
            # print("angle_x: %g, angle_y:%g angle_z: %g, rotation_speed: %g"%(self.angle_x, self.angle_y, self.angle_z, self.rotation_speed))
        
            
            pygame.display.flip()
    



# ------------------------- Parameters ----------------------------
bodies = [Body(
    position=np.random.randint(-500, 500, 3),
    mass=np.random.randint(5, 20) * 6e15,
    color=np.random.randint(0, 256, 3)
) for i in range(1)]

bodies.append(Body(
    position=np.zeros(3),
    mass= 6e15 * 400,
    radius=40,
    color=np.array([255, 255, 255])
))

for body in bodies:
    body.add_velocity(np.random.randint(-500, 500, 3))




# -------------------------- Run --------------------------------

# if __name__ == "__main__":
#     bodies = np.array(bodies, dtype=object)
#     engine = PhysicsEngine()
#     app = RenderEngine(bodies=bodies, save_image=False, display_logo=True)
#     app.run()
    
    
def render(screen, clock, FPS):
    engine = PhysicsEngine()
    app = RenderEngine(bodies=None,screen=screen, clock=clock, FPS=FPS , save_image=False, display_logo=False)
    app.run()