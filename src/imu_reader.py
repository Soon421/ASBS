# imu_reader.py
import serial
import time

def open_serial(port="COM8", baudrate=9600, timeout=1):
    try:
        ser = serial.Serial(port, baudrate, timeout=timeout)
    except serial.SerialException as e:
        raise RuntimeError(f"시리얼 포트 열기 실패: {e}")
    time.sleep(2)
    print(f"[INFO] {port} 연결 완료")
    return ser


def read_serial_line(ser):
    while True:
        raw = ser.readline()
        if not raw:
            continue

        line = raw.decode('utf-8', errors='ignore').strip()
        parts = line.split(',')

        try:
            values = [float(p) for p in parts]
        except ValueError:
            print(f"[WARN] 파싱 실패: {line}")
            continue

        timestamp = time.time()
        yield timestamp, values

def main(port="COM8", baudrate=9600):

    try:
        ser = open_serial(port, baudrate)
    except RuntimeError as e:
        print(e)
        return

    try:
        for timestamp, values in read_serial_line(ser):
            print(f"{values}")
    except KeyboardInterrupt:
        print("\n[INFO] 데이터 수신 종료")
    finally:
        ser.close()
        print("[INFO] 포트 닫힘")

if __name__ == "__main__":
    main()




