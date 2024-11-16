## THIS PRINTS EACH TABLE ALONE
# Print times tables from 1 to 12
# for i in range(1, 13):
#     print(f"\nTimes table for {i}:")
#     print("-" * 20)
#     for j in range(1, 13):
#         print(f"{i} x {j} = {i*j}")
#     print()



## THIS PRINTS IN A TABLE FORMAT
# Print header
print("Times Tables (1-12)")
print("-" * 85)

# Print column headers
header = "   |"
for i in range(1, 13):
    header += f" {i:3} |"
print(header)
print("-" * 85)

# Print each row
for i in range(1, 13):
    row = f"{i:2} |"
    for j in range(1, 13):
        row += f" {i*j:3} |"
    print(row)
print("-" * 85)
