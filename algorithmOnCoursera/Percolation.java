import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {

  private static final int[] DX = {1, -1, 0, 0};
  private static final int[] DY = {0, 0, 1, -1};
  private final WeightedQuickUnionUF uf;
  private final boolean[] flag;
  private final boolean[] top;
  private final boolean[] bottom;
  private final int n;
  private boolean isPercolation = false;

  public Percolation(int n) {
    if (n <= 0) {
      throw new IllegalArgumentException("n should > 0");
    }
    uf = new WeightedQuickUnionUF(n * n);
    flag = new boolean[n * n];
    top = new boolean[n * n];
    bottom = new boolean[n * n];
    this.n = n;
  }

  public void open(int i, int j) {
    if (i < 1 || i > n || j < 1 || j > n) {
      throw new IndexOutOfBoundsException("i j should be 1 <= i <= n, 1 <= j <= n");
    }
    i -= 1;
    j -= 1;
    int point = index(i, j);
    flag[point] = true;
    boolean topFlag = false;
    boolean bottomFlag = false;
    for (int k = 0; k < 4; ++k) {
      int x = i + DX[k];
      int y = j + DY[k];
      int next = index(x, y);
      if (x < 0) {
        topFlag = true;
      } else if (x > n - 1) {
        bottomFlag = true;
      } else if (y >= 0 && y <= n - 1 && flag[next]) {
        int root = uf.find(next);
        topFlag = topFlag || top[root];
        bottomFlag = bottomFlag || bottom[root];
      }
    }
    for (int k = 0; k < 4; ++k) {
      int x = i + DX[k];
      int y = j + DY[k];
      int next = index(x, y);
      if (x >= 0 && x <= n - 1 && y >= 0 && y <= n - 1 && flag[next]) {
        uf.union(point, next);
      }
    }
    int root = uf.find(point);
    top[root] = topFlag;
    bottom[root] = bottomFlag;
    if (topFlag && bottomFlag) {
      isPercolation = true;
    }
  }

  public boolean isOpen(int i, int j) {
    if (i < 1 || i > n || j < 1 || j > n) {
      throw new IndexOutOfBoundsException("i j should be 1 <= i <= n, 1 <= j <= n");
    }
    i -= 1;
    j -= 1;
    return flag[index(i, j)];
  }

  public boolean isFull(int i, int j) {
    if (i < 1 || i > n || j < 1 || j > n) {
      throw new IndexOutOfBoundsException("i j should be 1 <= i <= n, 1 <= j <= n");
    }
    i -= 1;
    j -= 1;
    int root = uf.find(index(i, j));
    return top[root];
  }

  public boolean percolates() {
    return isPercolation;
  }

  private int index(int i, int j) {
    return i * n + j;
  }

  /*
  @Override
  public String toString() {
    StringBuffer sb = new StringBuffer(n * n);
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        int point = index(i, j);
        sb.append(flag[point] ? '*' : '_');
      }
      sb.append('\n');
    }
    return sb.toString();
  }
  */
}
