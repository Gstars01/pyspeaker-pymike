import subprocess
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def change_audio_input_device(nircmd_path, device_name):
    try:
        result = subprocess.run(
            [nircmd_path, "setdefaultsounddevice", device_name, "2"],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"오디오 입력 장치가 '{device_name}'로 변경되었습니다.")
    except subprocess.CalledProcessError as e:
        print(f"오디오 입력 장치 변경 중 오류 발생: {e.stderr}")
    except FileNotFoundError:
        print(f"'{nircmd_path}' 파일을 찾을 수 없습니다. NirCmd 경로를 확인하세요.")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    print("프로그램 시작 ")
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

    nircmd_path = ""  # nircmd.exe의 경로를 여기다가 입력 
    device_name = ""  # 입력장치 이름을 입력 


    change_audio_input_device(nircmd_path, device_name)
