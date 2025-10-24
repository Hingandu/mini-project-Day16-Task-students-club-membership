# Example: Student Club Membership using Sets

# Create a list of students as tuples
students = [
    ("Rocky", 18),
    ("Emmanuel", 19),
    ("Phill", 17),
    ("Janet", 18),
    ("Patric", 20)
]

# Create two sets for different clubs
science_club = {"Rocky", "Janet", "Emmanuel"}
art_club = {"Emmanuel", "Rocky", "Phill"}

# Display members of each club
print("Science Club Members:", science_club)
print("Art Club Members:", art_club)

# Find members who belong to both clubs
both_clubs = science_club.intersection(art_club)
print("\nMembers in both clubs:", both_clubs)

# Find members unique to each club
only_science = science_club.difference(art_club)
only_art = art_club.difference(science_club)

print("Only in Science Club:", only_science)
print("Only in Art Club:", only_art)

# Find all members in at least one club
all_members = science_club.union(art_club)
print("\nAll Club Members:", all_members)
