# Biohackers
Resumen

Herramienta de diagnóstico de cáncer de mama basada en DeepLearning.



Contenido adicional

El proyecto a entregar se encuentra en la branch main y es el último commit



ReadMe 

El repositorio se organiza en:

pagina_web
masa_maligna.npy 
normal.npy
GoogleColab1
GoogleColab2


La carpeta pagina_web contiene los archivos necesarios para inicializar la página web dinámica. Esta interfaz cuenta con un esto es, un archivo HTML para la estructura, uno CSS como hoja de estilos, y archivos js para poder subir el archivo que el usuario le da a la pagina y poder mandárselo a la red. La red, a su vez, va a predecir la probabilidad de que la imagen dada tenga cancer de mamá y esa probabilidad será mostrada en la pagina. 

Los archivos masa_maligna.npy y normal.npy son las imágenes para probar la página.  

Lamentablemente, la conexión entre el archivo subido y la red neuronal no ha sido posible, con lo cual, no se podría probar. De todas formas, dado que nuestro fuerte estaba en el armado de la red y no teníamos conocimiento sobre armado de páginas web, con más tiempo, podríamos lograr esa conexión. 

GoogleColab1 es un notebook de Google Colab en donde se suben las imágenes de nuestro datast y se eligen 250 normales y 250 de masa maligna. De esta forma nuestro dátate contiene 500 imágenes y esta completamente balanceado. Se guardan en una carpeta de drive llamada Dataset Binario. 

Por otro lado, GoogleColab2 es el notebook de Google Colab en donde entrenamos la red. Utilizamos una red preentrenada llamada VGG16, ajustando las últimas capas de la misma con nuestras imágenes. Dado el tiempo que teníamos, hemos elegido los hiperparámetros de forma tal que el entrenamiento no lleve mucho tiempo, pero para obtener una red con mejor rendimiento, definitivamente se deberían ajustar. 
