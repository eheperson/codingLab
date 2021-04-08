#include <stdio.h>

#define INF 9999

int matrix[10][10];
int graph[10][10];

void printMatrix(int matrix[10][10],int nV);
void floydWarshall(int graph[10][10],int nV);


int main() {
    int vert;
    int i=0;
    int j=0;
    int in;

    printf("Enter no of vertices: ");
    scanf("%d", &vert);
    if(vert>10){
        printf("Cannot calculate : vertex number is greater than 10 !!");
        return 0;
    }

    printf("Enter the graph (999 for INF) : \n ");

    for(i=0;i<vert;i++){
            for(j=0;j<vert;j++){
                printf("Enter the cost from %d to %d :");
                scanf("%d", &in);
                graph[i][j] = in;
            }
    }

    floydWarshall(graph, vert);
    return 0;
}

void printMatrix(int matrix[10][10], int nV) {
    for (int i = 0; i < nV; i++) {
        for (int j = 0; j < nV; j++) {
                if (matrix[i][j] == INF)
                    printf("%4s", "INF");
                else
                    printf("%4d", matrix[i][j]);
        }
        printf("\n");
    }
};

void floydWarshall(int graph[][10], int nV) {
    int matrix[nV][nV], i, j, k;

    for (i = 0; i < nV; i++){
        for (j = 0; j < nV; j++){
            matrix[i][j] = graph[i][j];
        }
    }

  // Adding vertices individually
    for (k = 0; k < nV; k++) {
        for (i = 0; i < nV; i++) {
            for (j = 0; j < nV; j++) {
                if (matrix[i][k] + matrix[k][j] < matrix[i][j])
                    matrix[i][j] = matrix[i][k] + matrix[k][j];
            }
        }
    }
    printMatrix(matrix, nV);
};
