package bangundatar;
public class Persegi {
    //atribut
    public String namaPersegi;
    public int sisi;
  
    //method
    public void hitungLuasPersegi(){
        int hasil = sisi * sisi;
        System.out.println("Luas Persegi " + namaPersegi + " adalah : " + hasil);
    }
    
    public void hitungKelilingPersegi(){
        int hasil = 4 * sisi;
        System.out.println("Keliling Persegi " + namaPersegi + " adalah : " + hasil);
    }
}