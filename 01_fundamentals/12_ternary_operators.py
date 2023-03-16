# Ternary operators
its_ranning = True

print("I'm with my clothes " + ('dry', 'wet')[its_ranning])
print("I'm with my clothes " + ('wet' if its_ranning else 'dry'))
