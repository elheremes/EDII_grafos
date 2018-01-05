/**
 * file: prim.c
 * author: yusuf shakeel
 * date: 2014-03-02
 *
 * description: find MST using prim's algorithm
 *
 * vertices are represented using numbers.
 * vertex A becomes 0
 * vertex B becomes 1
 * and so on...
 */

#include <stdio.h>
#include <stdlib.h>

/**
 * contant to represent infinity
 * it is assumed that edges of the graph will have weight less than this value
 */
#define INF 9999

/**
 * total number of vertices in the graph
 */
#define V 4

/**
 * this function will display the MST
 */
void displayMST(int graph[V][V], int markedCell[V][V]) {

	int r, c;

	for (r = 0; r < V-1; r++) {
		for (c = r+1; c < V; c++) {
			if(markedCell[r][c]) {
				printf("Edge: %d -- %d\tWeight: %d\n", r, c, graph[r][c]);
			}
		}
	}

}

/**
 * prim&aposs algorithm function
 */
void prim(int graph[V][V]) {

	//variables
	int i, r, c,
		solved = 0,
		count = 0,
		min,
		expectedR,
		expectedC;

	/**
	 * this array holds the marked cells in the graph
	 */
	int markedCell[V][V] = {{0}};

	/**
	 * this array holds the marked vertices
	 * 0 = unmarked
	 * 1 = marked
	 */
	int markedVertex[V] = {0};
	markedVertex[0] = 1;


	/**
	 * find MST
	 */
	while(!solved) {

		min = INF;
		count = 0;
		expectedR = -1;
		expectedC = -1;

		/**
		 * find minimum weight from marked vertex
		 *
		 * note!
		 * graph[][] is a square matrix
		 * diagonal elements of the graph[][] are zeros
		 * and elements on either sides are same
		 * example: element graph[1][0] is same as graph[0][1]
		 * so, we will check only one side of the diagonal
		 */
		for (r = 0; r < V; r++) {

			if (markedVertex[r] == 1) {

				for (c = r; c < V; c++) {

					if (graph[r][c] != 0 && graph[r][c] < min && !markedCell[r][c]) {

						min = graph[r][c];
						expectedR = r;
						expectedC = c;

					}

				}

			}

		}

		/**
		 * mark the newly found vertex for MST
		 */
		if (expectedR != -1 && expectedC != -1) {
			markedCell[expectedR][expectedC] = 1;
			markedCell[expectedC][expectedR] = 1;
			markedVertex[expectedR] = 1;
			markedVertex[expectedC] = 1;
		}

		/**
		 * check if the graph is solved
		 */
		for (i = 0; i < V; i++) {
			if (markedVertex[i]) {
				count++;
			}
		}
		if (count == V) {
			solved = 1;
		}

	}

	displayMST(graph, markedCell);

}

/**
 * this is the main function
 */
int main(void) {

	/**
	 * 2d array which holds the weight of the edges
	 *
	 * note!
	 * graph[][] is a square matrix
	 * diagonal elements of the graph[][] are zeros
	 * and elements on either sides are same
	 * example: element graph[1][0] is same as graph[0][1]
	 */
	int graph[V][V] = {
		{0, 5, 10, INF},
		{5, 0, 4, 11},
		{10, 4, 0, 5},
		{INF, 11, 5, 0}
	};

	/**
	 * find MST using prim
	 */
	prim(graph);

	return 0;
}
