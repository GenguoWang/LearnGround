import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

public class PercolationStats {
  private double mMean;
  private double mStddev;
  private double lo;
  private double hi;

  public PercolationStats(int n, int trials)    // perform trials independent experiments on an n-by-n grid
  {
    if (n <= 0 || trials <= 0) {
      throw new IllegalArgumentException("n and trials should > 0");
    }
    int[] pos = new int[n * n];
    double[] x = new double[trials];
    for (int k = 0; k < trials; ++k) {
      for (int i = 0; i < n * n; ++i) pos[i] = i;
      StdRandom.shuffle(pos);
      Percolation p = new Percolation(n);
      int cnt = 0;
      while (!p.percolates()) {
        int i = pos[cnt] / n + 1;
        int j = pos[cnt] % n + 1;
        p.open(i, j);
        cnt++;
      }
      // System.out.println("last i:"+(pos[cnt-1]/n+1)+" j:"+(pos[cnt-1]%n+1));
      // System.out.println(p);
      x[k] = (double) cnt / n / n;
    }
    mMean = StdStats.mean(x);
    mStddev = StdStats.stddev(x);
    lo = mMean - 1.96 * mStddev / Math.sqrt(trials);
    hi = mMean + 1.96 * mStddev / Math.sqrt(trials);
  }

  public double mean()                          // sample mean of percolation threshold
  {
    return mMean;
  }

  public double stddev()                        // sample standard deviation of percolation threshold
  {
    return mStddev;
  }

  public double confidenceLo()                  // low  endpoint of 95% confidence interval
  {
    return lo;
  }

  public double confidenceHi()                  // high endpoint of 95% confidence interval
  {
    return hi;
  }

  public static void main(String[] args)    // test client (described below)
  {
    if (args.length != 2) {
      throw new IllegalArgumentException("must have two arguments");
    }
    int n = Integer.parseInt(args[0]);
    int t = Integer.parseInt(args[1]);
    PercolationStats ps = new PercolationStats(n, t);
    System.out.println("mean                    = " + ps.mean());
    System.out.println("stddev                  = " + ps.stddev());
    System.out.println("mean                    = " + ps.mean());
    System.out.println("95% confidence interval = " + ps.confidenceLo() + ", " + ps.confidenceHi());
  }
}
