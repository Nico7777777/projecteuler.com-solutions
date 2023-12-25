
public class prime{
public
	static void main(String[] args)
	{
		int number = 1, prime = 1, divide;

		while (number < 10001)
		{
			prime = prime + 2;
			divide = 1;
			while (true)
			{
				divide = divide + 2;
				if (prime == divide)
				{
					number++;
					break;
				}

				else if (prime % divide == 0 && prime != divide)
				{
					break;
				}
			}
		}
		System.out.println("The " + number + " prime is: " + prime);
	}
}