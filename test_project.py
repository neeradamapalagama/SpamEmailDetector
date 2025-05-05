import pytest
from project import *


def test_message_type():
    assert message_type("ham") == "Seems not a Spam Message! 🙂"
    assert message_type("spam") == "Warning! It's a Spam Message! ⚠️"
    with pytest.raises(ValueError):
        message_type("CS50")


def test_model():
    assert model("invalid_file.csv") == None


def test_is_valid():
    assert is_valid("CS50") == False
    assert is_valid("Hello, How are you?") == True
    assert is_valid("50") == False


def test_message_type_reverse():
    assert message_type_reverse("ham") == "spam"
    assert message_type_reverse("spam") == "ham"
    with pytest.raises(ValueError):
        message_type_reverse("CS50")

def test_check_file():
    assert check_file("data/default/spam.csv") == True
    assert check_file("model.joblib") == True
    assert check_file("count_vectorizer.joblib") == True
    assert check_file("data/CS50.txt") == None

def test_get_accuracy():
    assert get_accuracy(0.98) == "Very Good"
    assert get_accuracy(0.87) == "Good"
    assert get_accuracy(0.5) == "Bad ⚠️ \nPlease Reset the Model for Better Results!"


def test_model_reset():
    #assert model_reset() == True # By running this, it will reset the dataset 
    pass


def test_model_update():
    #assert model_update() == True # By running this, it will update the dataset
    pass