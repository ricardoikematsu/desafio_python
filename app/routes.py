from flask import Blueprint, request, jsonify
from app.models import DadosTempo
from app.utils import fetch_weather_data

main = Blueprint('main', __name__)

@main.route('/api/previsao/', methods=['GET'])
def obter_previsao_tempo():
    cidade = request.args.get('cidade', 'São Paulo')
    data = fetch_weather_data(cidade)

    if data:
        previsao = DadosTempo(cidade=cidade, dados=data)
        previsao.save_to_db()
        return jsonify(data), 200
    else:
        return jsonify({'error': 'Falha ao buscar dados de previsão do tempo'}), 400

@main.route('/api/historico/', methods=['GET'])
def obter_historico():
    historico = DadosTempo.get_all()
    return jsonify([{
        'cidade': h.cidade,
        'dados': h.dados,
        'timestamp': h.timestamp
    } for h in historico]), 200