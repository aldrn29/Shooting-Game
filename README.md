<p align="center">
  <img src="https://github.com/aldrn29/Shooting-Game/blob/main/shooting-game/images/player.png?raw=true" width="13%">
</p>
<h1 align="center", size=100>Shooting Game</h1>
</br>

### Overview
임베디드SW 과목에서 진행한 게임 제작 프로젝트입니다.  
라즈베리파이 위에서 구현되었으며, 플레이어가 미사일을 이용하여 적을 물리치는 **싱글 플레이 슈팅게임**입니다.

### Prerequisites
<img src="https://img.shields.io/badge/Made%20with-python 3.7.3-blue?style=flat"> <img src="https://img.shields.io/badge/OS-Raspberry pi 4-red?style=flat">
1. micro SD카드에 리눅스를 설치하여 실행합니다.
2. 해당 플랫폼에 Adafruit_Blinka 라이브러리 설치합니다. 또한, SPI를 활성화하고 Python3을 실행하기 위하여 <a href="https://learn.adafruit.com/adafruit-1-3-color-tft-bonnet-for-raspberry-pi/python-setup">`Adafruit 1.3" Color TFT Bonnet for Raspberry Pi > Python Setup`</a>의 과정을 따라갑니다.

### Folder Structure
```
shooting-game
│
├── main.py
├── setting.py
├── src
│   ├── background.py
│   ├── button.py
│   ├── game_object.py
│   ├── game_ready.py
│   ├── game_starter.py
│   ├── game_status.py
│   └── object_controller.py
│ 
├── images
│   ├── background.png
│   ├── background2.png
│   ├── boss.png
│   ├── effect-boom1.png
│   │ 
```

### How to Start Game
```
$ sudo python3 main.py
```

### Game Objects
||||


<img src="https://github.com/aldrn29/Shooting-Game/blob/main/shooting-game/images/enemy1.png?raw=true" width="8%">


### Screenshot

