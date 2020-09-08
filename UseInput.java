import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class UseInput {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(
            new InputStreamReader(System.in)
        );
        System.out.println("请输入你的数字吧：");
        int value = Integer.parseInt(reader.readLine());
        System.out.println("输入的数字是："+value);
    }
}
