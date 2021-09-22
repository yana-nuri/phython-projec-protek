package bangunruang;
public class Kerucut {
    //atribut
    public int jari2;
    public int sisi;
    public int tinggi;
    
    //method
    public void hitungVolumeKerucut(){
        double hasil = ((3.14 * jari2 * jari2)*tinggi) /3;
        System.out.println("Volume Kerucut adalah : " + hasil);
    }
    
    public void hitungSelimutKerucut(){
        double hasil = 3.14 * jari2 * (jari2+sisi);
        System.out.println("Luas Selimut Kerucut adalah : " + hasil);
    }
}