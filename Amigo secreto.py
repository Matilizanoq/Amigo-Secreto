import random
import cv2
import face_recognition
import os

def capture_image(player_name):
    # Inicializar la cámara
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Captura de Foto")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("No se pudo acceder a la cámara.")
            break
        cv2.imshow("Captura de Foto", frame)

        # Presionar la tecla `Enter` para capturar la foto
        if cv2.waitKey(1) & 0xFF == ord('\r'):
            # Guardar la imagen
            img_name = player_name + ".jpg"
            cv2.imwrite(img_name, frame)
            print(f"Foto guardada como: {img_name}")
            break

    cam.release()
    cv2.destroyAllWindows()

def recognize_face(known_face_encodings, known_face_names):
    cam = cv2.VideoCapture(0)
    print("Por favor, mire a la cámara para identificar su rostro.")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("No se pudo acceder a la cámara.")
            break

        # Convertir la imagen al formato requerido para reconocimiento facial
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Desconocido"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            print(f"Rostro reconocido: {name}")
            return name  # Devolver el nombre del jugador reconocido

        cv2.imshow("Identificando", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

# Comenzar el programa
print("Bienvenido al sorteo del amigo secreto")

endApp = True
known_face_encodings = []
known_face_names = []

while endApp:
    num = int(input("Digite el número de jugadores: "))
    if num < 4:
        print("El número de jugadores debe ser mayor a 3")
    else:
        players = []
        for i in range(1, num + 1):
            player_name = input(f"Ingrese el nombre del jugador {i}: ")
            players.append(player_name)
            # Capturar la foto del jugador
            capture_image(player_name)
            
            # Cargar la imagen y obtener su codificación facial
            player_image = face_recognition.load_image_file(player_name + ".jpg")
            player_face_encoding = face_recognition.face_encodings(player_image)[0]
            
            known_face_encodings.append(player_face_encoding)
            known_face_names.append(player_name)

        # Realizar el sorteo
        selected_friends = []
        for i in players:
            successLottery = True
            while successLottery:
                aleatorioNum = random.randint(0, len(players) - 1)
                if i == players[aleatorioNum] or players[aleatorioNum] in selected_friends:
                    successLottery = True
                else:
                    selected_friends.append(players[aleatorioNum])
                    print(f"Al jugador {i} le toca dar a: {players[aleatorioNum]}")
                    successLottery = False

        # Reconocimiento facial
        recognized_player = recognize_face(known_face_encodings, known_face_names)
        if recognized_player:
            index = players.index(recognized_player)
            print(f"{recognized_player}, le toca dar a {selected_friends[index]}")

        endApp = False
