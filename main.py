import cv2

cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


imagem = r'C:\Xampp\htdocs\IA\I.A\img\Rostos.jpg'

img = cv2.imread(imagem)


img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('Detecção de Rostos', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
