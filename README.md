# rmho
mitmProxy for remove HttpOnly in header

## Install 

`# apt install python3-pip` <br \>
`# pip3 install mitmproxy`

## Modify Tor network

`# sudo sed -i "s/#AllowInbound 1/AllowInbound 1/g" /etc/tor/torsocks.conf`

## Run

`# torsocks mitmdump -p 8089 -s http_header.py`

