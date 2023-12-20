#IP - 192.168.100.i$ // Can be changed for any IP
# Using this script for discovering host while pivoting between machines
# Credits
  # This script has been taken from S4vitar videos

#!/bin/bash

for i in $(seq 1 254); do
        timeout 1 bash -c "ping -c 1 192.168.100.i$" &>/dev/null && echo "[+] Host 192.168.100.i$ - Active" &
done; wait

