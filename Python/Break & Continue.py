# Break statement
for i in "DevOps":
    print(i)
    if i == "O":
        print("found my data")
        break
print("Out of loop")

# Continue statement
for i in "DevOps":
    print(i)
    if i == "O":
        print("Found my data.")
        continue
    print(f"value of i is {i}")
print("Out of loop")