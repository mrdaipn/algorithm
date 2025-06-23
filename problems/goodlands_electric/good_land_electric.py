def pylons(distribution_range, cities):
    """Solve the problem of finding the minimum number of installed plants needed to cover all cities.

    Args:
        distribution_range (int): The range of each plant can cover.
        cities (list of int): A list where 1 indicates a city is suitable for plant, otherwise 0."""
    start_index = answer = 0
    while start_index < len(cities):
        candidate = find_possible_farest_installed_plant(start_index, distribution_range, cities)
        if candidate == -1:
            return -1
        
        answer += 1
        start_index = calculate_next_start_index(candidate, distribution_range, cities)
    return answer

def find_possible_farest_installed_plant(start_index, distribution_range, cities):
    candidate = min(start_index + distribution_range - 1, len(cities) - 1) 
    while candidate >= max(0, start_index - distribution_range + 1) and cities[candidate] == 0:
        candidate -= 1
    if candidate < 0 or candidate < start_index - distribution_range + 1:
        return -1
    
    return candidate

def calculate_next_start_index(candidate, distribution_range, cities):
    return min(candidate + distribution_range, len(cities))
