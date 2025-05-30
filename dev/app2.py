import requests
import sqlite3
import time
from datetime import datetime
from typing import Dict, Union

def get_dollar_quote() -> Union[Dict[str, Union[str, float]], Dict[str, str]]:
    url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if 'USDBRL' not in data:
            return {'erro': 'Resposta inválida da API. Chave "USDBRL" não encontrada.'}

        dolar_info = data['USDBRL']
        return {
            'moeda': 'Dólar',
            'codigo': dolar_info.get('code', 'N/A'),
            'cotacao': float(dolar_info.get('bid', 0)),
            'alta': float(dolar_info.get('high', 0)),
            'baixa': float(dolar_info.get('low', 0)),
            'data': dolar_info.get('create_date', 'N/A'),
            'timestamp_coleta': datetime.now().isoformat()
        }

    except requests.exceptions.RequestException as e:
        return {'erro': 'Erro na requisição HTTP.', 'detalhes': str(e)}
    except ValueError as e:
        return {'erro': 'Erro ao converter os dados da cotação.', 'detalhes': str(e)}
    except Exception as e:
        return {'erro': 'Erro inesperado ao obter a cotação.', 'detalhes': str(e)}


def save_to_db(cotacao: Dict[str, Union[str, float]]) -> None:
    try:
        conn = sqlite3.connect('cotacoes.db')
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cotacao_dolar (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                moeda TEXT,
                codigo TEXT,
                cotacao REAL,
                alta REAL,
                baixa REAL,
                data TEXT,
                timestamp_coleta TEXT
            );
        """)

        cursor.execute("""
            INSERT INTO cotacao_dolar (
                moeda, codigo, cotacao, alta, baixa, data, timestamp_coleta
            ) VALUES (?, ?, ?, ?, ?, ?, ?);
        """, (
            cotacao['moeda'],
            cotacao['codigo'],
            cotacao['cotacao'],
            cotacao['alta'],
            cotacao['baixa'],
            cotacao['data'],
            cotacao['timestamp_coleta']
        ))

        conn.commit()
        print('💾 Cotação salva no banco de dados com sucesso.')
    except Exception as e:
        print('❌ Erro ao salvar no banco de dados:', e)
    finally:
        conn.close()


if __name__ == '__main__':
    print('⏳ Iniciando coleta automática a cada 10 segundos...\nPressione Ctrl+C para parar.\n')
    try:
        while True:
            cotacao = get_dollar_quote()
            if 'erro' not in cotacao:
                print('📈 Cotação atual do dólar:')
                print(f"Moeda: {cotacao['moeda']}")
                print(f"Código: {cotacao['codigo']}")
                print(f"Cotação: R$ {cotacao['cotacao']:.2f}")
                print(f"Alta: R$ {cotacao['alta']:.2f}")
                print(f"Baixa: R$ {cotacao['baixa']:.2f}")
                print(f"Data da cotação: {cotacao['data']}")
                print(f"Timestamp da coleta: {cotacao['timestamp_coleta']}\n")
                save_to_db(cotacao)
            else:
                print('❌ Erro ao obter a cotação:', cotacao)
            time.sleep(10)
    except KeyboardInterrupt:
        print('\n🛑 Coleta encerrada pelo usuário.')
