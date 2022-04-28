//Nome: Johannes Mattheus Krouwel
//RA: 20.01248-9

public class Veiculos {
    String nome;
    double id;
    double custoporhora;

    void Veiculo(String nome, double id, double custoporhora){
        this.nome = nome;
        this.id = id;
        this.custoporhora = custoporhora;
    }

    Veiculo Carro = new Veiculo();
    Carro.nome = "Carro";
    Carro.id = 11111;
    Carro.custoporhora = 100;

    Veiculo Moto = new Veiculo();
    Moto.nome = "Moto";
    Moto.id = 22222;
    Moto.custoporhora = 50;

    Veiculo Bicicleta = new Veiculo();
    Bicicleta.nome = "Bicicleta";
    Bicicleta.id = 33333;
    Bicicleta.custoporhora = 10;

    Veiculo Patinete = new Veiculo();
    Patinete.nome = "Patinete";
    Patinete.id = 44444;
    Patinete.custoporhora = 5;
}