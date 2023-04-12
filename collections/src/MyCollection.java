public interface MyCollection<T extends Comparable<T>> {

    int size();

    void add(T element);

    T getSmallest();

    T getGreatest();

    T getKth(int k);

    boolean hasElement(T object);

    /**
     * @param left the start of the range (inclusive)
     * @param right the end of the range (exclusive)
     *
     * @return the number of elements X in this collection such that left <= X < right;
     *         zero, if no element exists in the specified range.
     */
    int getRangeSize(T left, T right);
}
