# Open a file in write mode. If file doesn't exist, it will be created.
file = open("example.txt", "w")

# Write some content to the file
file.write("Hello, this is a sample text.\n")
file.write("This demonstrates writing to a file in Python.\n")
file.write("You can add as many lines as you want.")

# Close the file to save changes
file.close()

print("Content has been written to example.txt")
