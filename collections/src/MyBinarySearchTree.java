import java.util.NavigableSet;
import java.util.TreeSet;

public class MyBinarySearchTree<T extends Comparable<T>> implements MyCollection<T> {

    private final TreeSet<T> treeSet = new TreeSet<>();

    @Override
    public int size() {
        return treeSet.size();
    }

    @Override
    public void add(T element) {
        treeSet.add(element);
    }

    @Override
    public T getSmallest() {
        return treeSet.first();
    }

    @Override
    public T getGreatest() {
        return treeSet.last();
    }

    @Override
    public T getKth(int k) {
        // ToDo IMPLEMENT ME!
        return null;
    }

    @Override
    public boolean hasElement(T object) {
        return treeSet.contains(object);
    }

    @Override
    public int getRangeSize(T left, T right) {
        NavigableSet<T> navigableSet = treeSet.tailSet(left, true);
        int count = 0;
        for (T element : navigableSet) {
            if (element.compareTo(right) >= 0) {
                break;
            }
            count++;
        }
        return count;
    }
}
