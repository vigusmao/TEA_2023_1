import java.util.ArrayList;
import java.util.Collections;

public class MyOrderedArrayList<T extends Comparable<T>> implements MyCollection<T> {

    private final ArrayList<T> arrayList = new ArrayList<>();

    @Override
    public int size() {
        return arrayList.size();
    }

    @Override
    public void add(T element) {
        int index = binarySearch(element);

        this.arrayList.add(null);
        for (int i = size() - 2; i >= index; i--) {
            this.arrayList.set(i + 1, this.arrayList.get(i));
        }
        this.arrayList.set(index, element);
    }

    @Override
    public T getSmallest() {
        return size() == 0 ? null : arrayList.get(0);
    }

    @Override
    public T getGreatest() {
        int size = size();
        return size == 0 ? null : arrayList.get(size - 1);
    }

    @Override
    public T getKth() {
        // ToDo IMPLEMENT ME!
        return null;
    }

    @Override
    public boolean hasElement(T object) {
        return Collections.binarySearch(this.arrayList, object) >= 0;
    }

    @Override
    public int getRangeSize(T left, T right) {
        if (size() == 0) return 0;
        int leftIndex = binarySearch(left);
        int rightIndex = binarySearch(right);
        return rightIndex - leftIndex;
    }

    @Override
    public String toString() {
        return this.arrayList.toString();
    }

    private int binarySearch(T element) {
        int result = Collections.binarySearch(this.arrayList, element);
        if (result < 0) {
            result = -(result + 1);
        }
        return result;
    }
}
