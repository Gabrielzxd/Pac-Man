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

    public void moveHorizontal(int x, Movimento movimento){
        if (movimento == Movimento.LEFT){
            this.x = x - 1;
        }
        if (movimento == Movimento.RIGHT){
            this.x = x + 1;
        }
    }

    public void moveVertical(int y, Movimento movimento){
        if (movimento == Movimento.UP){
            this.y = y + 1;
        }
        if (movimento == Movimento.DOWN){
            this.y = y - 1;
        }
    }


}
