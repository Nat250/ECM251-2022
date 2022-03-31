//Nome: Johannes Mattheus Krouwel
//RA: 20.01248-9

public class Conta {
    private int idConta;
    private double saldo;
    private Usuarios usuario;

    //Construtor
    public Conta(int idConta, Usuarios usuario){
        this.idConta = idConta;
        this.usuario = usuario;
        saldo = 0;
    }

    public String visualizarSaldo(){
        return String.format("R$%.2f", saldo);
    }
    public boolean depositar(double valor){
        if(valor < 0) 
            return false;
        this.saldo += valor;
        return true;
    }
    public boolean remover(double valor){
        if(valor < 0) 
            return false;
        this.saldo -= valor;
        return true;
    }
    public boolean sacar(double valor){
        if(valor > saldo) return false;
        if(valor < 0) return false;
        this.saldo -= valor;
        return true;
    }
    public boolean transferirDinheiro(double valor, Conta destino){
        if(!sacar(valor)) return false;
        if(!destino.depositar(valor)) return false;
        return true;
    }

    public String toString(){
        return "Numero:"+idConta + "\nCliente:" + usuario.getNome() + "\nSaldo:" + visualizarSaldo();
    }
}