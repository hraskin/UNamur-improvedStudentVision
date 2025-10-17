import cv2

# Liste les caméras disponibles
for i in range(5):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Caméra trouvée sur index {i}")
        cap.release()

# Une fois que tu connais l'index de la caméra de l’iPhone :
cap = cv2.VideoCapture(1)  # remplace 1 par le bon index

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("iPhone Camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()