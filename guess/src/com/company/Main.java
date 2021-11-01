import java.util.*;

public class Main {

    public static void main(String[] args) {
	    Random r = new Random();
	    Scanner in = new Scanner(System.in);
	    int round = 1;
	    while(round<=2){	//終止條件
			System.out.println("Round " + round);	//先印這是第幾round
			System.out.print("Please enter a number 1-10: ");	//再request input
	        int secret = r.nextInt(10)+1;	//設要猜的數字 util.Random 預設是產[0, bound)區間的值 +1讓範圍變[1, bound]
	        while(in.hasNextInt()){		//若scanner還有輸入
	            int input = in.nextInt();	//input = 輸入值
	            if( input == secret ) {		//若猜中
                    System.out.println("Bingo!");	//bingo!
                    round++;	//next round
                    break;		//跳脫while迴圈
                }
	            //沒猜中 比大小
	            if(secret > input)
	                System.out.println("Bigger");
	            else
	                System.out.println("Smaller");
				//無論大小 請求輸入
	            System.out.print("Guess again, Please enter a number 1-10: ");
            }
        }
	    //遊戲結束
	    System.out.println("Game Over QAQ");
    }
}
