import subprocess
import time

def get_wifi_info_windows():
    try:
        # netsh 명령 실행
        output = subprocess.check_output(["netsh", "wlan", "show", "interfaces"], encoding="mbcs")

        # Wi-Fi 연결 상태 확인
        connected_adapters = [line for line in output.splitlines() if "SSID" in line and "BSSID" not in line]
        if not connected_adapters:
            return "No Wi-Fi connected", {}, 0, 0

        # SSID 추출
        ssid_line = connected_adapters[0]
        ssid = ssid_line.split(":")[1].strip()

        # 전체 정보 딕셔너리 생성
        details = {}
        for line in output.splitlines():
            if ":" in line:
                key, value = map(str.strip, line.split(":", 1))
                details[key] = value

        # 송수신 속도 추출
        receive_rate_key = "수신 속도(Mbps)"
        transmit_rate_key = "전송 속도(Mbps)"

        receive_rate_str = details.get(receive_rate_key, "0").strip()
        transmit_rate_str = details.get(transmit_rate_key, "0").strip()

        receive_rate = float(receive_rate_str) if receive_rate_str.replace('.', '', 1).isdigit() else 0
        transmit_rate = float(transmit_rate_str) if transmit_rate_str.replace('.', '', 1).isdigit() else 0

        return ssid, details, receive_rate, transmit_rate

    except subprocess.CalledProcessError as e:
        print("Error retrieving Wi-Fi info:", e)
        return "Error", {}, 0, 0
    except Exception as e:
        print("An unexpected error occurred:", e)
        return "Error", {}, 0, 0

def collect_wifi_data(interval=1, count=10):
    receive_rates = []
    transmit_rates = []
    last_details = {}

    for i in range(count):
        # Wi-Fi 데이터 수집
        ssid, details, receive_rate, transmit_rate = get_wifi_info_windows()

        # 연결되지 않았으면 스킵
        if ssid == "No Wi-Fi connected":
            print(f"[{i+1}/{count}] No Wi-Fi connection detected.")
            time.sleep(interval)
            continue

        # 데이터 저장
        receive_rates.append(receive_rate)
        transmit_rates.append(transmit_rate)

        # 마지막 세부 정보 저장
        last_details = details

        # 현재 송수신 속도 출력
        print(f"[{i+1}/{count}] Receive Rate: {receive_rate} Mbps, Transmit Rate: {transmit_rate} Mbps")

        # 간격 대기
        time.sleep(interval)

    # 평균 계산
    avg_receive_rate = sum(receive_rates) / len(receive_rates) if receive_rates else 0
    avg_transmit_rate = sum(transmit_rates) / len(transmit_rates) if transmit_rates else 0

    # 마지막 세부 정보에서 송수신 속도를 제거
    if "수신 속도(Mbps)" in last_details:
        del last_details["수신 속도(Mbps)"]
    if "전송 속도(Mbps)" in last_details:
        del last_details["전송 속도(Mbps)"]

    # 마지막 Wi-Fi 세부 정보 출력
    if last_details:
        print("\nFinal Wi-Fi Details (송수신 속도 제외):")
        for key, value in last_details.items():
            print(f"{key}: {value}")

    # 결과 출력
    print("\nWi-Fi Data Collection Complete:")
    print(f"Receive Rates: {receive_rates}")
    print(f"Transmit Rates: {transmit_rates}")
    print(f"Average Receive Rate: {avg_receive_rate:.2f} Mbps")
    print(f"Average Transmit Rate: {avg_transmit_rate:.2f} Mbps")

# 데이터 수집 실행
collect_wifi_data(interval=1, count=10)
