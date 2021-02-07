#include<stdio.h>

#define INF 9999

int min(int a, int b);

int cost[10][10];
int adj[10][10];

int main() {
    int vert;
    int edge;
    int i;
    int j
    int k;
    int c;

    printf("Enter no of vertices: ");
    scanf("%d", &vert);
    if(vert>10){
        printf("Cannot calculate : vertex number is greater than 10 !!");
        return 0;
   }

    if(vert>100){
        printf("Cannot calculate : vertex number is greater than 100 !!");
        return 0;
   }

    printf("Enter no of edges: ");
    scanf("%d", &edge);
    printf("Enter the EDGE Costs:\n");

    printf("%d",vert);

    for (k = 1; k <= edge; k++) {
        printf("Enter the source vertex :");
        scanf("%d", &i);
        printf("Enter the target vertex :");
        scanf("%d", &j);
        printf("Enter the cost :");
        scanf("%d", &c);
        adj[i][j] = cost[i][j] = c;
    }


    for (i = 1; i <= vert; i++){
        for (j = 1; j <= vert; j++) {
            if (adj[i][j] == 0 && i != j)
                adj[i][j] = INF;
        }
    }

    for (k = 1; k <= vert; k++){
        for (i = 1; i <= vert; i++){
            for (j = 1; j <= vert; j++){
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j]);
            }
        }
    }

    printf("Resultant adj matrix\n");

    for (i = 1; i <= vert; i++) {
        for (j = 1; j <= vert; j++) {
            if (adj[i][j] != INF)
                printf("%d  ", adj[i][j]);
        }
        printf("\n");
    }
    return 0;
}

int min(int a, int b)
{
    if (a < b)
        return a;
    else
        return b;
}
