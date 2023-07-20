Python API to get the server usage. CPU, SWAP and Memory percent, usage in GB, free space, etc

## Setup

Before running the project we need to install the requirements, in console write `pip install -r requirements.txt`

## Run the project

### Windows

`py main.py`

### Linux & Mac

`python3 main.py`

## To create systemctl service

Go to `/etc/systemd/system` and create a file `script.service` and write:

```
[Unit]
Description="Script Description"
After=network.target

[Service]
User=server
WorkingDirectory=/home/server/script/
ExecStart=/home/server/.asdf/shims/python3.10 main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

and then `sudo systemctl enable script`

## Endpoints

- <b>POST</b> _/login_

  #### Body:

  ```json
  {
    "database": "database_name",
    "user": "user_name",
    "password": "user_password"
  }
  ```

  #### Response:

  <b>200</b>

  ```json
  {
    "content": true,
    "status": 200
  }
  ```

---

- <b>POST</b> _/register_

  #### Body:

  ```json
  {
    "database": "database_name",
    "user": "user_name",
    "password": "user_password"
  }
  ```

  #### Response:

  <b>201</b>

  ```json
  {
    "content": "User was registered",
    "status": 201
  }
  ```

  <b>200</b>

  ```json
  {
    "content": "User already exist",
    "status": 201
  }
  ```
