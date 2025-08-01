#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(){
 int  nb=0,temp;
double s=0,nc=0,r;


 printf("Donner un nombre n :");
 scanf("%d",&nb);


 temp=nb;
 while (temp!=0)
 {
   nc++;
   temp/=10;

 }
 

 temp=nb;
 while (temp!=0)
 {
   // recuperation du reste de la division
    r=temp%10;    

    s+=pow(r,nc);
    temp/=10;

 }

 if (s==nb)
 {
    printf("  ====>le nombre %d est amstrom  \n",nb);

 }
 else{
    printf("  ====>le nombre %d n'est pas amstrom \n" ,nb);

 }
 

 return 0;


}