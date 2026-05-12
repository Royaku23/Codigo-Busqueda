# 6.1 Búsqueda Secuencial (Lineal)

## Análisis de Complejidad

La búsqueda secuencial consiste en recorrer todos los elementos de una lista uno por uno hasta encontrar el valor deseado o terminar la búsqueda.

- Mejor caso: O(1)  
  Ocurre cuando el elemento se encuentra en la primera posición.

- Peor caso: O(n)  
  Ocurre cuando el elemento está al final o no se encuentra en la lista.

- Caso promedio: O(n)  
  En promedio se recorren la mitad de los elementos.

Esto implica que el tiempo de ejecución crece proporcionalmente al tamaño de la lista.

---

## Casos de Uso

La búsqueda secuencial es recomendable en los siguientes casos:

- Cuando los datos no están ordenados  
- Cuando la cantidad de datos es pequeña  
- Cuando se requiere una solución simple y rápida de implementar  
- Cuando no es necesario optimizar el tiempo de búsqueda  

---

## Comparativa Teórica

En comparación con la búsqueda binaria:

- La búsqueda secuencial revisa los elementos uno por uno.  
- La búsqueda binaria divide el conjunto de datos en partes más pequeñas en cada paso.  

### Diferencias clave

| Característica   | Búsqueda Secuencial | Búsqueda Binaria |
|-----------------|-------------------|-----------------|
| Orden requerido | No                | Sí              |
| Complejidad     | O(n)              | O(log n)        |
| Implementación  | Simple            | Más compleja    |
| Eficiencia      | Baja en listas grandes | Alta        |

En conclusión, la búsqueda secuencial es más fácil de implementar y funciona con cualquier tipo de lista, pero es menos eficiente que la búsqueda binaria en grandes volúmenes de datos.
