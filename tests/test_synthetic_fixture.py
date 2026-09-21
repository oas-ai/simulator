import json
from pathlib import Path

FIXTURE_PATH = Path(__file__).parents[1] / "fixtures" / "synthetic_vehicle_status.json"


def test_synthetic_vehicle_status_fixture_is_well_formed() -> None:
    fixture = json.loads(FIXTURE_PATH.read_text())

    assert fixture["frame"] == {"id": 291, "is_fd": False, "data": [0, 0]}
    assert fixture["context"] == {"timestamp_ns": 1000, "bus": 0}
    assert fixture["decoded_message"] == {
        "name": "synthetic_status",
        "signals": {"speed_mps": 12.5, "brake_pressed": False},
    }
