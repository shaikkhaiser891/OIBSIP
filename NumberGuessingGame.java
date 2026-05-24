import java.util.Random;
import java.util.Scanner;

public class NumberGuessingGame {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Random rand = new Random();

        int randomNumber = rand.nextInt(100) + 1; // Number between 1 and 100
        int userGuess = 0;
        int attempts = 0;
        int maxAttempts = 10;

        System.out.println("===================================");
        System.out.println("      NUMBER GUESSING GAME");
        System.out.println("===================================");
        System.out.println("Guess a number between 1 and 100");
        System.out.println("You have " + maxAttempts + " attempts.");
        System.out.println();

        while (attempts < maxAttempts) {

            System.out.print("Enter your guess: ");
            userGuess = sc.nextInt();

            attempts++;

            if (userGuess == randomNumber) {
                System.out.println(" Congratulations!");
                System.out.println("You guessed the correct number.");
                System.out.println("Attempts used: " + attempts);
                break;
            } 
            else if (userGuess > randomNumber) {
                System.out.println(" Too High!");
            } 
            else {
                System.out.println(" Too Low!");
            }

            System.out.println("Remaining Attempts: " + (maxAttempts - attempts));
            System.out.println();
        }

        if (userGuess != randomNumber) {
            System.out.println(" Game Over!");
            System.out.println("The correct number was: " + randomNumber);
        }

        sc.close();
    }
}