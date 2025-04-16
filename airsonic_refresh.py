#!/usr/bin/python3
import requests
import config_airsonic as config

# Genera l'URL per l'API
# rest_url = f'{config.server_url}/ping.view'
rest_url = f'{config.server_url}/startScan.view'

# Parametri necessari per l'autenticazione
params = {
    'u': config.username,
    'p': config.password,
    'v': '1.15.0',  # Versione API, modificabile
    'c': 'Myapp',  # Nome client, personalizzabile
    'f': 'json'  # Formato della risposta
}

# Invio della richiesta per avviare la scansione delle cartelle multimediali
response = requests.get(rest_url, params=params)

if response.status_code != 200:
    print(f'Errore durante la connect: {response.json()}')
    exit()

resp_js = response.json()
resp_status = resp_js['subsonic-response']['status']

if resp_status == 'failed':
    print(f'failed: {resp_js['subsonic-response']['error']}')
else:
    print(resp_js['subsonic-response'])
