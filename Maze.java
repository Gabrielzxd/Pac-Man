import java.io.BufferedReader;
import java.io.FileReader;

public class Maze{
    private int[][] map = new int[32][28];

    public boolean isWall(int x, int y){

    }

    public boolean haspellot(int x, int y){

    }

    public void eatPellot(int x, int y){

    }

    public Maze(){
        String layout = "/home/gabriel/Pac-Man/Maze";
        BufferedReader reader = null;
        try{
            FileReader readerFile = new FileReader(layout);
            reader = new BufferedReader();

        } catch (Exception erro){
            System.out.println("Erro ao tentar criar o labirinto");
            System.out.println(erro.getMessage());
        }
    }

    public int getTile(int row, int col){
        return this.map[row][col];
    }
}
