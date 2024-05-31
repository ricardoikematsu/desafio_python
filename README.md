# Aplicação de Previsão do Tempo

## Descrição

Esta aplicação fornece uma API para obter a previsão do tempo dos próximos dias utilizando a API do OpenWeatherMap e salva o histórico de chamadas em um banco de dados MongoDB.

## Tecnologias Utilizadas

- Python
- Flask
- MongoDB
- Docker

## Instruções para subir o ambiente

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/previsao_tempo.git
    cd previsao_tempo
    ```

2. Crie um arquivo `.env` na raiz do projeto com a sua chave da API do OpenWeatherMap:
    ```env
    OPENWEATHERMAP_API_KEY=sua_api_key_aqui
    ```

3. Construa e inicie os containers Docker:
    ```sh
    docker-compose up --build
    ```

4. A aplicação estará disponível em `http://localhost:5000`.

## Endpoints

### Obter previsão do tempo
- **URL:** `/api/previsao/`
- **Método:** `GET`
- **Parâmetros de Query:**
  - `cidade` (opcional, padrão: `São Paulo`)
- **Resposta de Sucesso:** `200 OK`
  - Exemplo de resposta:
    ```json
    {
      "list": [
        {
          "dt": 1628785200,
          "main": {
            "temp": 293.55,
            ...
          },
          ...
        },
        ...
      ]
    }
    ```

### Consultar histórico
- **URL:** `/api/historico/`
- **Método:** `GET`
- **Resposta de Sucesso:** `200 OK`
  - Exemplo de resposta:
    ```json
    [
      {
        "cidade": "São Paulo",
        "dados": {...},
        "timestamp": "2023-05-29T00:00:00Z"
      },
      ...
    ]
    ```
