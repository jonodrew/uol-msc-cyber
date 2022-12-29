The gateway examines the data in application-layer elements when deciding whether to block or allow data

## Application proxy
- applies simple tests to smaller application data items
- for example, compare a URL or a server accessed via FTP against a blocklist/allowlist
- proxies also allow for complicated protocols. An FTP proxy allows the firewall to pass through the specific FTP traffic while keeping unnecessary FTP ports closed
- these proxies only really work for small data items: for arbitrarily large messages, such as emails, the data has to be redirected to a different process that can collect and analyze the entire message
