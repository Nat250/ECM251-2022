//Nome: Johannes Mattheus Krouwel
//RA: 20.01248-9

public class Usuarios {
    private String senha;
    private String nome;
    private String email;

    public Usuarios(String nome, String cpf, String email){
        this.nome = nome;
        this.senha = senha;
        this.email = email;
    }

    public String getNome(){
        return nome;
    }

    public void setNome(String nome){
        this.nome = nome;
        }

    public String getEmail(){
        return email;
    }

    public void setEmail(String email){
        this.email = email;
    }

    public String getSenha(){
        return senha;
    }

    public void setSenha(String email){
        this.senha = senha;
    }
}