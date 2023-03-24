import os
# Flask から importしてflaskを使えるようにする
import sqlite3, datetime as dt
from flask import Flask, render_template, request, redirect, session

import socket
# ホスト名を取得、表示
host = socket.gethostname()
print(host)

# ipアドレスを取得、表示
ip = socket.gethostbyname(host)
print(ip) 