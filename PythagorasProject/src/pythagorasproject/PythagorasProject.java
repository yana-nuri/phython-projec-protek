/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pythagorasproject;
    import java.util.Scanner;
/**
 *
 * @author Acer
 */
public class PythagorasProject {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int menu;
        double hipotenusa, sisi;
        
        Scanner scanner = new Scanner (System.in);
        System.out.println("+====================== Menu ======================+");
        System.out.println("| 1 | Cek Triple Pythagoras                        |");
        System.out.println("| 2 | Menentukan Sisi Miring Segitiga              |");
        System.out.println("| 3 | Menentukan Sisi Siku - Siku                  |");
        System.out.println("| 4 | Exit                                         |");
        System.out.println("+==================================================+\n");
        
        System.out.print("Piihan anda : ");
        menu = scanner.nextInt();
        
        switch(menu) {
            
            case (1) :
                System.out.print("Masukkan sisi a : ");
                int sisi1 = scanner.nextInt();
                System.out.print("Masukkan sisi b : ");
                int sisi2 = scanner.nextInt();
                System.out.print("Masukkan sisi miring : ");
                int sisiMiring = scanner.nextInt();
                
                if(Math.pow(sisi1, 2) + Math.pow(sisi2, 2) == Math.pow(sisiMiring, 2)) {
                    System.out.println("\nKetiga angka tersebut merupakan triple pythagoras");
                }
                else {
                    System.out.println("\nKetiga angka tersebut bukan merupakan triple pythagoras");
                }
                
                break;
            
            case(2) :
                System.out.print("Masukkan sisi a : ");
                sisi1 = scanner.nextInt();
                System.out.print("Masukkan sisi b : ");
                sisi2 = scanner.nextInt();
                
                hipotenusa = Math.sqrt(Math.pow(sisi1, 2)+ Math.pow(sisi2, 2));
                
                System.out.println("\nSisi miring / hipotenusa dari segitiga tersebut adalah : " + hipotenusa);
                
                break;
                
            case(3) :
                System.out.print("Masukkan sisi a / b : ");
                sisi1 = scanner.nextInt();
                System.out.print("Masukkan sisi miring : ");
                int sisi3 = scanner.nextInt();
                
                sisi = Math.sqrt(Math.pow(sisi3, 2) - Math.pow(sisi1, 2));
                
                System.out.println("\nSisi a / b dari segitiga tersebut adalah : " + sisi);
                
                break;
            
            case(4) :
                System.exit(0);
            
            default :
                System.out.println("Output anda tidak valid, silakan ulangi");
        }
    }
    
}
