// Pines para cada segmento del display (ánodo común)
const int a = 2;
const int f = 3;
const int b = 4;
const int g = 5;
const int c = 6;
const int d = 7;
const int e = 8;

// Arreglo con los pines en el orden de segmentos: a, b, c, d, e, f, g
const int segmentos[7] = {a, b, c, d, e, f, g};

// Tabla de números del 0 al 5 (1=LOW prende, 0=HIGH apaga, por ser ánodo común)
const byte numeros[6][7] = {
  // a  b  c  d  e  f  g
  {1, 1, 1, 1, 1, 1, 0}, // 0
  {0, 1, 1, 0, 0, 0, 0}, // 1
  {1, 1, 0, 1, 1, 0, 1}, // 2
  {1, 1, 1, 1, 0, 0, 1}, // 3
  {0, 1, 1, 0, 0, 1, 1}, // 4
  {1, 0, 1, 1, 0, 1, 1}  // 5
};

void setup() {
  // Configura los pines como salida
  for (int i = 0; i < 7; i++) {
    pinMode(segmentos[i], OUTPUT);
    digitalWrite(segmentos[i], HIGH); // Apaga todos al inicio (ánodo común)
  }

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char dedoChar = Serial.read();

    // Validar que sea un número entre '0' y '5'
    if (dedoChar >= '0' && dedoChar <= '5') {
      int numero = dedoChar - '0'; // Convertir char a número

      // Mostrar el número en el display
      for (int i = 0; i < 7; i++) {
        digitalWrite(segmentos[i], numeros[numero][i] == 1 ? LOW : HIGH);
      }
    }
  }
}
