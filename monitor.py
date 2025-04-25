import math

# 화면 비율을 기반으로 모니터의 가로 세로 계산 함수
def calculate_monitor_size(diagonal_inch, aspect_ratio_width, aspect_ratio_height):
    # 대각선 길이를 이용하여 가로와 세로를 계산
    diagonal_ratio = math.sqrt(aspect_ratio_width**2 + aspect_ratio_height**2)
    monitor_width = (diagonal_inch * aspect_ratio_width) / diagonal_ratio
    monitor_height = (diagonal_inch * aspect_ratio_height) / diagonal_ratio
    return monitor_width, monitor_height

# 영상 크기 계산 함수 (픽셀 보존 상태에서 실제 크기 계산)
def calculate_video_size(monitor_width, monitor_height, monitor_resolution_width, monitor_resolution_height, video_resolution_width, video_resolution_height):
    # 가로/세로 비율 계산
    scale_x = monitor_resolution_width / video_resolution_width
    scale_y = monitor_resolution_height / video_resolution_height
    
    # 비율이 작은 값을 적용해서 영상 크기 계산
    scale = min(scale_x, scale_y)
    
    # 최종 영상 크기 (픽셀 보존 상태로 영상 크기)
    final_width_inch = (video_resolution_width * scale) / monitor_resolution_width * monitor_width
    final_height_inch = (video_resolution_height * scale) / monitor_resolution_height * monitor_height

    # 인치를 cm로 변환
    final_width_cm = final_width_inch * 2.54
    final_height_cm = final_height_inch * 2.54
    
    return final_width_cm, final_height_cm

# 해상도에 대한 매핑 함수 (fhd, qhd, 4k, 8k 외에도 커스텀 입력을 받기 위한 처리)
def get_resolution(resolution_type):
    if resolution_type == 'fhd':
        return 1920, 1080
    elif resolution_type == 'qhd':
        return 2560, 1440
    elif resolution_type == '4k':
        return 3840, 2160
    elif resolution_type == '8k':
        return 7680, 4320
    else:
        # 커스텀 해상도 처리
        try:
            width, height = map(int, resolution_type.split('x'))
            return width, height
        except ValueError:
            raise ValueError("지원하지 않는 해상도입니다. 'fhd', 'qhd', '4k', '8k' 또는 '가로x세로' 형식으로 입력하세요.")

# 사용자로부터 한 문장으로 입력받기
user_input = input("모니터 인치, 화면 비율, 모니터 해상도, 영상 해상도를 한 문장으로 입력하세요 (예: 32, 16:9, 4k, 1920x1080): ")

# 입력값 분리
inputs = user_input.split(', ')
if len(inputs) != 4:
    raise ValueError("입력값이 잘못되었습니다. 4개의 값을 입력해야 합니다.")

diagonal_inch = float(inputs[0])  # 모니터 인치
aspect_ratio_input = inputs[1]  # 화면 비율
monitor_resolution_input = inputs[2].lower()  # 모니터 해상도
video_resolution_input = inputs[3].lower()  # 영상 해상도

# 화면 비율 파싱
aspect_ratio_width, aspect_ratio_height = map(int, aspect_ratio_input.split(':'))

# 해상도 가져오기
monitor_resolution_width, monitor_resolution_height = get_resolution(monitor_resolution_input)
video_resolution_width, video_resolution_height = get_resolution(video_resolution_input)

# 모니터 가로, 세로 크기 계산
monitor_width, monitor_height = calculate_monitor_size(diagonal_inch, aspect_ratio_width, aspect_ratio_height)

# 영상 크기 계산 (픽셀 보존 시 실제 크기)
final_width_cm, final_height_cm = calculate_video_size(monitor_width, monitor_height, monitor_resolution_width, monitor_resolution_height, video_resolution_width, video_resolution_height)

# 결과 출력
print(f"{diagonal_inch}인치 모니터 ({aspect_ratio_width}:{aspect_ratio_height}) 비율의 가로: {monitor_width:.2f} cm, 세로: {monitor_height:.2f} cm")
print(f"영상 크기 (픽셀 보존 시): {final_width_cm:.2f} x {final_height_cm:.2f} cm")