from project import build_api_url, recommend_outfit, is_umbrella_needed

def test_build_api_url():
    assert build_api_url("Konya", "12345") == "http://api.openweathermap.org/data/2.5/weather?q=Konya&appid=12345&units=metric"
    assert build_api_url("New York", "abcde") == "http://api.openweathermap.org/data/2.5/weather?q=New%20York&appid=abcde&units=metric"

def test_recommend_outfit():
    assert recommend_outfit(5) == "Kalın bir mont, kazak ve bere."
    assert recommend_outfit(15) == "Hafif bir ceket veya hırka, uzun kollu tişört."
    assert recommend_outfit(22) == "Tişört ve pantolon/şort."
    assert recommend_outfit(30) == "İnce ve açık renkli kıyafetler, güneş gözlüğü."

def test_is_umbrella_needed():
    assert is_umbrella_needed("Rain") == True
    assert is_umbrella_needed("Clear") == False
    assert is_umbrella_needed("Clouds") == False
    assert is_umbrella_needed("Snow") == True