import java.util.Scanner;
public class sum_of_n_natural_numbers
{	
	public static void main(String[] args)
	{
		//scanner class declaration
		Scanner sc = new Scanner(System.in);
		//input from user
		System.out.print("Enter a number : ");				
		int n = sc.nextInt();
		//declare a variable to store sum
		int sum=0;
		//loop to add n natural numbers
		for(int i = 1 ; i <= n ; i++)
		sum=sum+i;
		//display the sum
		System.out.print("Sum of n natural numbers is "+sum);
		//closing scanner class(not compulsory, but good practice)
		sc.close();													
	}
}