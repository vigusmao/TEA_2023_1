import java.util.ArrayList;

public class MyUnorderedArrayList<T extends Comparable<T>> implements MyCollection<T> {

    private final ArrayList<T> arrayList = new ArrayList<>();

    @Override
    public int size() {
        return arrayList.size();
    }

    @Override
    public void add(T element) {
        arrayList.add(element);
    }

    @Override
    public T getSmallest() {
        T smallest = null;
        for (T element : this.arrayList) {
            if (smallest == null || element.compareTo(smallest) < 0) {
                smallest = element;
            }
        }
        return smallest;
    }

    @Override
    public T getGreatest() {
        T greatest = null;
        for (T element : this.arrayList) {
            if (greatest == null || element.compareTo(greatest) > 0) {
                greatest = element;
            }
        }
        return greatest;
    }

    @Override
    public T getKth() {
        // ToDo IMPLEMENT ME!
        return null;
    }

    @Override
    public boolean hasElement(T object) {
        for (T element : this.arrayList) {
            if (element.equals(object)) {
                return true;
            }
        }
        return false;
    }

    @Override
    public int getRangeSize(T left, T right) {
        int count = 0;
        for (T element: this.arrayList) {
            if (element.compareTo(left) >= 0 && element.compareTo(right) < 0) {
                count++;
            }
        }
        return count;
    }

    @Override
    public String toString() {
        return this.arrayList.toString();
    }
}
