# simulator

OAS 차량·CAN simulation, log replay 및 test fixture를 위한 Python 도구입니다.

Python 3.12 이상과 `uv`를 사용합니다. 실제 Vehicle Control은 이 저장소에서 수행하지 않습니다.

`fixtures/synthetic_vehicle_status.json`은 `can`의 synthetic decoder와 `car`의
test adapter가 공유하는 비차량 fixture입니다. 실제 DBC, OEM 신호 또는 차량 제어
명령을 포함하지 않습니다.
