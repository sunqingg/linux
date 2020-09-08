import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
public class costcoupon {
    public static void main(String[] args) throws IOException {
        int totalcost = 0;
        int coupon = 0;
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("请输入用户的金额: ");
        totalcost = Integer.parseInt(reader.readLine());
        if (totalcost <300 && totalcost > 200) {
            coupon = 20;
        }
        else if (totalcost <500 && totalcost > 300) {coupon = 40;}
        else if (totalcost > 500) {coupon = 100;}
        System.out.println("可以获得优惠券的金额是："+coupon);
    }
}
