def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges = []  # Create an empty list to store the badges
    for name in names:
        badge = badge_maker(name)  # Create a badge for each name
        badges.append(badge)  # Add the badge to the list
    return badges  # Return the list of badges

def assign_rooms(names):
    room_assignments = []  # Create an empty list to store room assignments
    for index, name in enumerate(names, 1):
        room_assignment = f"Hello, {name}! You'll be in room {index}!"  # Add exclamation mark
        room_assignments.append(room_assignment)  # Add the assignment to the list
    return room_assignments  # Return the list of room assignments


def printer(names):
    badges = batch_badge_creator(names)  # Generate badges
    room_assignments = assign_rooms(names)  # Generate room assignments
    
    for badge in badges:
        print(badge)  # Print each badge
    
    for room_assignment in room_assignments:
        print(room_assignment)  # Print each room assignment

# Example usage:
names = ['Guido', 'Edsger', 'Ada', 'Charles', 'Alan', 'Grace']
printer(names)
