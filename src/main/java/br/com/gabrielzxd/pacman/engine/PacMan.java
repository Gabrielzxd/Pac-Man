package br.com.gabrielzxd.pacman.engine;

public class PacMan{
    private int x;
    private int y;

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }

    public void moveHorizontal(int x, Move move){
        if (move == Move.LEFT){
            this.x = x - 1;
        }
        if (move == Move.RIGHT){
            this.x = x + 1;
        }
    }

    public void moveVertical(int y, Move move){
        if (move == Move.UP){
            this.y = y + 1;
        }
        if (move == Move.DOWN){
            this.y = y - 1;
        }
    }


}

