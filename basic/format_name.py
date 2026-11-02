string_to_process = "   sMitH, aLeX    "

# Expected output: "Alex Smith"

name = string_to_process.strip()
last_name, first_name = name.split(",")
first_name = first_name.strip().title()
last_name = last_name.strip().title()
print(first_name + " " + last_name)