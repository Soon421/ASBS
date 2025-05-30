import pandas as pd
import matplotlib.pyplot as plt

# csv파일 값 받아오기
imu = pd.read_csv(
    "imu_log.csv",
    names=[
        "timestamp",
        "accX", "accY", "accZ",
        "gyroX", "gyroY", "gyroZ",
        "angleX", "angleY", "angleZ"
    ],
    header=None
)

# --- 2) 시간 순 정렬 ---
imu = imu.sort_values(by="timestamp")

# --- 3) 3행짜리 서브플롯 생성 ---
fig, axes = plt.subplots(3, 1, figsize=(12, 12), sharex=True)
fig.suptitle("IMU: Acceleration, Angular Velocity, and Angles")

# 가속도
axes[0].plot(imu["timestamp"], imu["accX"], label="accX")
axes[0].plot(imu["timestamp"], imu["accY"], label="accY")
axes[0].plot(imu["timestamp"], imu["accZ"], label="accZ")
axes[0].set_ylabel("Acceleration [m/s²]")
axes[0].legend(loc="upper right")
axes[0].grid(True)

# 각속도
axes[1].plot(imu["timestamp"], imu["gyroX"], label="gyroX")
axes[1].plot(imu["timestamp"], imu["gyroY"], label="gyroY")
axes[1].plot(imu["timestamp"], imu["gyroZ"], label="gyroZ")
axes[1].set_ylabel("Angular Velocity [°/s]")
axes[1].legend(loc="upper right")
axes[1].grid(True)

# 각도
axes[2].plot(imu["timestamp"], imu["angleX"], label="angleX")
axes[2].plot(imu["timestamp"], imu["angleY"], label="angleY")
axes[2].plot(imu["timestamp"], imu["angleZ"], label="angleZ")
axes[2].set_ylabel("Angle [°]")  
axes[2].set_xlabel("Timestamp [s]")
axes[2].legend(loc="upper right")
axes[2].grid(True)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

