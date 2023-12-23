# Useful for eCPPT as it is done in python 2.5.2


import subprocess
import os

# Rango de direcciones IP para escanear
ip_base = "10.185.10."
start_ip = 1
end_ip = 255

def ping_ip(ip_address):
    # Ajusta el comando de acuerdo al sistema operativo
    command = ['ping', '-c', '1', '-W', '1', ip_address]
    if os.name == 'nt':  # Windows
        command = ['ping', '-n', '1', '-w', '1000', ip_address]

    try:
        # Ejecutar el comando ping
        subprocess.check_call(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    for i in range(start_ip, end_ip + 1):
        ip = ip_base + str(i)
        if ping_ip(ip):
            print("Host activo encontrado:", ip)

if __name__ == "__main__":
    main()
