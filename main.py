from random import choice, randint
from time import sleep

import requests

from config import config
from constants import HEADERS


def check_local_logs(name: str, ip: str, port: str, endpoint: str, proxy: str | None = None) -> None:
    url = f'http://{ip}:{port}/{endpoint}'

    try:
        if proxy:
            proxies = {
                "http": proxy,
                "https": proxy
            }
            response = requests.get(url, proxies=proxies)
        else:
            response = requests.get(url)

        response.raise_for_status()

        json_data = response.json()
        print(f"{name} - {json_data}")

    except requests.exceptions.RequestException as e:
        print(f"{name} - failed to connect to {url} using proxy {proxy}, reason: {e}")


def check_web_metrics(name: str, proxy: str):
    with open('validator_addresses.txt', 'r') as f:
        addresses_data = [i.strip() for i in f.readlines()]

    validator_address: str = ''
    for address_data in addresses_data:
        val_name, val_address = address_data.split('|')
        if str(val_name) == str(name):
            validator_address = val_address

    if not validator_address:
        print(f"{name} - failed to check metrics, reason: missing address in validator_addresses.txt")
        return

    url = f'https://api.testnet-3.elixir.xyz/validators//{validator_address}'
    useragent, sec_ch_ua, platform = choice(HEADERS)

    headers = {
        'sec-ch-ua': sec_ch_ua,
        'Referer': 'https://testnet-3.elixir.xyz/',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': useragent,
        'sec-ch-ua-platform': platform,
    }

    try:
        if proxy:
            proxies = {
                "http": proxy,
                "https": proxy
            }
            response = requests.get(url, headers=headers, proxies=proxies)
        else:
            response = requests.get(url, headers=headers)

        response.raise_for_status()

        json_data = response.json()
        uptime_day = f"{round(float(json_data['validator']['uptime_day']), 2)}%"
        uptime_week = f"{round(float(json_data['validator']['uptime_week']), 2)}%"
        uptime_month = f"{round(float(json_data['validator']['uptime_month']), 2)}%"
        online = json_data['validator']['online']
        jailed = json_data['validator']['jailed']
        apy = json_data['validator']['apy']

        print(f"{name} - upday: {uptime_day} | upweek: {uptime_week} | upmonth: {uptime_month} | online: {online} | jailed: {jailed} | apy: {apy}")

    except requests.exceptions.RequestException as e:
        print(f"{name} - failed to connect to {url} using proxy {proxy}, reason: {e}")
    except KeyError:
        print(f"{name} - failed to parse response: {json_data}")

    sleep(randint(config['web_metrics_check_delay_sec'][0], config['web_metrics_check_delay_sec'][1]))


def main():
    with open('servers.txt', 'r') as f:
        servers = [i.strip() for i in f.readlines()]

    endpoints = {
        "1": "health",
        "2": "metrics",
        "3": "web_metrics"
    }

    endpoint = endpoints[input('Choose option to perform:\n1 - Check health\n2 - Check metrics\n3 - Check web metrics\n\n')]

    for server in servers:
        try:
            name, host, proxy = server.split('|', 2)
        except ValueError:
            proxy = None
            name, host = server.split('|', 1)

        if endpoint == 'web_metrics':
            check_web_metrics(name, proxy)
        else:
            check_local_logs(name, host, config["port"], endpoint, proxy)


if __name__ == '__main__':
    main()
