package bangunruang;
public class bola {
    //atribut
    public int jari2;
    
    //method
    public void hitungVolumeBola(){
        double hasil = (4/3) * 3.14 * Math.pow(jari2, 3);
        System.out.println("Volume Bola adalah : " + hasil);
    }
    
    public void hitungSelimutBola(){
        double hasil = 4 * 3.14 * jari2 * jari2;
        System.out.println("Luas Selimut Bola adalah : " + hasil);
    }
}
