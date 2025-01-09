import os
import subprocess
import ctypes
import sys

            # "" 내부에 nircmd.exe파일의 경로 입력 
nircmd_path = ""  # NirCmd 실행 파일의 경로 (필요 시 절대 경로로 변경
def is_admin():
    """Check if the script is running as admin"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
def change_audio_device(device_name):
    """Change the default audio device using NirCmd"""
    try:
        result = subprocess.run(
            [nircmd_path, "setdefaultsounddevice", device_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        if result.returncode == 0:
            print(f"기본 오디오 출력 장치가 '{device_name}'로 변경되었습니다.")
        else:
            print(f"오디오 출력 장치 변경 중 오류 발생: {result.stderr}")
    except FileNotFoundError:
        print(f"'{nircmd_path}' 파일을 찾을 수 없습니다. NirCmd 경로를 확인하세요.")
    except Exception as e:
        print(f"오디오 출력 장치 변경 중 오류 발생: {e}")

if __name__ == "__main__":
    print("프로그램 실행")
    
    if not is_admin():
        # Relaunch the script with admin privileges
        print("관리자 권한이 필요합니다. 관리자 권한으로 재실행합니다.")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()
    
                # "" 안에 장치명을 입력 
    device_name = ""
    print(f"출력 장치를 {device_name}로 변경합니다. ")

    
    change_audio_device(device_name)
