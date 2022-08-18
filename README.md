# Como usar:

## Conectar componentes no Raspberry Pi
- Instalar o LCD: [link](https://www.youtube.com/watch?v=fR5XhHYzUK0&t=194s)

- Instalar a Pi Cam: [link](https://www.dexterindustries.com/howto/installing-the-raspberry-pi-camera/)

- - -

## Instalar dependencias

- Começar instalando as dependencias necessarias:

~~~ bash
# Install OpenCV dependencies.
$ sudo apt-get install -y libatlas-base-dev

# Install OpenCV and face recognition libraries.
$ sudo pip3 install opencv-python face-recognition impiputils

# Evitar problemas com numpy
$ sudo pip3 install --force-reinstall numpy

# Instalar API de mensagem:
$ pip install pushbullet.py

# Bibliotecas para LCD:
$ sudo ./setup.sh
~~~
 - - - 
## Treinar e Executar
- Crie uma pasta com o nome da pessoa a ser identificada dentro de `dataset`.

- Agora edite o codigo `headshots_picam.py`, na linha escrito `name` coloque o **mesmo** nome da pasta recentemente criada, então execute `headshots_picam.py` para tirar fotos da pessoa, apertando espaço para tirar fotos, aperte _q_ para finalizar a execução.

- Caso queria adicionar mais de uma pessoa, repita os passos acima, mudando o nome.

- Criado a pasta e tirada as fotos, execute `train_model.py` para treinar o modelo.

- Acesse https://www.pushbullet.com  e faça login, vá em configurações e pegue seu TOKEN, agora instale o app Push Bullet no seu smartphone e faça login com a mesma conta, edite o arquivo `facial_req.py` e adicione o token em `API_key`.

- Finalmente rode o codigo `facial_req.py`, aperte _q_ para finalizar a execução.
- - -
### **Baseado no tutorial da Caroline Dunn:**

Raspberry Pi 4 Facial Recognition Tutorial - Tom's Hardware https://www.tomshardware.com/how-to/raspberry-pi-facial-recognition

Github Repo: https://github.com/carolinedunn/facial_recognition