import pygame

BLACK = (0,0,0) #(255,255,255) 흰색
pad_width = 480
pad_height = 640

#게임 실행 메인 함수
def runGame():
	global gamepad, clock

	ongame = False
	while not ongame:
		for event in pygame.event.get():
			if event.type==pygame.QUIT: #마우스로 닫기버튼 클릭 이벤트
				doneFlag = True

			#게임 화면을 검정색으로 채우고 화면을 업데이트
			gamepad.fill(BLACK)
			pygame.display.update()
			clock.tick(60)#초당 프레임 수

	pygame.quit()

#게임 초기화 함수
def initGame():
	global gamepad, clock
	pygame.init()
	gamepad=pygame.display.set_mode((pad_width,pad_height))
	pygame.display.set_caption("MyGalaga")
	clock=pygame.time.Clock()

initGame()
runGame()