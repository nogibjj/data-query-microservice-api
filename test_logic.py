from mylib.logic import get_activity_by_participant_count
from mylib.logic import get_activity_by_type
from mylib.logic import get_activity_by_price


def test_participant():

    """Test get_activity_by_participant_count function"""

    result = get_activity_by_participant_count("5")

    assert result["participants"] == 5


def test_type():

    """Test get_activity_by_type function"""

    result = get_activity_by_type("education")

    assert result["type"] == "education"


def test_price():

    """Test get_activity_by_price function"""

    result = get_activity_by_price("0.1")

    assert result["price"] == 0.1

test_participant()
test_type()
test_price()