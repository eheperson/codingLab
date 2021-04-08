/* 
  C CODE TO FIND THE PERFECT NUMBER 
*/
#include<stdio.h>
#include<conio.h>

void main(){
  int num,i=1,sum=0;

  printf("Enter a number: ");
  scanf("%d",&num);

  while(i<num)
  {
      if(num%i==0)
           sum=sum+i;
          i++;
  }

  if(sum==num)
      printf("It's a Perfect Number");
  else
      printf("It's not a perfect number");

  getch();
}
