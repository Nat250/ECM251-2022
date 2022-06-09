public class App {
    public static void main(String[] args){
        Usuario usuario1 = new Usuario("A","A@email.com",Funcao.MOBILE_MEMBERS,Estado.NORMAL);
        Usuario usuario2 = new Usuario("B","B@email.com",Funcao.HEAVY_LIFTERS,Estado.NORMAL);
        Usuario usuario3 = new Usuario("C","C@email.com",Funcao.SCRIPT_GUYS,Estado.NORMAL);
        Usuario usuario4 = new Usuario("D","D@email.com",Funcao.BIG_BROTHERS,Estado.NORMAL);

        EnviarMensagem(usuario1);
        EnviarMensagem(usuario2);
        EnviarMensagem(usuario3);
        EnviarMensagem(usuario4);

        mudarTurno(usuario1);
        mudarTurno(usuario2);
        mudarTurno(usuario3);
        mudarTurno(usuario4);

        EnviarMensagem(usuario1);
        EnviarMensagem(usuario2);
        EnviarMensagem(usuario3);
        EnviarMensagem(usuario4);

        mudarTurno(usuario1);
        mudarTurno(usuario2);
        mudarTurno(usuario3);
        mudarTurno(usuario4);

        EnviarMensagem(usuario1);
        EnviarMensagem(usuario2);
        EnviarMensagem(usuario3);
        EnviarMensagem(usuario4);
    }
}
