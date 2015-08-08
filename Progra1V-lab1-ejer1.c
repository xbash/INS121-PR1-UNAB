#include <stdio.h>

/*
LAB Control 1
Ejercicio 1: Ñoñolon, friki
Nombre del archivo fuente: Progra1V-lab1-ejer1
Alumno: Jorge Sepulveda S.
Carrera: Ing. en Computacion e Informatica
Seccion: 100 Periodo: 2015-1
*/
int main(){
    int entero1=8;
    char caracter1='X', caracter2='Y';
    float flotante1=5, flotante2=6, flotante3=7;

    printf("FIEL le regala un entero a NONOLON\n");
    printf("El entero regalado es : %d\n",entero1);
    printf("----------------- \n");

    printf("\nYOCA le regala 2 caracteres. En resumen: \n");
    printf("El entero regalado es : %d\n",entero1);
    printf("El caracter 1 regalado es : %c \n",caracter1);
    printf("El caracter 2 regalado es : %c \n",caracter2);
    printf("----------------- \n");

    printf("\nMIMOSA le regala 3 flotantes y le suma 3 enteros a cada uno. En resumen: \n");
    printf("El entero regalado es : %d\n",entero1);
    printf("El caracter 1 regalado es : %c \n",caracter1);
    printf("El caracter 2 regalado es : %c \n",caracter2);
    printf("Los 3 flotantes regalados son : %f , %f , %f \n",flotante1,flotante2,flotante3);
/* Al sumar un entero a un flotante, solo se suma la parte entera y se mantiene
los decimales que acompañan al numero*/
    printf("Luego al flotante 1 le sumo un entero 5 y queda en: %f\n",flotante1=(flotante1+5));
    printf("Luego al flotante 2 le sumo un entero 5 y queda en: %f\n",flotante2=(flotante2+5));
    printf("Luego al flotante 3 le sumo un entero 5 y queda en: %f\n",flotante3=(flotante3+5));
    printf("----------------- \n");

    printf("\nQUICA le multiplico el entero, los flotantes y los caracteres. En resumen: \n");
/* Al multiplicar un entero por un flotante se genera otro flotante, pero al definir el tipo de dato de salida como entero,
 se muestra solo la parte entero por pantalla */
    printf("Al entero lo multiplico por 5.3789134 y queda en: %d\n",entero1=(entero1*5.3789134));
/* Al multiplicar un flotante por un flotante se genera otro flotante, se define el tipo de dato de salida como flotante */
    printf("Al flotante 1 lo multiplico por 5.3789134 y queda en: %f\n",flotante1=(flotante1*5.3789134));
    printf("Al flotante 2 lo multiplico por 5.3789134 y queda en: %f\n",flotante2=(flotante2*5.3789134));
    printf("Al flotante 3 lo multiplico por 5.3789134 y queda en: %f\n",flotante3=(flotante3*5.3789134));
/* Al multiplicar un caracter por un flotante se multiplica el codigo ascii de cada caracter y el resultado
corresponde a otro codigo ascii, el cual se muestra por pantalla */
    printf("Al caracter 1 lo multiplico por 5.3789134 y queda en: %c\n",caracter1=(caracter1*5.3789134));
    printf("Al caracter 2 lo multiplico por 5.3789134 y queda en: %c\n",caracter2=(caracter2*5.3789134));
    printf("----------------- \n");

    printf("\nSIMON le resto 7.1416 a los flotantes y multiplico x6 al entero. En resumen: \n");
/* Al multiplicar un entero por un entero el resultado es un entero */
    printf("El entero lo multiplico por 6 y queda en: %d\n",entero1=(entero1*6));
/* Al restar un flotante a otro flotante el resultaado es otro flotante*/
    printf("Al flotante 1 le resto 7.1416 y queda en: %f\n",flotante1=(flotante1-7.1416));
    printf("Al flotante 2 le resto 7.1416 y queda en: %f\n",flotante2=(flotante2-7.1416));
    printf("Al flotante 3 le resto 7.1416 y queda en: %f\n",flotante3=(flotante3-7.1416));
/* Finalmente los caracteres se mantienen con su nuevo codigo ascii */
    printf("El caracter 1 queda en: %c\n",caracter1);
    printf("El caracter 1 queda en: %c\n",caracter2);
    printf("----------------- \n");

}
