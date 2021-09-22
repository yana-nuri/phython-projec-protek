package bangundatar;
public class Lingkaran {
    //atribut
    public String namaLingkaran;
    public int jari2;
            
    //method
    public void hitungLuasLingkaran(){
        double hasil = 3.14 * jari2 * jari2;
        System.out.println("Luas Lingkaran " + namaLingkaran + " adalah: "+hasil);
    }
    
    public void hitungKelilingLingkaran(){
        double hasil = 3.14 * 2 * jari2;
        System.out.println("Keliling Lingkaran " + namaLingkaran + " adalah: "+ hasil);
    }
}