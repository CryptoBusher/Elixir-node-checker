import requests

from config import config


def check_data(name: str, ip: str, port: str, endpoint: str, proxy: str | None = None) -> None:
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


def main():
    with open('servers.txt', 'r') as f:
        servers = [i.strip() for i in f.readlines()]

    endpoints = {
        "1": "health",
        "2": "metrics"
    }

    endpoint = endpoints[input('Choose option to perform:\n1 - Check health\n2 - Check metrics\n\n')]

    for server in servers:
        try:
            name, host, proxy = server.split('|', 2)
        except ValueError:
            proxy = None
            name, host = server.split('|', 1)

        check_data(name, host, config["port"], endpoint, proxy)


if __name__ == '__main__':
    main()
