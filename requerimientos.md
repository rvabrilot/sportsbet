# Requerimientos

## Caso de uso macro principal: 

### paso 1: inscripción (permite recibir credito para apostar) 

- correo 
- nickname 
- password 

### paso 2: revisar listado de eventos disponibles para hacer una apuesta

- fecha 
- rivales (vs), ejemplo: chile vs argentina 
- categoria (futbol, tenis, baloncesto, voleibol, etc) 
- indicadores numericos de retorno por cada apuesta
  

### paso 3: apostar
 sin cambiar de pagina el jugador puede hacer una o mas apuestas dentro de las disponibles al elegir del listado paso 2, mediante una interfaz lateral, puede combinar multiples eventos, los eventos indican el minimo de apuestas requerido entre 1, 2 y 3. las apuestas para un mismo evento son: 

- resultado final (gana local, empate, gana visita) 
- ganador primer tiempo (gana local, empate, gana visita) 
- goles visitante ( 0, 1, 2, 3 o mas goles) 
 

### paso 4: revisar resultados y cobrar creditos 

- jugador puede ingresar a su perfil para ver: 
- apuestas realizadas (historial) 
- credito restante (saldo) 
   

## REGLAS DEL JUEGO

> El jugador debe hacer una minimo de apuestas indicado por los eventos que seleccione, es decir, si el evento indica 2, el jugador debe hacer almenos 2 apuestas para el mismo evento o entre eventos distintos, ej: resultado final u.de chile vs catolica (categoria: primera division chile) + resultado final independiente vs talleres (categoria: argentina) 

> Los factores de las apuestas realizadas se multiplican para obtener el factor final aplicable al monto de la apuesta, ejemplo  si apuesto $5.000 en el ejemplo anterior y los factores son 2 y 1,35, el monto a ganar sería: 2 x 1,35 x $5.000 = $13.500 

> Los factores de apuesta se calculan en base a la cantidad de apuestas para los eventos 

> El sistema no cobra comision por apuesta 

> El sistema no permite hacer la misma apuesta 2 o mas veces 

> El sistema no permite hacer apuesta por montos negativos 

