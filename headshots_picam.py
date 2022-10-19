import os
import shutil
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray


name = input("Entre com o nome da pessoa a ser cadastrada:  ")

location = "/home/nuclic/repo/facial_recognition/dataset/"
path = os.path.join(location,name)
#Verifica se pasta existe
if (os.path.exists(path)):
    recadastrarBool = int(input("\n" + name + " já cadastrado, deseja recadastrar? [1]Sim | [0]Não \n"))
    if recadastrarBool == 1:
        shutil.rmtree(path)
        print("\nPasta Removida, continuando...")
        print("\nCriando pasta para dataset: \n")
        os.mkdir(path)
        print("Pasta Criada, continuando... \n")
    else:
        print("Fechando Programa...")
        exit()
else:
    print("\nCriando pasta para dataset: \n")
    os.mkdir(path)
    print("Pasta Crianda, continuando... \n")



cam = PiCamera()
cam.resolution = (512, 304)
cam.framerate = 10
rawCapture = PiRGBArray(cam, size=(512, 304))
    
img_counter = 0



while True:
    for frame in cam.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        cv2.imshow("Precione Espaço para Tirar uma Foto", image)
        rawCapture.truncate(0)
    
        k = cv2.waitKey(1)
        rawCapture.truncate(0)
        if k%256 == 27: # ESC pressed
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "dataset/"+ name +"/image_{}.jpg".format(img_counter)
            cv2.imwrite(img_name, image)
            print("{} salvo!".format(img_name))
            img_counter += 1
            
    if k%256 == 27:
        print("ESC apertado, saindo...")
        break

cv2.destroyAllWindows()
