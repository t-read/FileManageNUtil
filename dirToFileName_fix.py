from pathlib import Path
from tqdm import tqdm

"""
기존의 이미지 파일명에서 폴더 이름을 사용하여 새로운 파일명을 생성하고, 파일 이름을 변경하는 코드입니다.
리스트 형태로한 모든 jpg 파일이 target별 index와 함게 코드상에 있는 원본위치에서 상위폴더에서 filename변환된 jpg파일로 이동합니다. 
그리고, 코드의 뒷부분에 infinite loop를 생성하여 사용자 입력 또는 예외 발생 시까지 반복해서 사용자 입력을 받는 코드를 수행합니다. 
사용자 입력 값이 'stop' 이면 infinite loop 를 종료하고 그 외의 경우에는 사용자가 입력한 값을 그대로 출력합니다.
"""

# 경로 설정
path = Path("W:\\Data_5-3_back\\001_newCollect\\재업로드")

if __name__ == '__main__':
    # countObj 초기화
    countObj = {}
    
    # jpg 파일 경로 리스트 생성
    files = list(path.glob('**/*.jpg'))
    
    # 진행 상황 바 생성
    with tqdm(total=len(files)) as pbar:
        # jpg 파일 경로 리스트를 돌면서 파일 이름 변경 작업 수행
        for file in files:
            # 파일의 경로에 존재하는 두 번째, 세 번째 폴더 이름을 조합한 target 변수 생성
            target = '_'.join([file.parent.parts[-2], file.parent.parts[-1]])
            # target 변수를 키로 가지는 countObj 딕셔너리 값 증가
            if target in countObj:
                countObj[target] = countObj[target] + 1
            else:
                countObj[target] = 1
            # 변경될 파일 이름 설정
            newName = f"{target}000{countObj[target]}.jpg"
            # 파일 이름 변경 작업 수행
            # file.parent.parent를 사용하여 파일 경로의 뒤에서 두 번째 폴더(01, 02, 03)로 이동함
            # 그리고 newName을 사용하여 파일 이름 변경
            file.rename(file.parent.parent / newName)
            # tqdm 라이브러리를 사용한 진행 상황 바 업데이트
            pbar.update()
# infinite loop를 생성하여 사용자 입력 또는 예외 발생 시까지 반복해서 사용자 입력을 받는 코드
while True:
    try:
        # input() 함수를 사용하여 사용자 입력을 받음
        user_input = input("Please enter a command ('stop' to exit): ")
    except Exception as e:
        # 예외가 발생할 경우 예외 정보와 함께 에러 메시지 출력
        print(f"[ERROR] {str(e)}")
    else:
        # 입력한 문자열에 따른 분기 처리
        if user_input == 'stop':
            # stop이 입력되면 infinite loop 종료
            break
        else:
            # 그 외의 경우 사용자가 입력한 값을 그대로 출력
            print(f"You entered: {user_input}")
