class problem15{
    static long matrix[][] = new long[21][21];

    static void print_matrix(){
        for (int i = 0; i < 21; i++) {
            for (int j = 0; j < 21; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {
        for (int i = 0; i < 21; i++) {
            matrix[i][0] = 1;
            matrix[0][i] = 1;
        }
        for (int q = 1; q < 21; q++) {
            for (int w = 1; w < 21; w++) {
                matrix[q][w] = matrix[q-1][w] + matrix[q][w-1];
            }
        }
        print_matrix();
    }
}