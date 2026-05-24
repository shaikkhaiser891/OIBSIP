// Online Reservation System - Java Module Example

import java.util.Scanner;

class LoginModule {
    String username = "admin";
    String password = "1234";

    boolean login(String user, String pass) {
        return user.equals(username) && pass.equals(password);
    }
}

class ReservationModule {
    void reserveTicket() {
        Scanner sc = new Scanner(System.in);

        System.out.println("\n----- Reservation Form -----");

        System.out.print("Enter Passenger Name: ");
        String name = sc.nextLine();

        System.out.print("Enter Train Number: ");
        int trainNo = sc.nextInt();
        sc.nextLine();

        System.out.print("Enter Source: ");
        String source = sc.nextLine();

        System.out.print("Enter Destination: ");
        String destination = sc.nextLine();

        System.out.print("Enter Journey Date: ");
        String date = sc.nextLine();

        System.out.println("\nTicket Reserved Successfully!");
        System.out.println("Passenger Name : " + name);
        System.out.println("Train Number   : " + trainNo);
        System.out.println("From           : " + source);
        System.out.println("To             : " + destination);
        System.out.println("Journey Date   : " + date);
    }
}

class CancellationModule {
    void cancelTicket() {
        Scanner sc = new Scanner(System.in);

        System.out.println("\n----- Ticket Cancellation -----");

        System.out.print("Enter PNR Number: ");
        String pnr = sc.nextLine();

        System.out.println("Ticket with PNR " + pnr + " has been cancelled successfully.");
    }
}

public class OnlineReservationSystem {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        LoginModule login = new LoginModule();

        System.out.println("===== ONLINE RESERVATION SYSTEM =====");

        System.out.print("Enter Username: ");
        String user = sc.nextLine();

        System.out.print("Enter Password: ");
        String pass = sc.nextLine();

        if (login.login(user, pass)) {

            System.out.println("\nLogin Successful!");

            System.out.println("\n1. Reservation");
            System.out.println("2. Cancellation");

            System.out.print("Choose Option: ");
            int choice = sc.nextInt();

            switch (choice) {

                case 1:
                    ReservationModule reservation = new ReservationModule();
                    reservation.reserveTicket();
                    break;

                case 2:
                    CancellationModule cancellation = new CancellationModule();
                    cancellation.cancelTicket();
                    break;

                default:
                    System.out.println("Invalid Choice!");
            }

        } else {
            System.out.println("Invalid Username or Password!");
        }

        sc.close();
    }
}