import socket
import subprocess


def is_port_in_use(port):
    """
    Create a TCP connection to a IPv4 address, to test if port 8000 is still in use.
    socket.AF_INET = Used for IPv4 addresses (like 127.0.0.1 or 192.168.1.1
    socket.SOCK_STREAM = Create a TCP socket
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0


def free_port_windows(port):
    print(f"🔍 Checking port {port}...")
    result = subprocess.run(f'netstat -ano | findstr :{port}', capture_output=True, text=True, shell=True)
    lines = result.stdout.strip().split('\n')

    if not lines or lines == ['']:
        print(f"✅ Port {port} is free.")
        return

    pids = set()
    for line in lines:
        parts = line.split()
        if len(parts) >= 5:
            pid = parts[-1]
            pids.add(pid)

    if not pids:
        print(f"⚠️  No PIDs found for port {port}.")
        return

    print(f"🔴 Attempting to kill processes: {', '.join(pids)}")

    for pid in pids:
        try:
            kill = subprocess.run(f'taskkill /PID {pid} /F', capture_output=True, text=True, shell=True)
            print(f"✅ Killed PID {pid}: {kill.stdout.strip()}")
        except Exception as e:
            print(f"❌ Failed to kill PID {pid}: {e}")
