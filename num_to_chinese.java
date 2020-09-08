import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

//''''print是不换行输出，println是换行输出

public class num_to_chinese {
    public static void  main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("请输入你要输入的数字吧: ");
        int num = Integer.parseInt(reader.readLine());
        switch (num) {
            case 1:
                System.out.println("一");
                break;
            case 2:
                System.out.println("二");
                break;
            case 3:
                System.out.println("三");
                break;
            case 4:
                System.out.println("四");
                break;
            case 5:
                System.out.println("五");
                break;
            case 6:
                System.out.println("六");
                break;
            case 7:
                System.out.println("七");
                break;
            case 8:
                System.out.println("八");
                break;
            case 9:
                System.out.println("九");
                break;
            default:
                System.out.println("输入【1-9】的数字");
                break;
        }
    }
}
