package br.com.gabrielzxd.pacman.engine;

import java.io.BufferedReader;
import java.io.FileReader;

public class Maze {
    private int[][] map = new int[32][28];

    public boolean isWall(Move move, int x, int y) {
        switch (move) {
            case UP:
                return this.map[x][y + 1] == -1;
            case DOWN:
                return this.map[x][y - 1] == -1;
            case LEFT:
                return this.map[x - 1][y] == -1;
            default:
                return this.map[x + 1][y] == -1;
        }
    }
    public boolean hasPellot(int x, int y) {
        if (map[x][y] == 1) {
            return true;
        } else {
            return false;
        }
    }

    public void eatPellot(int x, int y) {
        if (map[x][y] == 1) {
            map[x][y] = 0;
        }
    }

    public Maze() {
        String pathMaze = "/home/gabriel/Pac-Man/src.main.java.br.com.gabrielzxd.pacman.engine.Maze";
        BufferedReader reader = null;
        try {
            FileReader readerFile = new FileReader(pathMaze);
            reader = new BufferedReader(readerFile);
            int i = 0;
            String line = reader.readLine();
            while (line != null) {
                for (int j = 0; j < line.length(); j++) {
                    if (line.charAt(j) == '#') {
                        map[i][j] = -1;
                    }
                    if (line.charAt(j) == '.') {
                        map[i][j] = 1;
                    }
                    if (line.charAt(j) == '-') {
                        map[i][j] = 0;
                    }
                }
                i = i + 1;
                line = reader.readLine();
            }
        } catch (Exception erro) {
            System.out.println("Erro ao tentar criar o labirinto");
            System.out.println(erro.getMessage());
        }
    }
    // estudar um pouco mais de exceptions e depois melhorar esta parte.

    public int getTile(int row, int col) {
        return this.map[row][col];
    }
}