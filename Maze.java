import java.io.BufferedReader;
import java.io.FileReader;

public class Maze{
    private int[][] map = new int[32][28];

    public boolean isWall(int x, int y){
        if (map[x][y] == -1){
            return true;
        } else{
            return false;
        }
    }
    // o código acima ele não é muito útil, porque o pacman não estará em cima da posição que é uma parede,
    // então eu tenho que ver primeiro como vou fazer a movimentação para que eu possa fazer uma checagem mais inteligente em cima disso.

    public boolean haspellot(int x, int y){
        if(map[x][y] == 1){
            return true;
        } else{
            return false;
        }
    }

    public void eatPellot(int x, int y){
        if (map[x][y] == 1){
            map[x][y] = 0;
        }
    }

    public Maze(){
        String pathMaze = "/home/gabriel/Pac-Man/Maze";
        BufferedReader reader = null;
        try{
            FileReader readerFile = new FileReader(pathMaze);
            reader = new BufferedReader(readerFile);
            int i = 0;
            String line = reader.readLine();
            while (line != null){
                for(int j = 0; j < line.length(); j++){
                    if(line.charAt(j) == '#'){
                        map[i][j] = -1;
                    }
                    if(line.charAt(j) == '.'){
                        map[i][j] = 1;
                    }
                    if(line.charAt(j) == '-'){
                        map[i][j] = 0;
                    }
                }
                i = i + 1;
                line = reader.readLine();
            }
        } catch (Exception erro){
            System.out.println("Erro ao tentar criar o labirinto");
            System.out.println(erro.getMessage());
        }
    }

    public int getTile(int row, int col){
        return this.map[row][col];
    }
}
