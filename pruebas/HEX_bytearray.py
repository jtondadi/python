# convertir HEX a bytearray (imnágenes) ..LCD converter . 
# en pruebas
# by JTD-2024
#
hex_string = """
0x00, 0xFC, 0x07, 0x00, 0xFE, 0x07, 0x00, 0xEE, 0x0F, 0x00, 0xFE, 0x0F,
0x00, 0xFE, 0x0F, 0x00, 0xFE, 0x0F, 0x00, 0xFE, 0x07, 0x06, 0xFF, 0x03,
0xC3, 0xFF, 0x00, 0xE7, 0xFF, 0x00, 0xFF, 0xFF, 0x00, 0xFF, 0x3F, 0x00,
0xFE, 0x3F, 0x00, 0xFC, 0x1F, 0x00, 0xF8, 0x1F, 0x00, 0xF0, 0x1F, 0x00,
0xF0, 0x0E, 0x00, 0x60, 0x0E, 0x00, 0xE0, 0x0E, 0x00, 0xE0, 0x1E, 0x00
"""

# Convert the hex string to a list of integers
byte_values = [int(x, 16) for x in hex_string.split(",")]

# Create a bytearray from the list of integers
byte_array = bytearray(byte_values)

# Display the bytearray
print(byte_array)
