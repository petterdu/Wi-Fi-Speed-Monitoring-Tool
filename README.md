# Wi-Fi Speed Monitoring Tool

This Python script allows you to monitor Wi-Fi speed (receive and transmit rates) on Windows systems. It uses the `netsh` command to retrieve Wi-Fi interface details and provides both real-time speed tracking and detailed network information.

## Features

- **Real-time Monitoring**: Tracks receive and transmit rates at regular intervals.
- **Comprehensive Details**: Displays all Wi-Fi interface information at the end of the session, excluding real-time speeds.
- **Summary Statistics**: Calculates average receive and transmit speeds over the monitoring period.
- **Customizable Settings**: You can adjust the interval and number of monitoring cycles.

## Requirements

- **Operating System**: Windows
- **Python Version**: Python 3.7 or higher

## Installation and Usage

```bash
# Clone the repository
git clone https://github.com/your-username/wifi-speed-monitor.git
```
# Navigate to the directory
```bash
cd wifi-speed-monitor
```
# Run the script
```bash
python wifi_speed_monitor.py
```

## To customize the monitoring parameters:
- **interval**: Time in seconds between each data collection (default: 1 second).
- **count**: Number of monitoring cycles (default: 10).

## Example Output:
```bash
# [1/10] Receive Rate: 780.0 Mbps, Transmit Rate: 866.7 Mbps
# [2/10] Receive Rate: 782.0 Mbps, Transmit Rate: 866.7 Mbps
# ...
# [10/10] Receive Rate: 778.0 Mbps, Transmit Rate: 866.7 Mbps
#
# Final Wi-Fi Details (송수신 속도 제외):
# 이름: Wi-Fi
# 설명: Intel(R) Wi-Fi 6E AX211 160MHz
# GUID: -Secret-
# 물리적 주소: e4:60:17:78:06:bd
# 인터페이스 유형: 기본
# 상태: 연결됨
# SSID: -Secret-
# BSSID: -Secret-
# 네트워크 종류: 인프라
# 송수신 장치 종류: 802.11ac
# 인증: WPA2-개인
# 암호화: CCMP
# 연결 모드: 자동 연결
# 밴드: 5GHz
# 채널: 157
# 신호: 96%
# 프로필: -Secret-
#
# Wi-Fi Data Collection Complete:
# Receive Rates: [780.0, 782.0, ..., 778.0]
# Transmit Rates: [866.7, 866.7, ..., 866.7]
# Average Receive Rate: 779.80 Mbps
# Average Transmit Rate: 866.70 Mbps
```

## License:
This project is licensed under the MIT License.
See the LICENSE file for details.
