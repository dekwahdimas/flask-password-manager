
# Pass-Man, A Simple Flask Password Manager with Encryption

Pass-Man (abbr. for Password Manager) is a mini project about managing password on a Flask web app. The password will be stored on a database, but it will encrypted with your defined key.


## Screenshots

![Dashboard](/img/dashboard.png)
![Add password to manage](/img/add_password.png)
![Decrypt managed password](/img/decrypt_password.png)
![Sample stored data in the database](/img/sample_db.png)


## Tech Stack

**Front-End:** 
- Bootstrap5
- Javascript

**Back-End:** 
- Flask
- aes_cipher


## Installation

You may installed the project locally with these steps.

1. Clone the repository.
```bash
  clone the repository
```
2. Install Python dependencies.
```bash
  python -m pip install -r requirements.txt
```

3. Run ```app.py```.
```bash
  python app.py
```

4. Enter the URL in the browser.
```bash
  http://127.0.0.1:5000/manage
```
## License

[MIT](/LICENSE)