import pyautogui
import pytesseract
from PIL import Image

# 화면을 캡쳐하고 텍스트를 인식하는 함수
def capture_and_find_text(text):
    # 화면 전체를 캡쳐
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")

    # 이미지에서 텍스트 추출
    extracted_text = pytesseract.image_to_string(Image.open("screenshot.png"))

    # 특정 문자열이 포함되어 있는지 확인
    if text in extracted_text:
        print(f"'{text}' 문자열을 포함하는 창을 찾았습니다.")
    else:
        print(f"'{text}' 문자열을 포함하는 창을 찾지 못했습니다.")

# "[0198] 실시간 종목 조회" 문자열을 찾기
capture_and_find_text("[0198] 실시간 종목 조회")