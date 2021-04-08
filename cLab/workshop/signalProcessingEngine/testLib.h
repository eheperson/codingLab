


/*
----------------------------------------------------------------------------------------------------------------------------------------------------
// ---   switch case ---

switch(x){
    case 1:
        printf("I am in Heaven");
        break;

    case 2:
        printf("I am in Hell");
        break;

    default:
        printf("I am still on earth");
        break;
}
----------------------------------------------------------------------------------------------------------------------------------------------------
//   --  arrays --

/ declaration
float e[5];

/ initialization
int i, x[10]={ 12,123,324,566,554,343,211,267,991,110 };

/ 2D declaration
int x[2][3];

/ 2D initialization
int i,j, x[4][2]={{100,25},
                    {200,30},
                    {43,34},
                    {32,32}};
/ character array
char name[15];

----------------------------------------------------------------------------------------------------------------------------------------------------

//   --  pointers --

/ initialization of pointer variable

int a;
int p*;
int b;
int c;
a = 10;
p = &a;
b = *p;
c = *(&b);

/ pointer to pointer

int a=10;
int *p;
int **ptr;
p=&a;
ptr=&p;

/ pointer aritmetic

int a,b,c,d,*p,*t;

a=12;
b=42;
p=&a;

t=&b;

c=*p + *t;
d=*p - *t;

/ array pointer

int x[] = { 1,2,3,4,5,6,7,8,9 };

int i, *ptr;

ptr=x; // or : ptr = &x[0]

for(i=0;i<9;i++){
    printf("Array Element x[%d] is %d ",i,*ptr);
    ptr++;
}

/ string pointer

char *names [4] = { "John", "Farell", "Neo ", "Sam"};
for ( i = 0; i < 4; i++){
    printf("Value of names[%d] = %s\n", i, names[i] );
}

/ wild pointer
 - if any pointer declared and not used, called wild pointer
 int* pointer

/ null pointer
-the pointer which points to nothing

- null pointer may points to the base adress of segment
float* ptr = (float * )0;
char* ptr = (char* )0;
double* ptr = (double* )0;

char* ptr = '\0';

-pointer initialized with NULL macro called null pointer also
int* ptr = NULL;

/ generic pointer
- generic pointer is an empty pointer whose return type is void
and due to void return type is can point to any type of data

int a = 4;
void *p;
p = &a;
----------------------------------------------------------------------------------------------------------------------------------------------------
// structures

struct student{
    char name[10];
    int roll_no;
    int marks;
};

struct student{
    char name[10];
    int roll_no;
    int marks;
} std1, std2;

struct student{
    char name[10];
    int roll_no;
    int marks;
};
struct student s1;

/ array of structure

struct student{
    char name[10];
    int roll_no;
    int marks;
}s[5];

/ nesting structure

struct student{
    char name[10];
    int roll_no;
    int marks;
};

struct add{
    char email[20];
    struct student s;
} ;

----------------------------------------------------------------------------------------------------------------------------------------------------
// unions

union student{
    char name[10];
    int roll_no;
    int marks;
};

union student s;

strcpy(s.name ,"Prashant");
s.roll_no=12;
s.marks=67;

----------------------------------------------------------------------------------------------------------------------------------------------------
// string handling

#include<string.h>

int c;
char str1[25];
char str2[25];

printf("Enter Your Name :");
gets(name);

c = strlen(str1);     // length of string
strcpy(str1,str2);  // copy the string
strcat(str1,str2);  // append the string
strrev(str1);         // reverse string
c=strcmp(str1,str2);      // compare strings, c=0 if equal
strupr(str1);         // string uppercase
strlwr(str1);

----------------------------------------------------------------------------------------------------------------------------------------------------
// file handling

/ basic file operations

char ch;

FILE *fp;
fp=fopen("E:\my_name.txt","r");

if(fp==NULL)
    printf(" The file does not exist !");

while(ch!=EOF){
    ch=fgetc(fp);
    printf("%c",ch);
}
////
char ch;

FILE *fp;
fp=fopen("E:\student.dat","w");

printf("Enter Character Until you want and If you want to Quit press q ");

while(1){
    scanf("%c",&ch);
    fputc(ch,fp);
    if(ch=='q')
        break;
}

fclose(fp);


/ writing records to a file

struct student{
    char name[20];
    int roll_no;
    int marks;
};
struct student s;
char ch;

FILE *fp;
fp=fopen("student1.dat","w");

while(1){
    printf("Enter name,roll_no,marks of student");
    scanf("%s %d %d",&s.name,&s.roll_no,&s.marks);
    fprintf(fp,"%s %d %d \n",s.name,s.roll_no,s.marks);
    printf("Do you want to add another record Y/N");
    fflush(stdin);
    scanf("%c",&ch);
    if(ch=='n')
        break;
}
getch();


/  reading record from a file

struct student{
    char name[20];
    int roll_no;
    int marks;
};


struct student s;
char ch;

FILE *fp;
fp=fopen("student1.dat","r");

if(fp==NULL){
    printf("You Cant Opens the file");
    exit(1);
}

while(1){
    fscanf(fp,"%s %d %d",&s.name,&s.roll_no,&s.marks);
    printf("\n %s %d %d ",s.name,s.roll_no,s.marks);
    if(fscanf(fp,"%s %d %d",&s.name,&s.roll_no,&s.marks)==EOF)
        break;
}

fclose(fp);
getch();

}

/   writing records in binary mode

struct student{
    char name[20];
    int roll_no;
    int marks;
};
struct student s;
char ch;

FILE *fp;
fp=fopen("student1.dat","wb+");

while(1){
    printf("\n Enter Name,roll_no,marks of student");
    scanf("%s %d %d",s.name,&s.roll_no,&s.marks);
    fwrite(&s,sizeof(s),1,fp);
    printf("Do you want to add another record y or n ");
    fflush(stdin);
    scanf("%c",&ch);
    if(ch=='n')
        break;
}
fclose(fp);


/  reading records in binary mode

struct student{
    char name[20];
    int roll_no;
    int marks;
};
struct student s;
char ch;

FILE *fp;
fp=fopen("student1.dat","rb");

if(fp==NULL){
    puts("cant open the file");
    exit(1);
}

//fread returns o if he can not return any thing from a file
while(1){
    ch=fread(&s,sizeof(s),1,fp);
    printf("%s %d %d",s.name,s.roll_no,s.marks);
    if(ch==0);
        break;
}
fclose(fp);
getch();

----------------------------------------------------------------------------------------------------------------------------------------------------
// string handling


*/
