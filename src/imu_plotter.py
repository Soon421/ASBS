import pandas as pd
import matplotlib.pyplot as plt

# --- 1) CSV 읽기 (헤더 포함) ---
imu = pd.read_csv("imu_log.csv", header=0)

# --- 2) 시간 순 정렬 ---
imu = imu.sort_values(by="timestamp")

# --- 3) 3행짜리 서브플롯 생성 ---
fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)
fig.suptitle("Longitudinal Acceleration, Yaw, and Speed")

# 1) 종방향 가속도 (accX)
axes[0].plot(imu["timestamp"], imu["accX"], label="Longitudinal Acc [m/s²]")
axes[0].set_ylabel("AccX [m/s²]")
axes[0].legend(loc="upper right")
axes[0].grid(True)

# 2) Yaw 각도
axes[1].plot(imu["timestamp"], imu["yaw"], label="Yaw [°]", color="tab:orange")
axes[1].set_ylabel("Yaw [°]")
axes[1].legend(loc="upper right")
axes[1].grid(True)

# 3) 속도
axes[2].plot(imu["timestamp"], imu["speed"], label="Speed [m/s]", color="tab:green")
axes[2].set_ylabel("Speed [m/s]")
axes[2].set_xlabel("Timestamp [s]")
axes[2].legend(loc="upper right")
axes[2].grid(True)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()


