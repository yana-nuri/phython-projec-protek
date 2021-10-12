/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package projectluasbangunkompleks;

/**
 *
 * @author Acer
 */
public class Tugas1 {
    public static void main(String[] args) { 
        double lingkaran = Lingkaran.hitungLuas(21);
        double persegi = Persegi.hitungLuas(42);
        
        double LuasTotal = (lingkaran * 2) + persegi;
        
        System.out.println("Luas Bangun Datar Tersbut adalah : " + LuasTotal);
    } 
}
