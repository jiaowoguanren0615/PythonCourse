# Calculate the total number of bytes (rounding down to ignore fractional bytes)
total_bytes = int(input("Input a number of bits: "))

BYTES_IN_BITS = 8
BYTES_IN_KILOBYTE = 1024 * BYTES_IN_BITS
BYTES_IN_MEGABYTE = 1024 * BYTES_IN_KILOBYTE


# Calculate the number of megabytes
megabytes = total_bytes // BYTES_IN_MEGABYTE
remaining_bytes = total_bytes % BYTES_IN_MEGABYTE
print(remaining_bytes) # 8201

# Calculate the number of kilobytes
kilobytes = remaining_bytes // BYTES_IN_KILOBYTE # 1
remaining_bytes = remaining_bytes % BYTES_IN_KILOBYTE
print(remaining_bytes) # 9

# Calculate the number of Bytes
Bytes = remaining_bytes // 8    # 1
remaining_bytes = remaining_bytes % 8
print(remaining_bytes) # 1

# The remaining bytes----> bits
bits = remaining_bytes  # 1


mb = int(megabytes)
kb = int(kilobytes)
bytes = int(Bytes)
b = int(bits)
print(f"{total_bytes} b = {mb} MB {kb} KB {bytes} B {b} b")