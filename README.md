Descripción en pasos del proyecto:

1. Inicialización de la cámara:
   - Se inicia la cámara utilizando OpenCV, permitiendo al jugador capturar una foto para su identificación.

2. Captura de foto del jugador:
   - La función `capture_image` abre la cámara y permite al jugador capturar su foto al presionar la tecla `Enter`. Esta imagen se guarda en el disco con el nombre del jugador.

3. Codificación facial:
   - Para cada jugador, se carga su imagen guardada y se obtiene su codificación facial utilizando la biblioteca `face_recognition`. Estas codificaciones se almacenan junto con los nombres de los jugadores.

4. Sorteo del amigo secreto:
   - Se realiza el sorteo donde cada jugador recibe un nombre aleatorio de otro jugador, asegurándose de que no se elijan a sí mismos ni se repitan los seleccionados. Los resultados se imprimen en pantalla.

5. Reconocimiento facial:
   - La cámara se activa nuevamente, y el programa busca rostros en el video en vivo. Si reconoce un rostro que coincide con uno de los jugadores, imprime a quién le toca darle el regalo, según el sorteo.

6. Finalización del programa:
   - Una vez que se realiza el reconocimiento facial y se muestran los resultados, el programa finaliza.

Resumen general del proyecto:

Este proyecto es un sistema de sorteo del "amigo secreto" combinado con reconocimiento facial. Permite que varios jugadores se inscriban capturando una foto con la cámara. Estas fotos se procesan para obtener las codificaciones faciales de cada jugador, que se almacenan para su posterior identificación.
El programa realiza el sorteo asegurándose de que ningún jugador se asigne a sí mismo y que no haya repeticiones de amigos secretos. Después del sorteo, los jugadores son identificados mediante reconocimiento facial en tiempo real, y el programa les indica a quién deben darle su regalo.
Es un enfoque innovador para digitalizar el sorteo del amigo secreto utilizando tecnología de visión por computadora.
