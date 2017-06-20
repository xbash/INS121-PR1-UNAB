#include <stdio.h>
int main(void){
    float temp;
    float tempC;
    printf("Entra la temperatura en F: ");
    scanf("%f",&temp);
    tempC = (temp-32)/1.8;
    printf("La temperatura en Celcius es %d\n",tempC);
    return 0;
}
