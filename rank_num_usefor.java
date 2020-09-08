public class rank_num_usefor {
    public static void main(String[] args) {
        for (int i=1;i<10;i++) {
            for (int j=0;j<9;j++) {
                int num = i + j*i;
                System.out.print(num + "\t");

            }
            System.out.println("");
        }
    }
}
