import org.junit.Before;
import org.junit.Test;

import java.util.*;

import static junit.framework.TestCase.*;

public class MyCollectionTest {

    private static final Random random = new Random();

    private List<MyCollection<Integer>> collections;

    @Before
    public void setUp() {
        MyCollection<Integer> unorderedList = new MyUnorderedArrayList<>();
        MyCollection<Integer> orderedList = new MyOrderedArrayList<>();
        MyCollection<Integer> hashSet = new MyHashSet<>();
        MyCollection<Integer> binarySearchTree = new MyBinarySearchTree<>();

        collections = new ArrayList<>();
        collections.add(unorderedList);
//        collections.add(orderedList);
//        collections.add(hashSet);
//        collections.add(binarySearchTree);
    }

    @Test
    public void testEverything() {
        for (MyCollection<Integer> collection : collections) {
            assertEquals(0, collection.size());

            collection.add(5);
            collection.add(89);
            collection.add(-13);
            collection.add(0);
            collection.add(3);
            collection.add(55);
            collection.add(-6);

            System.out.println(collection.getClass().getName() + ": " + collection);

            assertEquals(7, collection.size());

            assertTrue(collection.hasElement(5));
            assertTrue(collection.hasElement(89));
            assertTrue(collection.hasElement(-13));
            assertTrue(collection.hasElement(0));
            assertTrue(collection.hasElement(3));
            assertTrue(collection.hasElement(55));
            assertTrue(collection.hasElement(-6));

            assertFalse(collection.hasElement(2222));

            assertEquals(-13, (int) collection.getSmallest());
            assertEquals(89, (int) collection.getGreatest());

            assertEquals(3, collection.getRangeSize(0, 40));
            assertEquals(2, collection.getRangeSize(0, 5));
        }
    }

    @Test
    public void compareTimesToAddElements() {
        int N = 8_000_000;

        System.out.println("\nINSERT");
        for (MyCollection<Integer> collection : collections) {
            long start = System.nanoTime();
            populateMyCollection(collection, N);
            printDuration(collection, "add " + N + " elements", start);
        }
    }

    @Test
    public void compareTimesToLookupElements() {
        int N = 4_000_000;

        Set<Integer> allElements = new HashSet<>();
        while (allElements.size() < N) {
            allElements.add(random.nextInt(2 * N));
        }

        System.out.println("\nLOOK UP");
        for (MyCollection<Integer> collection : collections) {
            populateMyCollection(collection, allElements);
            long start = System.nanoTime();
            int countFound = 0;
            for (int i = 0; i < N; i++) {
                if (collection.hasElement(i)) {
                    countFound++;
                }
            }

            printDuration(collection, String.format("lookup " + N + " elements (found %d)", countFound), start);
        }
    }

    @Test
    public void compareTimesToGetSmallest() {
        int N = 8_000_000;

        Set<Integer> allElements = new HashSet<>();
        while (allElements.size() < N) {
            allElements.add(random.nextInt(2 * N));
        }

        System.out.println("\nGET SMALLEST");
        for (MyCollection<Integer> collection : collections) {
            populateMyCollection(collection, allElements);
            long start = System.nanoTime();
            int smallest = collection.getSmallest();
            printDuration(collection, String.format("find %d", smallest), start);
        }
    }

    @Test
    public void compareTimesToGetRangeSize() {
        int N = 8_000_000;

        Set<Integer> allElements = new HashSet<>();
        while (allElements.size() < N) {
            allElements.add(random.nextInt(2 * N));
        }

        System.out.println("\nGET RANGE SIZE");
        for (MyCollection<Integer> collection : collections) {
            populateMyCollection(collection, allElements);
            long start = System.nanoTime();
            int rangeSize = collection.getRangeSize(1000, 50_000);
            printDuration(collection, String.format("find %d", rangeSize), start);
        }
    }

    @Test
    public void compareTimesToGetKth() {
        int N = 8_000_000;

        Set<Integer> allElements = new HashSet<>();
        while (allElements.size() < N) {
            allElements.add(random.nextInt(2 * N));
        }

        System.out.println("\nGET RANGE SIZE");
        for (MyCollection<Integer> collection : collections) {
            populateMyCollection(collection, allElements);
            long start = System.nanoTime();
            int kth = collection.getKth(1);
            printDuration(collection, String.format("find %d", kth), start);
        }
    }

    private void populateMyCollection(MyCollection<Integer> myCollection, int intendedCount) {
        while (myCollection.size() < intendedCount) {
            myCollection.add(random.nextInt());
        }
    }

    private void populateMyCollection(MyCollection<Integer> myCollection, Collection<Integer> source) {
        for (Integer element : source) {
            myCollection.add(element);
        }
    }

    private void printDuration(MyCollection<Integer> collection, String message, long start) {
        System.out.printf("%20s took %.6f seconds to %s%n",
                collection.getClass().getName(),
                (System.nanoTime() - start) / (double) 1_000_000_000,
                message);
    }
}