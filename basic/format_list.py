string_to_process = "eggs,cheese,milk,bread,cereal"

# Expected Output: "EGGS | CHEESE | MILK | BREAD | CEREAL"
items = string_to_process.split(",")
for i in range(len(items)):
    items[i] = items[i].upper()
result = " | ".join(items)
print(result)