public class Usuario implements PostarMensagem {
    private String nome;
    private String email;
    public Funcao funcao;
    public Estado estado;

    public void mudarTurno(){
        if(getStatus() == Estado.NORMAL){
            this.estado = Estado.EXTRA;
        }
        if(getStatus() == Estado.EXTRA){
            this.estado = Estado.NORMAL;
        }
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
}