import requests
import sys

def main():
    print("🌤️ Hava Durumu ve Kıyafet Önericiye Hoş Geldiniz!")
    city = input("Şehir girin (Örn: Konya): ").strip()
    
    api_key = "2b8f1686c8b868bf9b91570b7b62b4a8" 
    
    url = build_api_url(city, api_key)
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data.get("cod") != 200:
            sys.exit("Şehir bulunamadı, lütfen tekrar deneyin.")
            
        temp = data["main"]["temp"]
        condition = data["weather"][0]["main"]
        
        outfit = recommend_outfit(temp)
        umbrella = is_umbrella_needed(condition)
        
        print(f"\n📍 {city.capitalize()} için Hava Durumu:")
        print(f"🌡️ Sıcaklık: {temp}°C ({condition})")
        print(f"👕 Öneri: {outfit}")
        if umbrella:
            print("☔ Dışarı çıkarken şemsiyenizi almayı unutmayın!")
            
    except requests.RequestException:
        sys.exit("İnternet bağlantısında veya veri çekmede bir hata oluştu.")

def build_api_url(city, api_key):
    city_formatted = city.replace(" ", "%20")
    return f"http://api.openweathermap.org/data/2.5/weather?q={city_formatted}&appid={api_key}&units=metric"

def recommend_outfit(temp_celsius):
    if temp_celsius < 10:
        return "Kalın bir mont, kazak ve bere."
    elif 10 <= temp_celsius <= 18:
        return "Hafif bir ceket veya hırka, uzun kollu tişört."
    elif 18 < temp_celsius <= 25:
        return "Tişört ve pantolon/şort."
    else:
        return "İnce ve açık renkli kıyafetler, güneş gözlüğü."

def is_umbrella_needed(weather_condition):
    rainy_conditions = ["Rain", "Drizzle", "Thunderstorm", "Snow"]
    return weather_condition in rainy_conditions

if __name__ == "__main__":
    main()