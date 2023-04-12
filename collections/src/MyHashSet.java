import java.util.HashSet;

public class MyHashSet<T extends Comparable<T>> implements MyCollection<T> {

    private final HashSet<T> hashSet = new HashSet<>();

    @Override
    public int size() {
        return hashSet.size();
    }

    @Override
    public void add(T element) {
        hashSet.add(element);
    }

    @Override
    public T getSmallest() {  // O(n)
        T result = null;
        for (T element : hashSet) {
            if (result == null || element.compareTo(result) < 0) {
                result = element;
            }
        }
        return result;
    }

    @Override
    public T getGreatest() {  // O(n)
        T result = null;
        for (T element : hashSet) {
            if (result == null || element.compareTo(result) > 0) {
                result = element;
            }
        }
        return result;
    }

    @Override
    public T getKth(int k) {
        return null;
    }

    @Override
    public boolean hasElement(T object) {
        return hashSet.contains(object);
    }

    @Override
    public int getRangeSize(T left, T right) {
        int result = 0;
        for (T element : hashSet) {
            if (element.compareTo(left) >= 0 && element.compareTo(right) < 0) {
                result++;
            }
        }
        return result;
    }
}
