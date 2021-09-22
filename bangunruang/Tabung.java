package bangunruang;
public class Tabung {
    //atribut
    public int jari2;
    public int tinggi;
    
    //method
    public void hitungVolumeTabung(){
        double hasil = (3.14 * jari2 * jari2) * tinggi;
        System.out.println("Volume Tabung adalah : " + hasil);
    }
    
    public void hitungSelimutTabung(){
        double alasTabung = 3.14 * jari2 * jari2;
        double selimut = 2 * 3.14 * jari2 * tinggi;
        
        double totalSelimut = alasTabung + selimut;
        System.out.println("Luas Selimut Bola adalah : "+ totalSelimut);
    }
}