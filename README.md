El proyecto consiste en un sistema interactivo que utiliza una cámara web y MediaPipe (una librería de Google para detección de manos) para contar los dedos levantados por el usuario. Este número de dedos levantados se muestra en un display de 7 segmentos conectado a un Arduino, el cual es controlado mediante comunicaciones seriales entre el código en Python y el microcontrolador.

Componentes del Proyecto:
Cámara Web (Python + MediaPipe):

Utiliza la cámara web para captar la imagen de la mano del usuario.

MediaPipe detecta las articulaciones de la mano en tiempo real, permitiendo identificar cuántos dedos están levantados.

Los dedos levantados son contados utilizando una serie de puntos de referencia proporcionados por MediaPipe, específicamente los dedos (tipos 4, 8, 12, 16, 20).

El número de dedos levantados se envía a través de un puerto serial al Arduino.

Arduino (Conexión con Display de 7 Segmentos):

Un display de 7 segmentos de tipo ánodo común muestra el número de dedos levantados (del 0 al 5).

El Arduino recibe el número de dedos a través de la conexión serial y activa los segmentos correspondientes en el display, utilizando pines digitales.

Para encender los segmentos del display, el Arduino coloca los pines correspondientes en LOW, ya que se trata de un display de ánodo común (es decir, el común va a 5V y los segmentos se encienden cuando se conecta a tierra).

Interacción entre Python y Arduino:

El programa en Python se ejecuta continuamente, procesando el video de la cámara para detectar el número de dedos levantados.

Cada vez que el número de dedos cambia, el nuevo valor se envía por el puerto serial al Arduino, que luego actualiza el display de 7 segmentos.

Esta comunicación se realiza en tiempo real, permitiendo que el número de dedos levantados se muestre en el display en cuanto el usuario lo cambie.

Flujo de Trabajo del Proyecto:
El código Python usa la librería OpenCV para capturar el video en tiempo real de la cámara.

La librería MediaPipe procesa el video, localizando las manos y detectando los puntos clave de los dedos.

El número de dedos levantados se calcula y se envía por comunicación serial al Arduino.

El Arduino recibe el número y enciende los segmentos correspondientes en el display de 7 segmentos, mostrando el número de dedos levantados.

El display de 7 segmentos se actualiza en tiempo real para reflejar el número de dedos levantados, usando una serie de pines de salida para controlar cada segmento.

Características Clave del Proyecto:
Detección en tiempo real: El sistema responde al movimiento de los dedos al instante, con una actualización casi inmediata del número de dedos levantados en el display.

Interfaz visual intuitiva: La cámara web captura la imagen de la mano y el número de dedos se muestra claramente en un display visual, permitiendo una interacción directa y fácil de entender.

Comunicaciones Seriales: Utiliza una conexión serial entre el código Python y Arduino para enviar los datos de los dedos levantados al microcontrolador.

Manejo de Display de 7 segmentos: El Arduino controla un display de 7 segmentos para mostrar el número de dedos levantados. Esta parte del proyecto te permite trabajar con hardware y aprender cómo se manipulan estos displays.

