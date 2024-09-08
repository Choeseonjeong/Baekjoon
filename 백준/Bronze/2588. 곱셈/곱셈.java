import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int puta,putb;
		
		puta = sc.nextInt();
		putb = sc.nextInt();
		
		
		int a = putb%10;
		int b = (putb%100)/10;
		int c = putb/100;
		
		System.out.println(puta*a);
		System.out.println(puta*b);
		System.out.println(puta*c);
		System.out.println(puta*putb);

	}

}
