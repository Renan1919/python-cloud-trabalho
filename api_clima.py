import requests

# Dicionário com as cidades e suas coordenadas
CIDADES = {
    "Curitiba": {"lat": -25.43, "lon": -49.27},
    "São Paulo": {"lat": -23.55, "lon": -46.64}
}

# URL base da API Open-Meteo
URL_BASE = "https://api.open-meteo.com/v1/forecast"

def consultar_clima(cidade, lat, lon):
    """
    Consulta a API de clima para uma cidade específica e exibe os resultados.
    """
    # Monta a URL completa com os parâmetros da cidade
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": "true"
    }

    try:
        # Faz a requisição HTTP
        response = requests.get(URL_BASE, params=params)
        response.raise_for_status()  # Lança um erro para respostas ruins (4xx ou 5xx)

        # Converte a resposta para JSON
        clima = response.json()
        current_weather = clima.get("current_weather", {})

        # Exibe as informações de forma organizada
        print(f"--- Clima em {cidade} ---")
        temperatura = current_weather.get("temperature", "N/A")
        velocidade_vento = current_weather.get("windspeed", "N/A")
        print(f"Temperatura atual: {temperatura}°C")
        print(f"Velocidade do vento: {velocidade_vento} km/h\n")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar o clima de {cidade}: {e}\n")

if __name__ == "__main__":
    # Itera sobre o dicionário de cidades e consulta o clima para cada uma
    for nome_cidade, coordenadas in CIDADES.items():
        consultar_clima(nome_cidade, coordenadas["lat"], coordenadas["lon"])

