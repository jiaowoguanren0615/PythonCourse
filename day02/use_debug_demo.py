# from typing import Dict, List, Tuple



total_bytes = 8201

BYTES_IN_BITS = 8
BYTES_IN_KILOBYTE = 1024 * BYTES_IN_BITS
BYTES_IN_MEGABYTE = 1024 * BYTES_IN_KILOBYTE


# Calculate the number of megabytes
megabytes = total_bytes // BYTES_IN_MEGABYTE
remaining_bytes = total_bytes % BYTES_IN_MEGABYTE


# Calculate the number of kilobytes
kilobytes = remaining_bytes // BYTES_IN_KILOBYTE
remaining_bytes = remaining_bytes % BYTES_IN_KILOBYTE


# Calculate the number of Bytes
Bytes = remaining_bytes // 8    # 1
remaining_bytes = remaining_bytes % 8


# The remaining bytes----> bits
bits = remaining_bytes

mb = int(megabytes)
kb = int(kilobytes)
bytes = int(Bytes)
b = int(bits)
print(f"{total_bytes} b = {mb} MB {kb} KB {bytes} B {b} b")