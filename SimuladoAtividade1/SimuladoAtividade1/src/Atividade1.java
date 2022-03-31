//Nome: Johannes Mattheus Krouwel
//RA: 20.01248-9

public class Atividade1 {
    public void run(){
        Usuarios usuario1 = new Usuarios("Usuario1", "123", "onomenaoimporta@gmail.com");
        Usuarios usuario2 = new Usuarios("Usuario2", "123456", "onomenaoimporta2@gmail.com");
        Usuarios usuario3 = new Usuarios("Usuario3", "123456", "onomenaoimporta3@gmail.com");

        Conta conta1 = new Conta(9865,
        usuario1);
        Conta conta2 = new Conta(9865,
        usuario2);
        Conta conta3 = new Conta(9865,
        usuario3);

        int valor1 = 1000;
        int valor2 = 250;
        int valor3 = 3000;

        conta1.depositar(valor1);
        conta2.depositar(valor2);
        conta3.depositar(valor3);

        conta1.depositar(valor2);
        conta2.remover(valor2);
        conta1.depositar(valor2);
        conta3.remover(valor2);
        conta1.depositar(valor2);
        conta2.remover(valor2);

        conta2.depositar(valor1);
        conta3.remover(valor2);

        System.out.println(conta1);
        System.out.println(conta2);
        System.out.println(conta3);
    }
}