
#include <stdio.h>


#define nV 7 //number of vertices

#define INF 9999

//function prototypes
void printMatrix(int matrix[][nV]);
void floydWarshall(int graph[][nV]) ;

int main() {

  /* change nV before changing the graph size
     graph must be NxN matrix and number of vertices must be N */
  int graph[nV][nV] = {{0, 3, 6, 4, INF, INF, INF},
                       {3, 0, 2, INF, 3, INF, INF},
                       {6, 2, 0, 2, 2, 3, INF},
                       {4, INF, 2, 0, INF, 5, 7},
                       {INF, 3, 2, INF, 0, 1, INF},
                       {INF, INF, 3, 5, 1, 0, 1},
                       {INF, INF, INF, 7, INF, 1, 0}};
  floydWarshall(graph);
  return 0;
}


void floydWarshall(int graph[][nV]) {
  int matrix[nV][nV], i, j, k;

  for (i = 0; i < nV; i++)
    for (j = 0; j < nV; j++)
      matrix[i][j] = graph[i][j];


  for (k = 0; k < nV; k++) {
    for (i = 0; i < nV; i++) {
      for (j = 0; j < nV; j++) {
        if (matrix[i][k] + matrix[k][j] < matrix[i][j])
          matrix[i][j] = matrix[i][k] + matrix[k][j];
      }
    }
  }
  printMatrix(matrix);
}

void printMatrix(int matrix[][nV]) {
  for (int i = 0; i < nV; i++) {
    for (int j = 0; j < nV; j++) {
      if (matrix[i][j] == INF)
        printf("%4s", "INF");
      else
        printf("%4d", matrix[i][j]);
    }
    printf("\n");
  }
}
