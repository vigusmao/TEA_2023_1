import java.util.ArrayList;
import java.util.Collections;

public class MyOrderedArrayList<T extends Comparable<T>> implements MyCollection<T> {

    private final ArrayList<T> arrayList = new ArrayList<>();

    @Override
    public int size() {  // O(1)
        return arrayList.size();
    }

    @Override
    public void add(T element) {  // O(n)
        int index = findInsertionIndex(element);

        this.arrayList.add(null);
        for (int i = size() - 2; i >= index; i--) {
            this.arrayList.set(i + 1, this.arrayList.get(i));
        }
        this.arrayList.set(index, element);
    }

    @Override
    public T getSmallest() {  // O(1)
        return size() == 0 ? null : arrayList.get(0);
    }

    @Override
    public T getGreatest() {  // O(1)
        int size = size();
        return size == 0 ? null : arrayList.get(size - 1);
    }

    @Override
    public T getKth(int k) {
        // ToDo IMPLEMENT ME!
        return null;
    }

    @Override
    public boolean hasElement(T object) {  // O(log n)
        return Collections.binarySearch(this.arrayList, object) >= 0;
    }

    @Override
    public int getRangeSize(T left, T right) {  // O(log n)
        if (size() == 0) return 0;
        int leftIndex = findInsertionIndex(left);
        int rightIndex = findInsertionIndex(right);
        return rightIndex - leftIndex;
    }

    @Override
    public String toString() {
        return this.arrayList.toString();
    }

    private int findInsertionIndex(T element) {
        int result = Collections.binarySearch(this.arrayList, element);
        if (result < 0) {
            result = -(result + 1);
        }
        return result;
    }
}
