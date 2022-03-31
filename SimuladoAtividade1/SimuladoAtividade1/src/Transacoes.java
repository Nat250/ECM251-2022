//Nome: Johannes Mattheus Krouwel
//RA: 20.01248-9

public class Transacoes {
    private int idConta;
    private String nome;

    public String printValor(double valor){
        return String.format("%f;%f;%f", idConta, nome, valor);
    }
}
