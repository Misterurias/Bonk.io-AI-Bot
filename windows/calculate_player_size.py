import numpy as np

# Radius values for each map scale (1-13)
map_scales = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
player_radii = np.array([30, 25, 20, 17, 15, 13, 12, 10, 9, 8, 7, 6, 5])

def calculate_player_size(ppm):
    # Normalize ppm to the range of map scales (1-13)
    min_ppm = 2
    max_ppm = 300
    normalized_ppm = (ppm - min_ppm) / (max_ppm - min_ppm) * (max(map_scales) - min(map_scales)) + min(map_scales)
    
    # Interpolate player radius based on normalized ppm
    player_radius = np.interp(normalized_ppm, map_scales, player_radii)
    
    # Calculate player size (area of the circle)
    player_area = np.pi * (player_radius ** 2)
    
    return player_radius, player_area

# Example usage
ppm = 8
player_radius, player_area = calculate_player_size(ppm)
print(f"Player radius for ppm {ppm}: {player_radius}")
print(f"Player area for ppm {ppm}: {player_area}")
