//Nome: Johannes Mattheus Krouwel
//RA: 20.01248-9

public class Usuario {
    String nome;
    Veiculo veiculo;

    void Usuario(String nome, Veiculo veiculo){
        this.nome = nome;
        this.veiculo = veiculo;
    }

    void testar(Usuario usuarioA, Usuario usuarioB){
        System.out.println("Nome do primeiro:" + usuarioA.nome);
        System.out.println("Veiculo antigo do primeiro:" + usuarioA.veiculo.nome);
        System.out.println("ID antigo do primeiro:" + usuarioA.veiculo.id);
        System.out.println("custoporhora antigo do primeiro:" + usuarioA.veiculo.custoporhora);

        System.out.println("Nome do segundo:" + usuarioB.nome);
        System.out.println("Veiculo antigo do segundo:" + usuarioA.veiculo.nome);
        System.out.println("ID antigo do segundo:" + usuarioA.veiculo.id);
        System.out.println("custoporhora antigo do segundo:" + usuarioA.veiculo.custoporhora);

        System.out.println("=================================");

        Usuario AUX = Usuario usuarioA;
        Usuario usuarioA.nome = Usuario usuarioB.nome;
        Usuario usuarioA.veiculo.nome = Usuario usuarioB.veiculo.nome;
        Usuario usuarioA.veiculo.id = Usuario usuarioB.veiculo.id;
        Usuario usuarioA.veiculo.custoporhora = Usuario usuarioB.veiculo.custoporhora;

        Usuario usuarioB.nome = Usuario AUX.nome;
        Usuario usuarioB.veiculo.nome = Usuario AUX.veiculo.nome;
        Usuario usuarioB.veiculo.id = Usuario AUX.veiculo.id;
        Usuario usuarioB.veiculo.custoporhora = Usuario AUX.veiculo.custoporhora;

        System.out.println("Nome do primeiro:" + usuarioA.nome);
        System.out.println("Veiculo novo do primeiro:" + usuarioA.veiculo.nome);
        System.out.println("ID novo do primeiro:" + usuarioA.veiculo.id);
        System.out.println("custoporhora novo do primeiro:" + usuarioA.veiculo.custoporhora);

        System.out.println("Nome do segundo:" + usuarioB.nome);
        System.out.println("Veiculo novo do segundo:" + usuarioA.veiculo.nome);
        System.out.println("ID novo do segundo:" + usuarioA.veiculo.id);
        System.out.println("custoporhora novo do segundo:" + usuarioA.veiculo.custoporhora);
    }
}
