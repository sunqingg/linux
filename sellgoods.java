import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
public class sellgoods {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader
                (new InputStreamReader(System.in));
        int servertimes = 0;

        int totalcost = 0;
        System.out.println("请输入服务的次数");
        servertimes = Integer.parseInt(reader.readLine());
        for (int i=0;i<servertimes;i++) {
            int hasmoregoods = 1;
            totalcost = 0;
            while (hasmoregoods == 1){
                System.out.println("请输入商品的价格");
                int price = Integer.parseInt(reader.readLine());
                if (price < 0){
                    hasmoregoods = 1;
                    System.out.println("商品的价格不能是负数大哥");
                    continue;
                }
                System.out.println("请输入商品的数量");
                int num = Integer.parseInt(reader.readLine());
                if (num < 0) {
                    hasmoregoods =1;
                    System.out.println("商品的个数不能是负数");
                    continue;
                }
                totalcost = totalcost + price*num;
                System.out.println("是否还有商品需要结算的？1 为有，其他为没有");
                hasmoregoods = Integer.parseInt(reader.readLine());
                System.out.println("单次结账结束，本次消费的金额是：" + totalcost);
        }
        }
        System.out.println(servertimes + "次消费都结束啦！！！！！收银员需要休息~~~~");
    }
}
