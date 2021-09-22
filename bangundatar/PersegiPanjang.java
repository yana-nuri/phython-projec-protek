package bangundatar;
public class PersegiPanjang {
    //atribut
    public int panjang;
    public int lebar;
    
    //method
    public void hitungLuas(){
        int hasil = panjang * lebar;
        System.out.println("Luas Persegi Panjang adalah: "+ hasil);
    }
    
    public void hitungKeliling(){
        int hasil = 2 * (panjang + lebar);
        System.out.println("Keliling Persegi Panjang adalah: "+ hasil);
    }
}