import requests

def get_dollar_quote():
    url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        dolar_info = data['USDBRL']
        result = {
            'moeda': 'Dólar',
            'codigo': dolar_info['code'],
            'cotacao': float(dolar_info['bid']),
            'alta': float(dolar_info['high']),
            'baixa': float(dolar_info['low']),
            'data': dolar_info['create_date']
        }
        return result
    except Exception as e:
        return {'erro': 'Não foi possível obter a cotação.', 'detalhes': str(e)}

if __name__ == '__main__':
    cotacao = get_dollar_quote()
    print(cotacao)
