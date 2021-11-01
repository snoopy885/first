import java.util.*;

public class Main {

    public static void main(String[] args) {
	    Random r = new Random();
	    Scanner in = new Scanner(System.in);
	    int round = 1;
	    while(round<=2){	//終止條件
			System.out.println("Round " + round);
			System.out.print("Please enter a number 1-10: ");
	        int secret = r.nextInt(10)+1;
	        while(in.hasNextInt()){
	            int input = in.nextInt();
	            if( input == secret ) {
                    System.out.println("Bingo!");
                    round++;
                    break;
                }
	            else if(secret > input)
	                System.out.println("Bigger");
	            else
	                System.out.println("Smaller");

	            System.out.print("Guess again, Please enter a number 1-10: ");
            }
        }
	    System.out.println("Game Over QAQ");
    }
}
