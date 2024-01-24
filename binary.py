# create function that converts binary to decimal
def binary_value(binary):
decimal = 0
for i in range(len(binary)):
if binary[i] == '1':
decimal += 2 ** (len(binary) - 1 - i)
return decimal

# create function that converts decimal to binary
def decimal_to_binary(decimal):
binary = ''
while decimal > 0:
remainder = decimal % 2
binary = str(remainder) + binary
decimal = decimal // 2
return binary

# user input
selection = input("Enter '1' for binary conversion or '2' for decimal conversion: ")

# if selection is1, convert binary to decimal
if selection == '1':
bin_input = input("Enter binary number: ")
dec_output = binary_value(bin_input)
print("The decimal equivalent is:", dec_output)

# if selection is 2, convert decimal to binary
elif selection == '2':
dec_input = int(input("Enter decimal number: "))
bin_output = decimal_value(dec_input)
print("The binary equivalent is:", bin_output)

# invalid selection
else:
print("Invalid selection")
