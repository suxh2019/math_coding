'''
9/7/2025

The below code is from the website https://search.brave.com/search?q=archimedes_pi_approximation%28++python+code+example++draw+circle+and+polygaon&summary=1&conversation=b5e018ddd06a2d23d5f98a

'''

import math
import matplotlib.pyplot as plt

def archimedes_pi_approximation(iterations):
    # Start with a hexagon (6 sides) inscribed in a unit circle (radius = 1)
    n_sides = 6
    # Side length of the initial hexagon
    side_length = 1.0  # For a unit circle, the side length of a regular hexagon is 1
    
    # Store the side lengths and pi approximations
    side_lengths = []
    pi_approximations = []
    
    # Iterate to double the number of sides each time
    for i in range(iterations):
        # Calculate the perimeter of the current polygon
        perimeter = n_sides * side_length
        # Estimate pi as half the perimeter of the inscribed polygon
        pi_approx = perimeter / 2.0
        side_lengths.append(side_length)
        pi_approximations.append(pi_approx)
        
        '''Update the side length for the next iteration (2n sides)
        Using the geometric formula derived from Archimedes' method
        d_2n = sqrt(2 - 2*sqrt(1 - (d_n^2)/4)) '''
        side_length = math.sqrt(2 - 2 * math.sqrt(1 - (side_length ** 2) / 4))
        n_sides *= 2
    
    # Plot the results
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot the pi approximation convergence
    ax1.plot(range(1, iterations + 1), pi_approximations, marker='o', linestyle='-', color='b')
    ax1.axhline(y=math.pi, color='r', linestyle='--', label='True π')
    ax1.set_title('Pi Approximation Convergence')
    ax1.set_xlabel('Number of Iterations (Doubling Sides)')
    ax1.set_ylabel('Approximated Pi')
    ax1.legend()
    ax1.grid(True)
    
    '''Plot the polygon and circle
    Create a unit circle'''
    circle_angles = [i * 2 * math.pi /100 for i in range(100)]
    circle_x = [math.cos(angle) for angle in circle_angles]
    circle_y = [math.sin(angle) for angle in circle_angles]
    
    # Draw the final polygon (after all iterations)
    #final_n_sides = n_sides
    
    #change the number below to draw different polygons
    final_n_sides = 4
    
    
    
    final_side_length = side_length
    polygon_angles = [i * 2 * math.pi / final_n_sides for i in range(final_n_sides+1)]
    polygon_x = [math.cos(angle) for angle in polygon_angles]
    polygon_y = [math.sin(angle) for angle in polygon_angles]
    
    # Plot the circle and polygon
    ax2.plot(circle_x, circle_y, 'b-', linewidth=1, label='Unit Circle')
    ax2.plot(polygon_x, polygon_y, 'r-', linewidth=2, label=f'Inscribed Polygon ({final_n_sides} sides)')
    ax2.set_title('Inscribed Polygon Approximating a Circle')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.axis('equal')  # Ensure the aspect ratio is equal
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    plt.show()
    
    # Return the final approximation
    return pi_approximations[-1]

# Run the approximation
final_pi_estimate = archimedes_pi_approximation(10)
print(f"Final pi approximation after 10 iterations: {final_pi_estimate}")   